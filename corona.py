import urllib3
from bs4 import BeautifulSoup

class Corona():

    def GetirTurkiye(self):

        http = urllib3.PoolManager()
        page = http.request('GET', 'https://www.worldometers.info/coronavirus/')
        soup = BeautifulSoup(str(page.data))
        table = soup.find('table', attrs={'class':'main_table_countries'})
        table_body = table.find('tbody')
        data = []
        rows = table_body.find_all('tr')
        for row in rows:
            if "Turkey" in str(row):
                cols = row.find_all('td')
                cols = [ele.text for ele in cols]
                data.append([ele for ele in cols])

        return str("Toplam Vaka: " + data[0][1] + "\nYeni Vaka: " + data[0][2] + "\nToplam Ölüm: " + data[0][3] + "\nYeni Ölüm: " + data[0][4] + "\nToplam İyileşen: " + data[0][5])
