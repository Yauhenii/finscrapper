import pytest

from app import get_yahooscrapper


@pytest.mark.parametrize(
    'name, module',[
    ('^GSPC','price')
])
def test_yahooscrapper(name,module):
    scrapper = get_yahooscrapper()
    response = scrapper.get_data(name,module)
    assert response.status_code == 200
