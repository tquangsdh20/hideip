<h1 align="center">HideIP library</h1>

## Installation

**Windows**
```
python -m pip install hideip
```

**macOS**
```
sudo pip install hideip
```

**Linux**
```
pip install hideip
```

## Major Features

- Open file SOCKS5 proxy
- Get the avaiable proxy in the file
- Torrent the proxy

## How to use?

First of all, we need the file SOCKS5 download it from [HideMe](https://hideip.me/en/proxy/socks5list)

```python
from hideip import HideMe

# The path file socks5.csv
file = 'socks5.csv'
hide = HideMe(file)

# Get the avaiable proxy
proxy = hide.torrent()

# Print 
print(proxy)

```

## Use with requests library

The socks5 maybe not support `verify`, therefore we need to set it `False`. We might want to turn off the InsecureRequest warning. 

```python
import requests
from hideip import HideMe


# Turn off warning, please ignore if you don't want
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Get the proxy
file = 'socks5.csv'
hide = HideMe(file)
hideme = hide.torrent()

# Requests
res = requests.get('https://httpbin.org/ip',proxies = hideme, verify = False, timeout = 2)
print(res.text)

```