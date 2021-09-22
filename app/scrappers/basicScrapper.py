from typing import List
import logging
import requests
from app import settings

logger = logging.getLogger(settings.logging.NAME)


class BasicScrapper:
    _schema_str: str
    _host_str: str
    _headers: dict

    def __init__(self) -> None:
        self._schema_str = settings.yahooscrapper.SCHEMA
        self._host_str = settings.yahooscrapper.HOST
        self._headers = {
            'user-agent': settings.yahooscrapper.USER_AGENT,
        }

    def _request(self, url) -> requests.Response:
        response = requests.get(url, headers=self._headers)
        logger.debug(f'Response code: {response.status_code}')
        return response
    
    def get_data(self, *args, **kwargs):
        pass
