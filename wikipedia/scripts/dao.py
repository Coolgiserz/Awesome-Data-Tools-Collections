# coding: utf-8
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
from urllib.parse import quote_plus
from sqlalchemy import Column, Float, Integer, Numeric, String, Text, Time, text, DateTime
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

import pymysql

# 解决Mac M2芯片MySQLdb不兼容问题
pymysql.install_as_MySQLdb()
import sqlalchemy

# https://github.com/PyMySQL/mysqlclient/issues/496
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configparser import ConfigParser

db_config = ConfigParser()
db_config.read(os.path.join(BASE_DIR, "db.conf"))
section_name = "geo_basic"
db_name = db_config.get(section_name, "DB_NAME")
db_user = db_config.get(section_name, "MYSQL_USER")
db_pwd = db_config.get(section_name, "MYSQL_PWD")
db_host = db_config.get(section_name, "MYSQL_HOST")
db_port = db_config.get(section_name, "MYSQL_PORT")
connect_str = f"postgresql://{db_user}:{quote_plus(db_pwd)}@{db_host}:{db_port}/{db_name}"
class Province(Base):
    __tablename__ = 'province'
    __table_args__ = {'comment': '省份表'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('province_gid_seq'::regclass)"))
    objectid = Column(Numeric)
    name = Column(String(50), comment='省份名')
    shape_leng = Column(Numeric, comment='周长')
    shape_area = Column(Numeric, comment='面积')
    code = Column(Integer, comment='省份编码')
    geo = Column(NullType, comment='地理要素')
    update_time = Column(Time(True), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    intro = Column(Text, comment='省介绍')


class City(Base):
    __tablename__ = 'city'
    __table_args__ = {'comment': '地级市表'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('city_gid_seq'::regclass)"))
    code = Column(Integer, comment='地级市编码')
    shape_leng = Column(Numeric, comment='周长')
    shape_area = Column(Numeric, comment='面积')
    name = Column(String(50), nullable=False, comment='城市名')
    nickname = Column(String(50), comment='别名')
    provincena = Column(String(50), comment='省份名')
    geo = Column(NullType, comment='地理要素')
    update_time = Column(DateTime(True), nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='数据更新时间')
    intro = Column(Text, comment='城市介绍')


class Dao():
    def __init__(self, session=None):
        # pool_recycle=900,每15分钟重建连接（无效）
        # 参考官方文档的连接池配置：https://docs.sqlalchemy.org/en/20/core/pooling.html
        #  pool_size=20, max_overflow=0
        self.engine = create_engine(connect_str, pool_size=20, max_overflow=0, pool_recycle=900)
        if session is not None:
            self.session = session
        else:
            self.session = sessionmaker(self.engine)()
        assert isinstance(self.session, sqlalchemy.orm.session.Session)

    def write_province_intro(self, province_name, intro=None):
        obj = self.session.query(Province).filter(Province.name==province_name).first()
        if intro is not None:
            obj.intro = intro
            self.session.commit()
        print(obj.name, obj.code, obj.intro)

    def write_city_intro(self, city_name, intro=None):
        obj = self.session.query(City).filter(City.name==city_name).first()
        if intro is not None:
            obj.intro = intro
            self.session.commit()
        print(obj.name, obj.code, obj.intro)



if __name__ == "__main__":
    d = Dao()
    # d.write_province_intro("")