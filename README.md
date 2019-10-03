# Scraproxy

Proxy listing library useful for using with python [requests](https://requests.readthedocs.io/pt_BR/latest/user/quickstart.html).

## Usage

    >>> import requests
    >>> from scraproxy import Scraproxy
    
    >>> sp = Scraproxy()
    >>> sp.fetch_proxies(only_https=True, allow_transparent=False, country='US')
    
    >>> len(sp.proxies)    
    >>> requests.get('https://httpbin.org/anything', proxies=sp.random_proxy())