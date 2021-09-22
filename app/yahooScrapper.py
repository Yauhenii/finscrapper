import re
from typing import List
import logging
import requests
from app import settings

logger = logging.getLogger(settings.logging.NAME)


class YahooScrapper:
    schema: str
    host: str
    headers: dict

    def __init__(self) -> None:
        self.schema = settings.yahooscrapper.SCHEMA
        self.host = settings.yahooscrapper.HOST
        self.headers = {
            'user-agent': settings.yahooscrapper.USER_AGENT,
        }

    def get_data(self, url) -> requests.Response:
        response = requests.get(url, headers=self.headers)
        logger.debug(f'Response code: {response.status_code}')
        return response

    def get_fundamental_data(self, ticker: str, modules: List[str]) -> requests.Response:
        prefix = settings.yahooscrapper.fundata.PREFIX
        version = settings.yahooscrapper.fundata.VERSION
        path = settings.yahooscrapper.fundata.PATH
        template = settings.yahooscrapper.TEMPLATE

        joined_modules = YahooScrapper.concat_modules(modules)
        path = path.format(**{'ticker': ticker, 'modules': joined_modules, })

        # form url
        url = template.format(
            **{'schema': self.schema,
               'prefix': prefix,
               'host': self.host,
               'version': version,
               'path': path, })

        response = self.get_data(url)
        return response

    def get_option_contracts_data(self, ticker: str) -> requests.Response:
        prefix = settings.yahooscrapper.optcontracts.PREFIX
        version = settings.yahooscrapper.optcontracts.VERSION
        path = settings.yahooscrapper.optcontracts.PATH
        template = settings.yahooscrapper.TEMPLATE

        path = path.format(**{'ticker': ticker, })

        # form url
        url = template.format(
            **{'schema': self.schema,
               'prefix': prefix,
               'host': self.host,
               'version': version,
               'path': path, })

        response = self.get_data(url)
        return response

    def get_price_data(self,
                       ticker: str,
                       period1: str = None,
                       period2: str = None,
                       interval: str = None,
                       prepost: str = None,
                       events: List[str] = None,
                       ) -> requests.Response:
        prefix_str = settings.yahooscrapper.price.PREFIX
        version_str = settings.yahooscrapper.price.VERSION
        path_str = settings.yahooscrapper.price.PATH
        symbol_str = settings.yahooscrapper.price.SYMBOL
        period1_str = settings.yahooscrapper.price.PERIOD1
        period2_str = settings.yahooscrapper.price.PERIOD2
        interval_str = settings.yahooscrapper.price.INTERVAL
        prepost_str = settings.yahooscrapper.price.PREPOST
        events_str = settings.yahooscrapper.price.EVENTS
        template_str = settings.yahooscrapper.TEMPLATE

        parameters = []
        if ticker:
            symbol_str = symbol_str.format(**{'symbol':ticker})
            parameters.append(symbol_str)
        if period1:
            period1_str = period1_str.format(**{'period1':period1})
            parameters.append(period1_str)
        if period2:
            period2_str = period2_str.format(**{'period2':period2})
            parameters.append(period2_str)
        if interval:
            interval_str = interval_str.format(**{'interval':interval})
            parameters.append(interval_str)
        if prepost:
            prepost_str = prepost_str.format(**{'includePrePost':prepost})
            parameters.append(prepost_str)
        if events:
            joined_events = YahooScrapper.concat_events(events)
            events_str = events_str.format(**{'events':joined_events})
            parameters.append(events_str)
        
        joined_parameters = YahooScrapper.concat_parameters(parameters)
        path_str = path_str.format(**{'ticker': ticker, 'parameters': joined_parameters,})

        # form url
        url = template_str.format(
            **{'schema': self.schema,
               'prefix': prefix_str,
               'host': self.host,
               'version': version_str,
               'path': path_str, })

        response = self.get_data(url)
        return response
        
    @staticmethod
    def concat_modules(modules):
        separator = '%2C'
        joined = separator.join(modules)
        return joined

    @staticmethod
    def concat_events(events):
        separator = '%7C'
        joined = separator.join(events)
        return joined

    @staticmethod
    def concat_parameters(parameters):
        separator = '&'
        joined = separator.join(parameters)
        return joined
