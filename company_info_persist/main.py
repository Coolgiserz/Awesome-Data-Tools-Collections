import os.path
from glob import glob
from config import ProjectConfigParserProxy
from dao import CompanyDao
from pipelines.qichacha import QichachaExcelParserPipeline
import multiprocessing
config_proxy = ProjectConfigParserProxy(conf_path="project.conf")
print(config_proxy.get_sections())
connect_str = config_proxy.get_database_connect_string()
print(f"connect_str: {connect_str}")
company_dao = CompanyDao(connect_str=connect_str)


def get_source_data_path(dirname, suffix=".xlsx"):
    return glob(os.path.join(dirname, f"*{suffix}"))

def process_file(file):
    print(f"Processing: {file}")
    qcc_parser = QichachaExcelParserPipeline(file, dao=company_dao)
    qcc_parser.run()

def main():
    data_source_paths = get_source_data_path(config_proxy.get_data_dirname())
    print(len(data_source_paths))
    pool = multiprocessing.Pool(processes=4)
    pool.map(process_file, data_source_paths)
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
