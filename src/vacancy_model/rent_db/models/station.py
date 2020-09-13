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


class Station(models.Model):
    """
    駅
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)
    railway_id = models.IntegerField(_('railway_id'), db_column='railway_id', db_index=True, default=0)
    name = models.CharField(_('name'), db_column='name', max_length=50)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    is_trading = models.BooleanField(_('is_trading'), db_column='is_trading', db_index=True, default=False)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'station'
        ordering = ['priority', 'id']
        verbose_name = _('station')
        verbose_name_plural = _('stations')

