"""
System Name: Vasyworks
Project Name: vacancy_model
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
import os
import datetime
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class City(models.Model):
    """
    市区町村
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)
    name = models.CharField(_('name'), db_column='name', max_length=50)
    pref_id = models.IntegerField(_('pref_id'), db_column='pref_id', db_index=True, default=0)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    lat = models.FloatField(_('lat'), db_column='lat', db_index=True, default=0)
    lng = models.FloatField(_('lng'), db_column='lng', db_index=True, default=0)
    is_trading_area = models.BooleanField(_('is_trading_area'), db_column='is_trading_area', db_index=True, default=False)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'city'
        ordering = ['pref_id', 'priority', 'id']
        verbose_name = _('city')
        verbose_name_plural = _('cities')

