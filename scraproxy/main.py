import random
import requests
from lxml import html

class Scraproxy:

    proxies = []
    proxy_index = 'https://free-proxy-list.net/'

    def fetch_proxies(self, only_https=False, allow_transparent=True, country=''):
        self.proxies = []
        page = requests.get(self.proxy_index, headers={'User-Agent':'Mozilla/5.0'})
        tree = html.fromstring(page.content)
        trs = tree.xpath('//table[@width="100%"]//tr')

        for tr in trs:
            _country = tr.xpath('td[3]/text()')
            _category = tr.xpath('td[5]/text()')
            _https = tr.xpath('td[7][@class="hx"]/text()')
            if not len(_country) and not len(_category) and not len(_https):
                continue

            if only_https and _https[0] != 'yes':
                continue

            if not allow_transparent and _category[0] == 'transparent':
                continue

            if country and country != _country[0]:
                continue

            ip = tr.xpath('td[1]/text()')[0]
            port = tr.xpath('td[2]/text()')[0]

            proxy = {'http': f"http://{ip}:{port}"}
            proxy['https'] = f"https://{ip}:{port}" if _https[0] == 'yes' else ''

            self.proxies.append(proxy)

    def random_proxy(self):
        return self.proxies[random.randrange(len(self.proxies))]