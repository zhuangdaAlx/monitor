# -*- coding: utf-8 -*-
"""
用于正式环境的全局配置
"""
from settings import APP_ID


# ===============================================================================
# 数据库设置, 正式环境数据库设置
# ===============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 默认用mysql
        'NAME': 'zhuangd_pro',                        # 数据库名 (默认与APP_ID相同)
        'USER': 'zhuangd',                            # 你的数据库user
        'PASSWORD': 'zhuangd_pro@2018',                        # 你的数据库password
        'HOST': '172.50.21.22',                   		   # 数据库HOST
        'PORT': '3306',                        # 默认3306
    },
}