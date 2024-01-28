# @Author: weirdgiser
# @Time: 2024/1/28
# @Function:
import sqlalchemy.exc
from common.dao.base import BaseDAO
from models.company import Company

class CompanyDao(BaseDAO):
    def merge_company(self, **kwargs):
        # Query whether the is exist?
        company_obj = Company(**kwargs)
        try:
            self.session.add(company_obj)
            self.session.commit()
            return True
        except sqlalchemy.exc.IntegrityError:
            self.session.rollback()
            return False
