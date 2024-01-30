# @Author: weirdgiser
# @Time: 2024/1/29
# @Function: Get address From industry.company
import os
from pathlib import Path
from dao import CompanyAddressDao, PoiSearchDao
from settings import ProjectConfigParserProxy, DB_INDUSTRY, DB_GEO_BASIC
pp_proxy = ProjectConfigParserProxy("/Users/weirdgiser/文稿/Projects/Python/Experiments/data_tools_collections/address2coordinate/project.conf")
class MailingAddress2CoordPipeline(object):
    def __init__(self):
        self.company_dao = CompanyAddressDao(pp_proxy.get_database_connect_string(DB_INDUSTRY))
        self.poi_dao = PoiSearchDao(pp_proxy.get_database_connect_string(DB_GEO_BASIC))

    def get_addresses(self):
        return self.company_dao.get_company_objs_with_null_mailing_point_address(limit=100)


    def write_addresses_point(self, **kwargs):
        search_keyword = kwargs.get("search_keyword", None)
        formatted_address = kwargs.get("formatted_address", None)
        country_name = kwargs.get("country_name", None)
        province_name = kwargs.get("province_name", None)
        city_name = kwargs.get("city_name", None)
        district = kwargs.get("district_name", None)
        street = kwargs.get("street", None)
        adcode = kwargs.get("adcode", None)
        level = kwargs.get("level", None)
        data_source = kwargs.get("data_source", "AMAP")
        record_count = kwargs.get("record_count", None)
        status = kwargs.get("status", False)
        geo = kwargs.get("geo", None)
        self.poi_dao.insert_log(**kwargs)

