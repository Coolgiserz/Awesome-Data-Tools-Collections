# @Author: weirdgiser
# @Time: 2024/1/28
# @Function: Store the data to PostgreSQL
# coding: utf-8
import pandas as pd
from sqlalchemy import Column, SmallInteger, String, UniqueConstraint, text
from sqlalchemy.dialects.postgresql import TIME
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class CurrencyMeta(Base):
    __tablename__ = 'currency_meta'
    __table_args__ = (
        UniqueConstraint('country_name', 'currency_code'),
        {'comment': '货币元数据表'}
    )

    id = Column(SmallInteger, primary_key=True, server_default=text("nextval('currency_meta_id_seq'::regclass)"))
    update_time = Column(TIME(True, 0), server_default=text("CURRENT_TIMESTAMP"))
    country_name = Column(String(48), comment='国家名称')
    currency_code = Column(String(32), comment='货币代码')
    currency_number = Column(SmallInteger, comment='货币编号')
    currency_name = Column(String(64), nullable=False, comment='货币名称')

if __name__ == "__main__":
    import sys
    sys.path.append("/Users/weirdgiser/文稿/Projects/Python/Experiments/industry_graph_tool")
    from common.persists.base import BaseDAO
    from setting import get_connect_string
    dao = BaseDAO(get_connect_string("industry"))
    df = pd.read_excel("货币.xlsx")
    for data in df.itertuples():
        currency_number = getattr(data, "currency_number", None)
        if currency_number is not None or str(currency_number)!='nan':
            try:
               currency_number = int(currency_number)
            except:
                currency_number = None
                print(str(currency_number))
        obj = CurrencyMeta(country_name=getattr(data, "country",None),
                     currency_name=getattr(data, "currency",None),
                     currency_number=currency_number,
                     currency_code=getattr(data, "currency_code", None)
                     )
        dao.session.add(obj)
    dao.session.commit()
