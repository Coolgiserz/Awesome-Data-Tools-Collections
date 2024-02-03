# @Author: weirdgiser
# @Time: 2024/2/3
# @Function:
import os
from glob import glob
from pipelines.qichacha import QichachaBatchQueryExcelParserPipeline
from config import ProjectConfigParserProxy
from dao import CompanyDao
config_proxy = ProjectConfigParserProxy(conf_path="project.conf")
connect_str = config_proxy.get_database_connect_string()
company_dao = CompanyDao(connect_str=connect_str)

def get_source_data_path(dirname, suffix=".xlsx"):
    return glob(os.path.join(dirname, f"*{suffix}"))
def process_file(file):
    print(f"Processing: {file}")
    qcc_parser = QichachaBatchQueryExcelParserPipeline(file, dao=company_dao)
    qcc_parser.run()

if __name__ == "__main__":
    data_source_paths = get_source_data_path(config_proxy.get_data_batch_query_dirname())
    print(len(data_source_paths))
    for data_path in data_source_paths:
        process_file(data_path)