import sys
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))
from pipelines.qichacha import get_registered_capital, founded_time_clean, get_currency_name,get_currency_code,get_company_scale

def test_get_currency_name():
    print(get_currency_name())

def test_get_currency_code():
    print(get_currency_code())

def test_get_registered_capital():
    print("注册资本解析")
    cases = ["41982.21033万元人民币","10,000,000 USD","5000万元人民币", "380,000 HKD", "1000万美元"]
    for case in cases:
        a,b,c = get_registered_capital(case)
        print(f"{case}: ", a, b, c)

def test_founded_time_clean():
    cases = ["-","2005-01-12", "2024-01-32", "2023-02-29", "2023-02-28", "1231123", "20230112", "2023-01-1", "2020-1-1"]
    for case in cases:
        print(f"{case}: ",founded_time_clean(case))

def test_get_company_scale():
    cases = ["XS(微型)", "-", "S(小型111)", "大型"]
    for case in cases:
        print(f"{case}: ",get_company_scale(case))
