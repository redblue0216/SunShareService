# -*- coding: utf-8 -*-
# author:shihua
# designer:shihua
# coder:shihua
# 这是一个信息工具类，主要功能创建元数据库，主要技术sqlite3
"""
模块介绍
-------

这是一个信息工具类，主要功能创建元数据信息库，主要技术sqlite3

    功能：             

        （1）元数据信息库创建

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from sunshareservice.util import cons as ct
import sqlite3
import hashlib
import sunshareservice as ds



####### 信息工具类 ###############################################################
### 功能：                                                                    ###
### （1）元数据信息库创建                                                       ###
#################################################################################



####### 信息工具类 ######################################################################################
########################################################################################################



### 创建sunshareservice元数据信息库
def create_sunshareservice_metadb(sunshareservice_metadb_path = ct.SUNSHARESERVICE_METADB_PATH,*args,**kwargs):
    '''
    函数功能：

        定义一个创建sunshareservice元数据信息库的函数

    参数：
        sunshareservice_metadb_path (str): sunshareservice元数据信息库路径

    返回：
        result (str): 创建成功结果信息
    '''

    ### 获取包安装后的路径site-packages/sunshareservice/
    sunshareservice_metadb_path_in_pkg = ds.__file__.replace('__init__.py','') 
    ### 开始创建数据库
    sunshareservice_metadb_connection = sqlite3.connect(sunshareservice_metadb_path_in_pkg + sunshareservice_metadb_path)
    sunshareservice_metadb_cursor = sunshareservice_metadb_connection.cursor()
    sunshareservice_metadb_cursor.execute('''CREATE TABLE IF NOT EXISTS SunShareServiceInfo(
        user TEXT NOT NULL,
        password TEXT NOT NULL,
        token TEXT NOT NULL,
        trafic TEXT NOT NULL 
    )
    ''')
    sunshareservice_metadb_cursor.close()
    sunshareservice_metadb_connection.close()
    result = 'SunShareService metadb create well done!====>>{}'.format(sunshareservice_metadb_path)
    print(result)

    return result



### 获取sunshareservice元数据信息库操作游标
def get_sunshareservice_metadb_connection(sunshareservice_metadb_path = ct.SUNSHARESERVICE_METADB_PATH,*args,**kwargs):
    '''
    函数功能：

        定义一个获取sunshareservice元数据信息库操作游标的函数

    参数：
        sunshareservice_metadb_path (str): sunshareservice元数据信息库路径

    返回：
        sunshareservice_metadb_connection (obj): sunshareservice元数据信息库连接
    '''


    sunshareservice_metadb_connection = sqlite3.connect(sunshareservice_metadb_path)

    return sunshareservice_metadb_connection



### 加密密码
def encrypt_password(password,salt='sunshareservice',algorithm='md5'):
    '''
    函数功能：

        定义一个加密密码的函数，默认使用md5加密算法

    参数：
        password (str): 密码
        salt (str): 密码加盐，默认为sunshareservice
        algorithm (str): 加密算法

    返回：
        encrypted_pwd (str): 加密后的密码
    '''

    SALT = salt
    md5_salt = hashlib.md5((password + SALT).encode('utf-8'))
    encrypted_pwd = md5_salt.hexdigest()

    return encrypted_pwd



#############################################################################################################
#############################################################################################################


