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


class CityElementarySchool(models.Model):
    """
    市区町村小学校区
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)
    city_id = models.IntegerField(_('city_id'), db_column='city_id', db_index=True, default=0)
    school_id = models.IntegerField(_('school_id'), db_column='school_id', default=0)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    class Meta:
        db_table = 'city_elementary_school'
        ordering = ['city_id', 'school_id', 'id']
        verbose_name = _('city_elementary_school')
        verbose_name_plural = _('city_elementary_schools')

