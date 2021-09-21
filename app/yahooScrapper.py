from urllib.parse import urljoin
import requests


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
        return response
