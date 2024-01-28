# @Author: weirdgiser
# @Time: 2024/1/15
# @Function:

class JobAbstractModel:
    def __init__(self, **kwargs):
        self.boss_name = kwargs.get("bossName", None)
        self.boss_title = kwargs.get("bossTitle", None)
        self.job_name = kwargs.get("jobName", None)
        self.salary_desc = kwargs.get("salaryDesc", None)
        self.job_labels = kwargs.get("jobLabels", None)
        self.skills = kwargs.get("skills", None)
        self.city_name = kwargs.get("cityName", None)
        self.area_district = kwargs.get("areaDistrict", None)
        self.business_district = kwargs.get("businessDistrict",None)
        self.brand_name = kwargs.get("brandName", None)
        self.welfare_list = kwargs.get("welfareList",None)

    def to_json(self):
        pass

    def to_dict(self):
        pass