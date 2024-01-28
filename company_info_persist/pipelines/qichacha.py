# @Author: weirdgiser
# @Time: 2024/1/28
# @Function:
from pathlib import Path
import tqdm
import os
import re
import datetime
import pandas as pd
from dao import CompanyDao

BASE_DIR = Path(__file__).resolve().parent.parent


def get_currency_name():
    # df =  pd.read_csv(os.path.join(BASE_DIR, "data", "currency_name.csv"))
    # return "|".join(df["currency_name"])
    # 处理常见币种
    return "人民币|美元|欧元|新台币|日元|韩元|澳元"


def get_currency_code():
    # df =  pd.read_csv(os.path.join(BASE_DIR, "data", "currency_code.csv"))
    # return "|".join(df["currency_code"])
    return "HKD|EUR|CNY|USD"


def parse_currency(text):
    """
    TODO: 统一表示：货币编码和货币币种名称
    :param text:
    :return:
    """
    # 定义币种正则表达式模式
    currency_names = get_currency_name()
    currency_codes = get_currency_code()
    # Not working
    pattern = rf'({"|".join([currency_codes, currency_names])})'
    # print(pattern)
    # 使用正则表达式匹配文本
    matches = re.findall(pattern, text)

    # 去重并获取匹配的币种列表
    currencies = list(set(matches))
    return currencies


def extract_number(text):
    if text is None:
        return None
    if isinstance(text, str):
        # text = text.strip().replace(",","").replace("，","")
        pattern = r'(\d{1,}(?:,\d{3})*)(?:\.\d+)?'

        # 使用正则表达式匹配文本
        match = re.search(pattern, text)

        if match:
            # 去除逗号并将结果转换为数值形式
            number = float(match.group().replace(',', ''))
            return number

    return None

def extract_unit(text):
    pattern = r'[\u4e00-\u9fff]+'

    # 匹配汉字
    matches = re.findall(pattern, text)

    # 打印匹配结果
    # print(matches)
    if matches is None or len(matches)==0:
        return None
    else:
        return matches[0]

def get_registered_capital(text):
    """
     注册资本
    :param text:
    :return:
    """
    if text is None:
        return None, None, None
    currency_list = parse_currency(text)
    currency = None
    if len(currency_list) > 0:
        currency = currency_list[0]
    number = extract_number(text)
    unit = extract_unit(text)
    return number, unit, currency


def founded_time_clean(text):
    """
    >>> founded_time_clean("2005-11-03") == datetime.date(year=2005, month=11, day=3)
    :param text:
    :return:
    """
    if text is None:
        return None
    try:
        text = str(text).strip()
        datetime_obj = datetime.datetime.strptime(text, "%Y-%m-%d")
        return datetime_obj
    except:
        return None

def get_company_scale(text):
    if text is None or text == "-":
        return None
    pattern = r'[A-Za-z]+'
    # 匹配模式
    match = re.search(pattern, text)
    if match is not None:
        # 提取匹配结果
        result = match.group()
        return result
    return None


class QichachaExcelParserPipeline():
    def __init__(self, path, dao: CompanyDao):
        self.df = pd.read_excel(path, skiprows=1,engine='openpyxl')
        self.dao = dao
        # print(self.df.columns)
        print(self.df.shape)

    def get_company_name(self, data):
        name = getattr(data, "企业名称", None)
        if isinstance(name, str):
            if name== "-":
                return None
            return name.strip()

    def get_company_short_name(self, full_name: str):
        return full_name.replace("股份有限公司", "").replace("有限公司", "")

    def insured_people_number_clean(self, text):
        if text is None:
            return None
        if isinstance(text, str):
            text = text.strip()
            if text == "-":
                return None
            try:
                text = int(text)
                return text
            except:
                # TODO record
                pass

    def common_text_clean(self, text):
        if text is None or text == "-":
            return None
        return text.strip()

    def get_anual_year(self, text):
        if text is None or isinstance(text, float):
            return None
        if text == "-":
            return None
        text = str(text).strip().replace("年报","")
        return int(text)


    def process_company(self, data):
        full_name = self.get_company_name(data)
        if full_name is None:
            return False
        registered_capital_value, registered_capital_unit, registered_capital_currency = get_registered_capital(
            getattr(data, "注册资本"))
        # TODO check data alreay exists?
        self.dao.merge_company(full_name=full_name,
                             short_name=self.get_company_short_name(full_name),
                             insured_people_number=self.insured_people_number_clean(getattr(data, "参保人数")),
                             business_scope=self.common_text_clean(getattr(data, "经营范围")),
                             registered_address=self.common_text_clean(getattr(data, "企业注册地址")),
                             english_name=self.common_text_clean(getattr(data, "英文名")),
                             representative=self.common_text_clean(getattr(data, "法定代表人")),
                             registration_status=self.common_text_clean(getattr(data, "登记状态")),
                             registered_capital_string=self.common_text_clean(getattr(data, "注册资本")),
                             registered_capital_value=registered_capital_value,
                             registered_capital_unit=registered_capital_unit,
                             registered_capital_currency=registered_capital_currency,
                             founded_date=founded_time_clean(getattr(data, "成立日期")),
                             unified_social_credit_identifier=self.common_text_clean(getattr(data, "统一社会信用代码")),
                             phone=self.common_text_clean(getattr(data, "电话")),
                             more_phone=self.common_text_clean(getattr(data, "更多电话")),
                             email=self.common_text_clean(getattr(data, "邮箱")),
                             more_email=self.common_text_clean(getattr(data, "更多邮箱")),
                             province_name=self.common_text_clean(getattr(data, "所属省份")),
                             city_name=self.common_text_clean(getattr(data, "所属城市")),
                             district_name=self.common_text_clean(getattr(data, "所属区县")),
                             # mailing_address_point=None,
                             # type_name=self.common_text_clean(getattr(data, "企业(机构)类型")),
                             type_name=self.common_text_clean(data[20]),

                             taxpayer_registeration_number=self.common_text_clean(getattr(data, "纳税人识别号")),
                             registration_number=self.common_text_clean(getattr(data, "注册号")),
                             institution_code=self.common_text_clean(getattr(data, "组织机构代码")),
                             insured_number_annal =self.get_anual_year(getattr(data, "参保人数所属年报")),
                             scale_code = get_company_scale(getattr(data, "企业规模")),
                             former_name = self.common_text_clean(getattr(data, "曾用名")),
                             official_website = self.common_text_clean(getattr(data, "官网网址")),
                             profile = self.common_text_clean(getattr(data, "企业简介")),
                             gb_industry_name = self.common_text_clean(getattr(data, "国标行业门类")),
                             gb_major_industry_name = self.common_text_clean(getattr(data, "国标行业大类")),
                             gb_medium_industry_name =self.common_text_clean(getattr(data, "国标行业中类")),
                             gb_small_industry_name =self.common_text_clean(getattr(data, "国标行业小类")),
                             approval_date =founded_time_clean(getattr(data, "核准日期")),
                             operating_period = self.common_text_clean(getattr(data, "营业期限")),
                             mailing_address = self.common_text_clean(getattr(data, "通信地址")),
                             # registered_address_point = None,
                             qichacha_category_name = self.common_text_clean(getattr(data, "企查查行业门类")),
                             qichacha_major_category_name = self.common_text_clean(getattr(data, "企查查行业大类")),
                             qichacha_medium_category_name = self.common_text_clean(getattr(data, "企查查行业中类")),
                             qichacha_small_category_name = self.common_text_clean(getattr(data, "企查查行业小类")),
                             data_source_id = 1,
                             nick_name = None,
                             country_name = None,


                             )

    def run(self):
        for data in tqdm.tqdm(self.df.itertuples()):
            self.process_company(data)
