# @Author: weirdgiser
# @Time: 2024/1/15
# @Function:
import datetime

from entities import JobAbstractModel
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///joblist.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
class Job(Base):
    __tablename__ = 'job_list'
    id = Column(Integer, primary_key=True)
    job_name = Column(String)
    salary_desc = Column(String)
    boss_title = Column(String)
    boss_name = Column(String)
    job_labels = Column(String)
    skills = Column(String)
    city_name = Column(String)
    area_district = Column(String)
    business_district = Column(String)
    created_at = Column(DateTime)
    brand_name = Column(String)
    welfare_list = Column(String)

# Base.metadata.create_all(engine)

class JobSaver:
    def save_to_pgsql(self, obj):
        pass

class JobListSaver(JobSaver):
    def save_to_pgsql(self, obj:JobAbstractModel):
        """
        将岗位简介存入PostgreSQL
        :param obj:
        :return:
        """
        job = Job(job_name=obj.job_name,
                  salary_desc=obj.salary_desc,
                    boss_title = obj.boss_title,
                    boss_name = obj.boss_name,
                    job_labels =  obj.job_labels,
                    skills =  obj.skills,
                    city_name = obj.city_name,
                    area_district = obj.area_district,
                  business_district=obj.business_district,
                  brand_name=obj.brand_name,
                  welfare_list=obj.welfare_list,
                    created_at = datetime.datetime.now(),
                  )
        session.add(job)
        session.commit()
