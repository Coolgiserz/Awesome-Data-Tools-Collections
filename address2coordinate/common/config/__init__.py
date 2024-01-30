# @Author: weirdgiser
# @Time: 2024/1/28
# @Function:
from configparser import ConfigParser
class ConfigParserProxy():
    def __init__(self, conf_path):
        super().__init__()
        self.handler = ConfigParser()
        self.handler.read(conf_path)

    def get_sections(self):
        return self.handler.sections()

    def get_section(self, section, option):
        return self.handler.get(section, option)
