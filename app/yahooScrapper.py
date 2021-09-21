from re import I
from urllib.parse import urljoin
import logging
import requests
from app import settings

logger = logging.getLogger(settings.logging.NAME)


class YahooScrapper:
    host: str
    path_template: str
    headers: dict

    def __init__(self, host: str, path_template: str, user_agent: str) -> None:
        self.host = host
        self.path_template = path_template
        self.headers = {
            'user-agent': user_agent,
        }

    def get_data(self, name: str, module: str) -> requests.Response:
        path = self.path_template.format(name, module)
        url = urljoin(self.host, path)
        response = requests.get(url, headers=self.headers)
        logger.debug(f'Response code: {response.status_code}')
        return response
