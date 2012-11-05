# -*- coding: utf-8 -*-
VERSION = (1, 0, 0, 'beta')

__version__ = ".".join(map(str, VERSION[0:3])) + "".join(VERSION[3:])
__author__ = 'Kuba Janoszek'

try:
    from django_settings.models import Setting
except:
    pass

def get_setting(name, default=''):
    return Setting.objects.get_value(name,default=default)
        
def set_setting(name, value):
    Setting.objects.set_value(name, models.Integer, value)