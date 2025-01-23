from dataclasses import dataclass
from subprocess import Popen, PIPE
# from typing import Literal
import ast

import config
from exceptions import CantGetCoordinates


@dataclass(slots=True, frozen=True)
class Coordinates:
    longitude: float
    latitude: float


def get_gps_coordinates() -> Coordinates:
    """Returns current coordinates"""
    coordinates = _get_whereami_coordinates()
    return _round_coordinates(coordinates)


def _get_whereami_coordinates() -> Coordinates:
    whereami_output = _get_whereami_output()
    coordinates = _parse_coordinates(whereami_output)
    return coordinates


def _get_whereami_output() -> bytes:
    process = Popen(["curl", "ipinfo.io"], stdout=PIPE)
    output, err = process.communicate()
    exit_code = process.wait()
    if err is not None or exit_code != 0:
        raise CantGetCoordinates
    return output


def _parse_coordinates(whereami_output: bytes) -> Coordinates:
    try:
        output = ast.literal_eval(
            whereami_output.decode().strip().lower())
    except UnicodeDecodeError:
        raise CantGetCoordinates
    str_latitude, str_longitude = output["loc"].split(",")
    return Coordinates(
        latitude=_parse_float_coordinate(str_latitude),
        longitude=_parse_float_coordinate(str_longitude)
    )


def _parse_float_coordinate(value: str) -> float:
    try:
        return float(value)
    except ValueError:
        raise CantGetCoordinates


def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    if not config.USE_ROUNDED_COORDS:
        return coordinates
    return Coordinates(*map(
        lambda c: round(c, 1),
        [coordinates.latitude, coordinates.longitude]
    ))


if __name__ == "__main__":
    print(get_gps_coordinates())
