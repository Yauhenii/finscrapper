import pytest

from app import get_yahooscrapper


@pytest.mark.parametrize(
    'ticker, modules', [
        ('^GSPC', ['price'])
    ])
def test_fundamental_data_scrapper(ticker, modules):
    scrapper = get_yahooscrapper()
    response = scrapper.get_fundamental_data(ticker, modules)
    assert response.status_code == 200


@pytest.mark.parametrize(
    'ticker', [
        ('^GSPC')
    ])
def test_option_contracts_scrapper(ticker):
    scrapper = get_yahooscrapper()
    response = scrapper.get_option_contracts_data(ticker)
    assert response.status_code == 200


@pytest.mark.parametrize(
    'ticker,period1,period2,interval,prepost,events', [
        ('^GSPC','0','9999999999','1d','true',['div','split'])
    ])
def test_price_data_scrapper(ticker, period1, period2, interval, prepost, events):
    scrapper = get_yahooscrapper()
    response = scrapper.get_price_data(ticker, period1, period2, interval, prepost, events)
    assert response.status_code == 200
