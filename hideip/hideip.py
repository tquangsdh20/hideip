import requests


def open_csv(filename) -> list:
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
        requests.get("https://httpbin.org/ip", proxies=proxy(ip), timeout=1)
    except requests.exceptions.ConnectTimeout as e:
        print(e)
        retBool = False
    return retBool


class HideMe:
    def __init__(self, filename: str):
        self.__cur = 0
        self.__ipList = open_csv(filename)
        self.__max = len(self.__ipList)

    def torrent(self):
        self.__cur += 1
        while is_usable(self.__ipList[self.__cur]):
            self.__cur += 1
            self.__cur %= self.__max
        return proxy(self.__ipList[self.__cur])


if __name__ == "__main__":
    file = "./socks5.csv"
    proxies = open_csv(file)
    for ip in proxies:
        if is_usable(ip):
            print(proxy(ip))
