from hideip import __version__
from hideip import proxy
import pytest


def test_version():
    assert __version__ == "0.1.0"


# Unit test for functions
@pytest.mark.parametrize(
    "ip, expected",
    [
        ("0", {"http": "socks5://0", "https": "socks5://0"}),
        (
            "185.245.182.106:1080",
            {
                "http": "socks5://185.245.182.106:1080",
                "https": "socks5://185.245.182.106:1080",
            },
        ),
        (
            "127.0.0.1",
            {"http": "socks5://127.0.0.1", "https": "socks5://127.0.0.1"}
        ),
        (
            "192.168.1.1",
            {"http": "socks5://192.168.1.1", "https": "socks5://192.168.1.1"},
        ),
    ],
)
def test_proxy(ip, expected):
    assert proxy(ip) == expected


def test_HideMe(url_connection):
    assert url_connection.status_code == 200
