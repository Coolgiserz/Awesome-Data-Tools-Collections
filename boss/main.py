import random
import time

import requests
import csv
import json
from urllib.parse import quote
from persists.pgsql import JobListSaver
from entities import JobAbstractModel
import setting

keyword = "知识图谱"
city_code = 101280700
f = open(f'{keyword}_{101280600}.csv',mode='w',newline='',encoding='utf-8-sig')
w_header = csv.DictWriter(f, fieldnames=
['bossName', 'bossTitle', 'jobName', 'salaryDesc', 'jobLabels', 'skills', 'cityName', 'areaDistrict','businessDistrict','brandName','welfareList'])
w_header.writeheader()

saver = JobListSaver()
def check_response(text):
    if "异常" in text:
        return False
    return True
def job_list_fetcher(query, city_code=101280600, page=1, page_size=30):
    """
    工作列表爬取
    :param query:
    :param city_code:
    :param page:
    :param page_size:
    :return:
    """
    base_url =  f'https://www.zhipin.com/'
    url = f'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query={query}&city={city_code}&experience=&degree=&industry=&scale=&stage=&position=&jobType=&salary=&multiBusinessDistrict=&multiSubway=&page={page}&pageSize={page_size}'
    # url = f"https://www.zhipin.com/web/geek/job?query={query}&city=101280100"
    headers = setting.headers
    headers.update({"Cookie": setting.cookie})
    # res = requests.get(url=base_url,headers=headers)
    # if not check_response(res.text):
    #     print(res.text)
    # print(f"cookies: {res.cookies}")

    print(f"url: {url}")
    res = requests.get(url=url,headers=headers)
    print(f"response: {res.status_code}")
    print(f"cookies: {res.cookies}")
    if not check_response(res.text):
        print(res.text)
        print(f"headers: {headers}")
        return
    json_data = res.json()
    boss_list = json_data['zpData'].get('jobList', None)
    if boss_list is None:
        raise Exception("No job list! Check your request")
    dit = {}
    for i in boss_list:
        job = JobAbstractModel(bossName=i['bossName'],
                               bossTitle=i['bossTitle'],
                               jobName=i['jobName'],
                               jobLabels=",".join(i['jobLabels']),
                               salaryDesc=i['salaryDesc'],
                               skills=",".join(i['skills']),
                               cityName=i['cityName'],
                               areaDistrict=i['areaDistrict'],
                               businessDistrict=i['businessDistrict'],
                               brandName=i['brandName'],
                               welfareList=",".join(i['welfareList'])
                               )
        saver.save_to_pgsql(job)
        # # 招聘人
        # dit['bossName'] = i['bossName']
        # # 招聘人职位
        # dit['bossTitle'] = i['bossTitle']
        # # 工作岗位名称
        # dit['jobName'] = i['jobName']
        # # 薪资
        # dit['salaryDesc'] = i['salaryDesc']
        # # 要求
        # dit['jobLabels'] = i['jobLabels']
        # # 工作相关内容
        # dit['skills'] = i['skills']
        # # 详细地址
        # dit['cityName'] = i['cityName']
        # dit['areaDistrict'] = i['areaDistrict']
        # dit['businessDistrict'] = i['businessDistrict']
        # #公司名称
        # dit['brandName'] = i['brandName']
        # # 福利
        # dit['welfareList'] = i['welfareList']
        # print(dit)
        w_header.writerow(dit)
    print('Craw done！')


# %E5%B5%8C%E5%85%A5%E5%BC%8F
print(quote(keyword))
for page in range(1, 100):
    job_list_fetcher(quote(keyword), city_code=city_code, page=page)
    sleep_time = random.randrange(10,15)
    print(f"sleep {sleep_time}s")
    time.sleep(sleep_time)
pass
