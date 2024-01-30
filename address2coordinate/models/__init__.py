# @Author: weirdgiser
# @Time: 2024/1/29
# @Function:

# coding: utf-8
from sqlalchemy import BigInteger, Boolean, Column, Integer, String, UniqueConstraint, Text, DateTime, Date, CHAR, Float,text
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry
Base = declarative_base()
metadata = Base.metadata


class PoiAddressCoordinateLog(Base):
    __tablename__ = 'poi_address_coordinate_log'
    __table_args__ = (
        UniqueConstraint('search_keyword', 'data_source', 'formatted_address'),
        {'comment': '兴趣点坐标查询日志'}
    )

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('poi_address_coordinate_log_id_seq'::regclass)"), comment='自增长ID')
    search_keyword = Column(String(512), nullable=False, comment='搜索关键词')
    formatted_address = Column(String(512), comment='格式化后的地址（搜索结果，网络地理编码数据库中的地址名）')
    province_name = Column(String(64))
    city_name = Column(String(64), comment='城市名')
    adcode = Column(String(32), comment='高德地图区划行政编码')
    level = Column(String(32))
    data_source = Column(String(32), comment='数据源*（高德、百度、...）')
    record_count = Column(Integer, comment='结果数量（如果大于1个，说明坐标可能不太精确）')
    status = Column(Boolean, nullable=False, server_default=text("false"), comment='状态（是否完成采集）')
    created_at = Column(TIMESTAMP(True, 0), server_default=text("CURRENT_TIMESTAMP"))
    district = Column(String(32))
    geo = Column(Geometry("POINT"))
    country_name = Column(String(64))
    street = Column(String(32))


class Company(Base):
    __tablename__ = 'company'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('company_id_seq'::regclass)"), comment='自增长ID')
    full_name = Column(String(256), nullable=False, comment='企业全称')
    short_name = Column(String(256), comment='企业简称')
    insured_people_number = Column(Integer, server_default=text("0"), comment='参保人数')
    business_scope = Column(Text, comment='经营范围')
    registered_address = Column(String(255), comment='企业注册地址')
    english_name = Column(String(256), comment='英文名称')
    region = Column(String(128), comment='所属地区')
    representative = Column(Text, comment='法定代表人')
    registration_status = Column(String(32), comment='登记状态')
    registered_capital_value = Column(Float(53), comment='注册资本（值）')
    registered_capital_unit = Column(String(32), comment='注册资本（单位）')
    registered_capital_currency = Column(CHAR(32), comment='注册资本（币种）')
    unified_social_credit_identifier = Column(String(64), unique=True, comment='统一社会信用代码')
    phone = Column(String(64), comment='电话')
    more_phone = Column(Text, comment='更多电话')
    email = Column(String(512), comment='邮箱')
    more_email = Column(Text, comment='更多邮箱')
    province_name = Column(String(64), comment='所属省份')
    city_name = Column(String(64), comment='所属城市')
    district_name = Column(String(64), comment='所属区县名称')
    mailing_address_point = Column(Geometry("POINT"), comment='通信地址（坐标点)')
    type_name = Column(String(64), comment='企业/机构类型（名称）')
    taxpayer_registeration_number = Column(String(32), unique=True, comment='纳税人识别号')
    registration_number = Column(String(64), comment='注册号')
    institution_code = Column(String(64), comment='机构代码')
    insured_number_annal = Column(Integer, comment='参保人数所属年报')
    scale_code = Column(String(8), comment='企业规模编码')
    former_name = Column(String(512), comment='曾用名')
    official_website = Column(Text, comment='官网地址')
    profile = Column(Text, comment='企业简介')
    gb_industry_name = Column(String(32), comment='国标行业门类')
    gb_major_industry_name = Column(String(32), comment='国标行业大类')
    gb_medium_industry_name = Column(String(32), comment='国标行业中类')
    gb_small_industry_name = Column(String(32), comment='国标行业小类')
    operating_period = Column(String(128), comment='营业期限')
    mailing_address = Column(Text, comment='通信地址')
    registered_address_point = Column(Geometry("POINT"), comment='注册地址坐标点')
    qichacha_category_name = Column(String(32), comment='企查查行业门类')
    qichacha_major_category_name = Column(String(32), comment='企查查行业大类')
    qichacha_medium_category_name = Column(String(32), comment='企查查行业中类')
    qichacha_small_category_name = Column(String(32), comment='企查查行业小类')
    data_source_id = Column(Integer, comment='数据源ID')
    nick_name = Column(String(32), comment='别称')
    country_name = Column(String(64), comment='所属国家名称')
    registered_capital_string = Column(String(128), comment='注册资本（字符）')
    created_at = Column(DateTime(True), server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime(True), server_default=text("CURRENT_TIMESTAMP"))
    approval_date = Column(Date)
    founded_date = Column(Date)
