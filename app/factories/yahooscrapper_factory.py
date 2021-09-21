from app import YahooScrapper
from app import settings


def get_yahooscrapper() -> YahooScrapper:
    host = settings.yahooscrapper.HOST
    path_template = settings.yahooscrapper.PATH_TEMPLATE
    user_agent = settings.yahooscrapper.USER_AGENT

    scrapper = YahooScrapper(host, path_template, user_agent)
    return scrapper
