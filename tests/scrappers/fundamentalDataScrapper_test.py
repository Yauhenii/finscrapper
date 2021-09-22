import pytest

from app import FundamentalDataScrapper


@pytest.mark.parametrize(
    'ticker, modules', [
        ('^GSPC', ['price'])
    ])
def test_fundamental_data_scrapper(ticker, modules):
    scrapper = FundamentalDataScrapper()
    response = scrapper.get_data(ticker, modules)
    assert response.status_code == 200
