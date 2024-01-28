# @Author: weirdgiser
# @Time: 2024/1/28
# @Function: Definition of Company Model

# coding: utf-8
from sqlalchemy import BigInteger, CHAR, Column, Float, Integer, String, Text, text, DATE, TIMESTAMP
# from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry
Base = declarative_base()
metadata = Base.metadata


class Company(Base):
    __tablename__ = 'company'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('company_id_seq'::regclass)"), comment='自增长ID')
    full_name = Column(String(256), nullable=False, comment='企业全称')
    short_name = Column(String(256), comment='企业简称')
    created_at = Column(TIMESTAMP(True), server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    updated_at = Column(TIMESTAMP(True), server_default=text("CURRENT_TIMESTAMP"), comment='数据更新时间')
    insured_people_number = Column(Integer, server_default=text("0"), comment='参保人数')
    business_scope = Column(Text, comment='经营范围')
    registered_address = Column(String(255), comment='企业注册地址')
    english_name = Column(String(256), comment='英文名称')
    region = Column(String(128), comment='所属地区')
    representative = Column(Text, comment='法定代表人')
    registration_status = Column(String(32), comment='登记状态')
    registered_capital_string = Column(String(128), comment='注册资本（字符串）')
    registered_capital_value = Column(Float(53), comment='注册资本（值）')
    registered_capital_unit = Column(String(32), comment='注册资本（单位）')
    registered_capital_currency = Column(CHAR(32), comment='注册资本（币种）')
    founded_date = Column(DATE(), comment='成立日期')
    unified_social_credit_identifier = Column(String(64), unique=True, comment='统一社会信用代码')
    phone = Column(String(64), comment='电话')
    more_phone = Column(Text, comment='更多电话')
    email = Column(String(512), comment='邮箱')
    more_email = Column(Text, comment='更多邮箱')
    province_name = Column(String(64), comment='所属省份')
    city_name = Column(String(64), comment='所属城市')
    district_name = Column(String(64), comment='所属区县名称')
    # mailing_address_point = Column(Geometry('Point', srid=4326), nullable=True, default=None, comment='通信地址（坐标点)')
    type_name = Column(String(64), comment='企业/机构类型（名称）')
    taxpayer_registeration_number = Column(String(32), unique=True, comment='纳税人识别号')
    registration_number = Column(String(64), comment='注册号')
    institution_code = Column(String(64), comment='机构代码')
    insured_number_annal = Column(Integer, comment='参保人数所属年报')
    scale_code = Column(String(8), comment='企业规模编码')
    former_name = Column(String(256), comment='曾用名')
    official_website = Column(Text, comment='官网地址')
    profile = Column(Text, comment='企业简介')
    gb_industry_name = Column(String(32), comment='国标行业门类')
    gb_major_industry_name = Column(String(32), comment='国标行业大类')
    gb_medium_industry_name = Column(String(32), comment='国标行业中类')
    gb_small_industry_name = Column(String(32), comment='国标行业小类')
    approval_date = Column(DATE(), comment='核准日期')
    operating_period = Column(String(128), comment='营业期限')
    mailing_address = Column(String(512), comment='通信地址')
    # registered_address_point = Column(Geometry('Point', srid=4326), nullable=True,  default=None, comment='注册地址坐标点')
    qichacha_category_name = Column(String(32), comment='企查查行业门类')
    qichacha_major_category_name = Column(String(32), comment='企查查行业大类')
    qichacha_medium_category_name = Column(String(32), comment='企查查行业中类')
    qichacha_small_category_name = Column(String(32), comment='企查查行业小类')
    data_source_id = Column(Integer, comment='数据源ID')
    nick_name = Column(String(32), comment='别称')
    country_name = Column(String(64), comment='所属国家名称')
