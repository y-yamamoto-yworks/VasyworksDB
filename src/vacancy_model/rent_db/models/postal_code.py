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


class PostalCode(models.Model):
    """
    郵便番号
    """
    id = models.AutoField(_('id'), db_column='id', primary_key=True)
    postal_code = models.CharField(_('postal_code'), db_column='postal_code', db_index=True, max_length=20)
    pref_id = models.IntegerField(_('pref_id'), db_column='pref_id', db_index=True, default=0)
    city_id = models.IntegerField(_('city_id'), db_column='city_id', db_index=True, default=0)
    pref_name = models.CharField(_('pref_name'), db_column='pref_name', max_length=50, null=True, blank=True)
    city_name = models.CharField(_('city_name'), db_column='city_name', max_length=50, null=True, blank=True)
    town_name = models.CharField(_('town_name'), db_column='town_name', max_length=100, null=True, blank=True)
    pref_kana = models.CharField(_('pref_kana'), db_column='pref_kana', max_length=50, db_index=True, null=True, blank=True)
    city_kana = models.CharField(_('city_kana'), db_column='city_kana', max_length=50, db_index=True, null=True, blank=True)
    town_kana = models.CharField(_('town_kana'), db_column='town_kana', max_length=100, db_index=True, null=True, blank=True)

    def __str__(self):
        return self.postal_code

    class Meta:
        db_table = 'postal_code'
        ordering = ['postal_code', 'id']
        verbose_name = _('postal_code')
        verbose_name_plural = _('postal_codes')

