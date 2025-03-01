# Weather CLI Utility

## Описание

**Weather CLI Utility** — это консольная утилита на Python, которая с помощью API предоставляет актуальную информацию о погоде. Вы можете узнать текущий прогноз погоды, ваше местоположение, время восхода и заката солнца.

## Возможности

- Отображение текущей температуры и погодных условий.

- Определение вашего местоположения с помощью геолокации.

- Вывод времени восхода и заката солнца.

- Удобный интерфейс командной строки.

- Сохранение истории запросов в файл history.txt


## Установка

1. Убедитесь, что у вас установлен Python версии 3.8 или выше.

2. Склонируйте репозиторий:

    ```
    git clone https://github.com/yourusername/weather-cli-utility.git
    ```

3. Перейдите в директорию проекта:

    ```
    cd weather-cli-utility
    ```

4. Установите необходимые зависимости:

    ```
    pip install -r requirements.txt
    ```


## Использование

1. Получите API-ключ для работы с сервисом прогноза погоды - OpenWeather('https://openweathermap.org/')

2. Создайте файл `.env` в корневой директории проекта и добавьте ваш API-ключ:

    ```
    OPENWEATHER_API=ваш_api_ключ
    ```

3. Запустите утилиту с помощью команды:

    ```
    ./weather
    ```

4. Следуйте подсказкам в терминале для ввода данных.


## Зависимости

- Python 3.8+

- Requests

- python-dotenv