import requests
from hideip import HideMe
import pytest

@pytest.fixture(scope="session")
def url_connection():
    hm = HideMe('./socks5.csv')
    url = 'https://httpbin.org/ip'
    res = requests.get(url,proxies=hm.torrent(),verify=False)
    yield res
