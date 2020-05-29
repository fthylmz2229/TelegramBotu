import urllib3
from bs4 import BeautifulSoup

class MeyveSebze():

    def FiyatGetir(self, adi):
        self.adi = adi

        http = urllib3.PoolManager()
        page = http.request('GET', 'https://www.carrefoursa.com/tr/meyve-sebze/c/1014')
        soup = BeautifulSoup(page.data, 'html.parser')
        liste = soup.find('ul', attrs={'class':'product-listing'})
        items = liste.find_all('li')
        result = ""
        for item in items:
            itemName = item.find('span', attrs={'class': 'item-name'})
            if str(self.adi).lower() in str(itemName).lower():
                itemPrice = item.find("span", {"class": "item-price"})
                result = str(itemPrice.text)
                break

        return result