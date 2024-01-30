# @Author: weirdgiser
# @Time: 2024/1/29
# @Function:
import sqlalchemy.exc

from common.dao.base import BaseDAO
from models import Company, PoiAddressCoordinateLog
from sqlalchemy import and_
from sqlalchemy.sql import func
from geoalchemy2.functions import ST_GeomFromEWKT, ST_GeomFromText
class CompanyAddressDao(BaseDAO):
    def get_company_objs_with_null_mailing_point_address(self, limit=10):
        company_objs = self.session.query(Company.full_name, Company.mailing_address).filter(and_(Company.mailing_address_point==None, Company.mailing_address!=None)).limit(limit).all()
        return company_objs

    def write_mailing_address_point(self, mailing_address, point):
        objs = self.session.query(Company).filter_by(mailing_address=mailing_address).all()
        for obj in objs:
            obj.mailing_address_point = point
        self.session.commit()

class PoiSearchDao(BaseDAO):
    def insert_log(self, **kwargs):
        search_address = kwargs.get("search_address", None)
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
        try:
            obj = PoiAddressCoordinateLog(**kwargs, data_source=data_source)

            self.session.add(obj)
            self.session.commit()
        except sqlalchemy.exc.IntegrityError:
            self.session.rollback()

