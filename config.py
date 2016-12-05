#coding=utf-8
import ConfigParser
import os
import codecs


class ConfigIni(object):
    """
    配置类
    """
    config_path = os.getcwd() + '\config.ini'
    # config_path = os.path.abspath("config.ini")
    # config_path ="F:\\EWT_InterfaceTest\\config.ini"
    if not os.path.isfile(config_path):
        raise Exception,"This is not config Learn_BeautifulSoup."

    config = ConfigParser.ConfigParser()
    config.readfp(codecs.open(config_path,'r',"utf-8"))

    @classmethod
    def get_Cid(cls):
        """
        获取院校id
        """
        return cls.config.get("DEFAULT","cid")

    @classmethod
    def get_Gid(cls):
        """
        按科目查询获取组合id
        """
        return cls.config.get("DEFAULT","gid")

    @classmethod
    def get_dbinfo(cls):
        """
        获取数据库信息
        """
        return cls.config.get("DEFAULT", "dbinfo")

    @classmethod
    def get_QueryDict(cls):
        """
        获取数据库信息
        """
        return cls.config.get("Group", "QueryDict")



