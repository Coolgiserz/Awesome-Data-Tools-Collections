# @Author: weirdgiser
# @Time: 2024/1/28
# @Function:
from common.config import ConfigParserProxy
from urllib.parse import quote_plus


class ProjectConfigParserProxy(ConfigParserProxy):
    pgsql_section = "pgsql"
    data_section = "data"
    def get_database_connect_string(self, dbname=None):
        user = self.handler.get(self.pgsql_section, "USER")
        pwd = self.handler.get(self.pgsql_section, "PWD")
        host = self.handler.get(self.pgsql_section, "HOST")
        port = self.handler.get(self.pgsql_section, "PORT")
        if dbname is None:
            dbname = self.handler.get(self.pgsql_section, "DBNAME")
        return f"postgresql://{user}:{quote_plus(pwd)}@{host}:{port}/{dbname}"

    def get_data_dirname(self):
        return self.handler.get(self.data_section, "DIRNAME")