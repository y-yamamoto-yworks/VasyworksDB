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


class Company(models.Model):
    """
    会社
    """
    id = models.AutoField(_('id'), db_column='id', primary_key=True)
    api_key = models.CharField(_('api_key'), db_column='api_key', max_length=50, null=True, blank=True)
    internal_api_key = models.CharField(_('internal_api_key'), db_column='internal_api_key', max_length=50, null=True, blank=True)
    company_name = models.CharField(_('company_name'), db_column='company_name', max_length=100, db_index=True, null=True, blank=True)
    company_kana = models.CharField(_('company_kana'), db_column='company_kana', max_length=100, db_index=True, null=True, blank=True)
    shop_name = models.CharField(_('shop_name'), db_column='shop_name', max_length=100, null=True, blank=True)
    postal_code = models.CharField(_('postal_code'), db_column='postal_code', max_length=10, null=True, blank=True)
    address = models.CharField(_('address'), db_column='address', max_length=255, null=True, blank=True)
    tel = models.CharField(_('tel'), db_column='tel', max_length=20, null=True, blank=True)
    fax = models.CharField(_('fax'), db_column='fax', max_length=20, null=True, blank=True)
    mail = models.EmailField(_('mail'), db_column='mail', null=True, blank=True)
    agency_no = models.CharField(_('agency_no'), db_column='agency_no', max_length=50, null=True, blank=True)
    pm_no = models.CharField(_('pm_no'), db_column='pm_no', max_length=50, null=True, blank=True)
    water_mark = models.CharField(_('water_mark'), db_column='water_mark', max_length=50, null=True, blank=True)
    is_default = models.BooleanField(_('is_default'), db_column='is_default', default=True)

    def __str__(self):
        return self.company_name

    class Meta:
        db_table = 'company'
        ordering = ['company_kana', 'id']
        verbose_name = _('company')
        verbose_name_plural = _('companies')
