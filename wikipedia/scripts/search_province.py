import time

import requests
import fake_headers
import fake_useragent
import pandas as pd
import tqdm

from core import WekipediaTool
URLS = "http://127.0.0.1:8000/map_basic/provinces"
header = fake_headers.make_header()
ua = fake_useragent.UserAgent().random
print(ua)
# print(header)
header["User-Agent"] = ua
print(header)
def get_provinces_list():
    resp = requests.get(URLS, headers=header)
    print(resp.json())
    for data in resp.json()["data"]:
        yield data["name"]

def main():
    """
    获取省份
    :return:
    """
    wiki = WekipediaTool()
    error_data = []
    result = []
    title = []
    for keyword in tqdm.tqdm(get_provinces_list()):
        title.append(keyword)
        page= wiki.get_page(keyword)
        if page is not None:
            # print(page)
            # 入库
            result.append(page.summary)
        else:
            error_data.append(keyword)
            result.append("")
        time.sleep(2)
    pd.DataFrame({"title": title, "intro": result}).to_excel("provinces.xlsx")
    print(f"Error Data: {error_data}")


if __name__ == "__main__":
    main()
