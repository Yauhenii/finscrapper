import logging
from typing import List
import requests
from app.scrappers.basicScrapper import BasicScrapper
from app import settings
from app.scrappers.utils.utils import concat_parameters, concat_events

logger = logging.getLogger(settings.logging.NAME)


class PriceDataScrapper(BasicScrapper):
    _prefix_str: str
    _version_str: str
    _path_str: str
    _symbol_str: str
    _period1_str: str
    _period2_str: str
    _interval_str: str
    _prepost_str: str
    _events_str: str
    _template_str: str

    def __init__(self) -> None:
        super().__init__()
        self._prefix_str = settings.yahooscrapper.price.PREFIX
        self._version_str = settings.yahooscrapper.price.VERSION
        self._path_str = settings.yahooscrapper.price.PATH
        self._symbol_str = settings.yahooscrapper.price.SYMBOL
        self._period1_str = settings.yahooscrapper.price.PERIOD1
        self._period2_str = settings.yahooscrapper.price.PERIOD2
        self._interval_str = settings.yahooscrapper.price.INTERVAL
        self._prepost_str = settings.yahooscrapper.price.PREPOST
        self._events_str = settings.yahooscrapper.price.EVENTS
        self._template_str = settings.yahooscrapper.TEMPLATE

    def get_data(self,
                       ticker: str,
                       period1: str = None,
                       period2: str = None,
                       interval: str = None,
                       prepost: str = None,
                       events: List[str] = None,
                       ) -> requests.Response:
        parameters = []
        if ticker:
            symbol_str = self._symbol_str.format(**{'symbol': ticker})
            parameters.append(symbol_str)
        if period1:
            period1_str = self._period1_str.format(**{'period1': period1})
            parameters.append(period1_str)
        if period2:
            period2_str = self._period2_str.format(**{'period2': period2})
            parameters.append(period2_str)
        if interval:
            interval_str = self._interval_str.format(**{'interval': interval})
            parameters.append(interval_str)
        if prepost:
            prepost_str = self._prepost_str.format(
                **{'includePrePost': prepost})
            parameters.append(prepost_str)
        if events:
            joined_events = concat_events(events)
            events_str = self._events_str.format(**{'events': joined_events})
            parameters.append(events_str)

        joined_parameters = concat_parameters(parameters)
        path_str = self._path_str.format(
            **{'ticker': ticker, 'parameters': joined_parameters, })

        # form url
        url = self._template_str.format(
            **{'schema': self._schema_str,
               'prefix': self._prefix_str,
               'host': self._host_str,
               'version': self._version_str,
               'path': path_str, })

        response = self._request(url)
        return response
