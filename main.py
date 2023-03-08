import requests

from interfaces import WeatherForecast, WeatherCurrent


class WeatherService:

    TOKEN = 'YTI1YWM5ZjctNzFkZi00ZGVmLWE5NDMtZjM5NjUxYzM1MGY5'
    api = 'https://api.m3o.com/v1'
    endpoint = {
        'forecast': api + '/weather/Forecast',
        'now': api + '/weather/Now'
    }

    def get_forecast(self, days: int = 2, location: str = 'London') -> WeatherForecast:
        """ Прогноз погоды. """

        data = {'days': days, 'location': location}
        response = self._query(endpoint=self.endpoint['forecast'], data=data)
        return WeatherForecast.from_dict(response)

    def get_current(self, location: str = 'London') -> WeatherCurrent:
        """ Текущая погода. """

        data = {'location': location}
        response = self._query(endpoint=self.endpoint['now'], data=data)
        return WeatherCurrent.from_dict(response)

    def _query(self, endpoint: str, data: dict) -> dict:
        """ Запрос на сторонний сервис. """

        header = {'Authorization': f'Bearer {self.TOKEN}', 'Content-Type': 'application/json'}
        response = requests.post(endpoint, json=data, headers=header)
        if response.status_code != 200:
            raise ValueError(f'status_code={response.status_code}:{response.text}')

        return response.json()


if __name__ == '__main__':
    print(WeatherService().get_current())
    print(WeatherService().get_forecast())
