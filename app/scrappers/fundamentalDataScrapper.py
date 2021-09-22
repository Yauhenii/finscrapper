import logging
from typing import List
import requests
from app.scrappers.basicScrapper import BasicScrapper
from app.scrappers.utils.utils import concat_modules
from app import settings

logger = logging.getLogger(settings.logging.NAME)

class FundamentalDataScrapper(BasicScrapper):
    _prefix_str: str
    _version_str: str
    _path_str: str
    _template_str: str

    def __init__(self) -> None:
        super().__init__()
        self._prefix_str = settings.yahooscrapper.fundata.PREFIX
        self._version_str = settings.yahooscrapper.fundata.VERSION
        self._path_str = settings.yahooscrapper.fundata.PATH
        self._template_str = settings.yahooscrapper.TEMPLATE

    def get_data(self, ticker: str, modules: List[str]) -> requests.Response:
        joined_modules = concat_modules(modules)
        path_str = self._path_str.format(**{'ticker': ticker, 'modules': joined_modules, })

        # form url
        url = self._template_str.format(
            **{'schema': self._schema_str,
               'prefix': self._prefix_str,
               'host': self._host_str,
               'version': self._version_str,
               'path': path_str, })

        response = self._request(url)
        return response