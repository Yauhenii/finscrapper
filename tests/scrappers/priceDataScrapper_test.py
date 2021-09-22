import pytest

from app import PriceDataScrapper


@pytest.mark.parametrize(
    'ticker,period1,period2,interval,prepost,events', [
        ('^GSPC', '0', '9999999999', '1d', 'true', ['div', 'split'])
    ])
def test_price_data_scrapper(ticker, period1, period2, interval, prepost, events):
    scrapper = PriceDataScrapper()
    response = scrapper.get_price_data(
        ticker, period1, period2, interval, prepost, events)
    assert response.status_code == 200
