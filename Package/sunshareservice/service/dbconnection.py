# -*- coding: utf-8 -*-
# author:shihua
# designer:shihua
# coder:shihua
# 这是一个数据库连接脚本，主要功能数据库连接管理，主要技术sqlachemy
"""
模块介绍
-------

这是一个数据库连接脚本，主要功能数据库连接管理，主要技术sqlachemy

    功能：             

        （1）数据库连接

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from sunshareservice.service import cons as ct
from sqlalchemy import create_engine



####### 数据库连接管理 ###########################################################
### 功能：                                                                    ###
### （1）数据库连接                                                            ###
#################################################################################



####### 数据库连接管理 ##################################################################################
########################################################################################################



db_engine = create_engine("{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}".format(
                            dialect = ct.SERVICE_DIALECT,
                            driver = ct.SERVICE_DRIVER,
                            username = ct.SERVICE_USERNAME,
                            password = ct.SERVICE_PASSWORD,
                            host = ct.SERVICE_HOST,
                            port = ct.SERVICE_PORT,
                            database = ct.SERVICE_DATABASE))
print('database engine create well done!')



#######################################################################################################
#######################################################################################################


