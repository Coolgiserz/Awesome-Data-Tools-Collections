# 地址转坐标工具

基于高德地理编码API查询地址的坐标，查坐标的的功能实现于main.py下的search_address方法
一个key每日调用限额5000，超出次数会返回{'info': 'USER_DAILY_QUERY_OVER_LIMIT', 'infocode': '10044', 'status': '0'}

## 地理编码/逆地理编码API
- [高德开放平台-地理编码/逆地理编码](https://lbs.amap.com/api/webservice/guide/api/georegeo)

## 类似其它工具
- https://maplocation.sjfkai.com

## TODO
- 扩充key，并行爬取（顺便测试可支持的并发调用数）
- 