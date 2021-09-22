import pytest

from app import OptionContractsDataScrapper


@pytest.mark.parametrize(
    'ticker, modules', [
        ('^GSPC', ['price'])
    ])
def test_fundamental_data_scrapper(ticker, modules):
    scrapper = OptionContractsDataScrapper()
    response = scrapper.get_data(ticker)
    assert response.status_code == 200
