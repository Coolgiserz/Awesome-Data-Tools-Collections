# @Author: weirdgiser
# @Time: 2024/1/28
# @Function:
import random
import time

import requests
from settings import AMAP_KEY
from pipelines.tasks import MailingAddress2CoordPipeline
from geoalchemy2.functions import ST_MakePoint
api = f"https://restapi.amap.com/v3/geocode/geo"

class KeyUsageExceedLimitException(Exception):
    pass
def search_address(address):
    params = {"key": AMAP_KEY,
              "address": address}
    res = requests.get(api, params=params, proxies=None)
    if res.status_code == 200:
        data = res.json()
        info = data.get("info", None)
        if info == "USER_DAILY_QUERY_OVER_LIMIT":
            raise KeyUsageExceedLimitException()
        geocodes = data.get("geocodes", [])
        results = []
        for geocode in geocodes:
            formatted_address = geocode.get("formatted_address", None)
            location = geocode.get("location", None)
            adcode = geocode.get("adcode", None)
            province = geocode.get("province", None)
            city = geocode.get("city", None)
            district = geocode.get("district", None)
            country = geocode.get("country", None)
            street = geocode.get("street", None)
            level = geocode.get("level", None)
            if formatted_address is not None:
                results.append([address, formatted_address, location, adcode, country,province, city, district, street, level])
        return results
    else:
        return None

def main():
    p = MailingAddress2CoordPipeline()
    while True:
        objs = p.get_addresses()
        print(f"{len(objs)}")
        if len(objs) == 0:
            print("=======任务结束======")
            break
        try:
            for obj in objs:
                mailing_address = obj[1]
                print(obj[0], mailing_address )
                result_list = search_address(mailing_address)
                if result_list is None:
                    p.write_addresses_point(search_keyword=mailing_address,status=False)

                for i, result in enumerate(result_list):
                    coord = result[2].split(",")
                    # print(result[2], coord)
                    formatted_address = result[1]
                    # point = ST_GeomFromText(f"POINT({result[2]})")
                    point = ST_MakePoint(coord[0], coord[1])
                    # point = f"POINT({result[2]})"
                    # point =result[2].replace(","," ").replace("，"," ")

                    adcode = result[3]
                    country = result[4]
                    province = result[5]
                    city = result[6]
                    district = result[7]
                    street = result[8]
                    level = result[9]
                    p.write_addresses_point(search_keyword=mailing_address,
                                            formatted_address=formatted_address,
                                            adcode=adcode,
                                            country_name=country,
                                            province_name=province,
                                            city_name=city,
                                            district=district,
                                            street=street,
                                            level=level,
                                            geo=point,
                                            status=True)
                    if i==0:
                        p.company_dao.write_mailing_address_point(mailing_address=mailing_address,
                                                              point=point)
        except KeyUsageExceedLimitException:
            print("Key额度用尽")
            break
        time.sleep(random.randint(3,6))
    print("Done")
if __name__ == "__main__":
    # api = f"https://restapi.amap.com/v3/geocode/geo?key={key}&address=广州塔"

    # # datas = ["东南大学", "中南大学", "中北大学", "西南大学", "西北大学"]
    # # TODO get data from company table
    # datas = ["北京大学", "西南大学"]
    # results = []
    # for data in datas:
    #     r = search_address(data)
    #     results.extend(r)
    #     # TODO store the coordinate to log table
    #     print(f"{data}: {r}")
    # pd.DataFrame(results, columns=["search_address", "formatted_address", "location", "adcode", "country","province", "city", "district", "street", "level"]).to_excel("test.xlsx")
    # res = requests.get(api, proxies=None)

    main()
