import requests
from typing import List
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def open_csv(filename) -> List[str]:
    fh = open(filename, "r")
    retList = []
    for line in fh:
        ip = line.split(",")[0].replace('"', "")
        retList.append(ip)
    return retList


def proxy(ip: str):
    return {"http": f"socks5://{ip}", "https": f"socks5://{ip}"}


def is_usable(ip: str) -> bool:
    retBool = True
    try:
        requests.get(
            "https://httpbin.org/ip",
            proxies=proxy(ip),
            timeout=1,
            verify=False
        )
    except (
        requests.exceptions.ConnectTimeout,
        requests.exceptions.ReadTimeout,
        requests.exceptions.ConnectionError,
    ):
        retBool = False
    return retBool


class HideMe:
    def __init__(self, filename: str):
        self.__cur = 0
        self.__ipList = open_csv(filename)
        self.__max = len(self.__ipList)

    def torrent(self):
        self.__cur += 1
        while is_usable(self.__ipList[self.__cur]) is False:
            self.__cur += 1
            self.__cur %= self.__max
        return proxy(self.__ipList[self.__cur])


if __name__ == "__main__":
    file = "./socks5.csv"
    hm = HideMe(file)
    print(hm.torrent())
    print(hm.torrent())
