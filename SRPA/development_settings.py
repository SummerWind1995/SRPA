#!/usr/bin/env python3
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2017-10-01 15:15
# Last modified: 2017-10-14 13:56
# Filename: development_settings.py
# Description:

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v_&4b1seyjht1+vl6c08)&7is*srv_0lqg4t^%0f71o19r5%yu'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'SRPA',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '192.168.3.95',
        'PORT': '3307',
        'OPTIONS': {
            'sql_mode': 'STRICT_TRANS_TABLES',
        }
    }
}
