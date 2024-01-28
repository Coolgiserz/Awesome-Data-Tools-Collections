import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://www.iban.hk/currency-codes"
columns = ['country', 'currency', 'currency_code', 'currency_number']
def main():
    response = requests.get(url, proxies=None)
    print(response.status_code)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find("table")
    tbody = table.find('tbody')
    # 提取每行(tr)的数据
    rows = tbody.find_all('tr')
    datas = []
    # 遍历每行，提取单元格(td)的数据
    for row in rows:
        cells = row.find_all('td')
        data = [cell.get_text() for cell in cells]
        datas.append(data)
    pd.DataFrame(datas, columns=columns).to_excel("货币.xlsx")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
