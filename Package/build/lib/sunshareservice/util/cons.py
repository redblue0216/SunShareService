# -*- coding: utf-8 -*-
# author:shihua
# designer:shihua
# coder:shihua
# 这是一个元数据信息库参数管理脚本，主要用于存储相应参数
"""
模块介绍
-------

这是一个元数据信息库参数管理脚本，主要用于存储相应参数

    功能：             

        （1）元数据信息库参数管理

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import yaml
import sunshareservice as ds



####### 元数据信息库参数管理 #####################################################
### 功能：                                                                    ###
### （1）元数据信息库参数管理                                                   ###
#################################################################################



####### 元数据信息库参数管理 #############################################################################
########################################################################################################



### sunshareservice_sunshareservice_metadb_PATH：sunshareservice数据库路径
### 从配置文件sunshareservice_config.yaml中获取
# sunshareservice_sunshareservice_metadb_PATH = r'D:\Workspace\JiYuan\sunshareservice\Demo\sunshareservice.db'
sunshareservice_package_path = ds.__file__.replace('__init__.py','')
sunshareservice_config_file = open('{}sunshareservice_config.yaml'.format(sunshareservice_package_path),encoding='UTF-8')
sunshareservice_config_yaml = yaml.load(sunshareservice_config_file,Loader=yaml.FullLoader)
sunshareservice_metadb_path = sunshareservice_config_yaml['sunshareservice_metadb_path']
SUNSHARESERVICE_METADB_PATH = r'{}'.format(sunshareservice_metadb_path)



########################################################################################################
########################################################################################################


