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


class CityArea(models.Model):
    """
    市区町村エリア
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)
    city_id = models.IntegerField(_('city_id'), db_column='city_id', db_index=True, default=0)
    area_id = models.IntegerField(_('area_id'), db_column='area_id', default=0)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    class Meta:
        db_table = 'city_area'
        ordering = ['city_id', 'area_id', 'id']
        verbose_name = _('city_area')
        verbose_name_plural = _('city_areas')

