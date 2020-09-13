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


class Owner(models.Model):
    """
    オーナー
    """
    id = models.AutoField(_('id'), db_column='id', primary_key=True)
    owner_name = models.CharField(_('owner_name'), db_column='owner_name', max_length=255, db_index=True)
    owner_kana = models.CharField(_('owner_kana'), db_column='owner_kana', max_length=255, db_index=True, null=True, blank=True)
    is_corporation = models.BooleanField(_('is_corporation'), db_column='is_corporation', default=False)
    corporation_owner_name = models.CharField(_('corporation_owner_name'), db_column='corporation_owner_name', max_length=255, db_index=True, null=True, blank=True)
    postal_code = models.CharField(_('postal_code'), db_column='postal_code', max_length=10, null=True, blank=True)
    address = models.CharField(_('address'), db_column='address', max_length=255, null=True, blank=True)
    tel1 = models.CharField(_('tel1'), db_column='tel1', max_length=20, null=True, blank=True)
    tel2 = models.CharField(_('tel2'), db_column='tel2', max_length=20, null=True, blank=True)
    fax = models.CharField(_('fax'), db_column='fax', max_length=20, null=True, blank=True)
    mail = models.EmailField(_('mail'), db_column='mail', null=True, blank=True)
    staff_id = models.IntegerField(_('staff_id'), db_column='staff_id', db_index=True, default=0)
    note = models.TextField(_('note'), db_column='note', max_length=2000, null=True, blank=True)
    created_at = models.DateTimeField(_('created_at'), db_column='created_at', default=timezone.now)
    created_user_id = models.IntegerField(_('created_user_id'), db_column='created_user_id', db_index=True, default=0)
    updated_at = models.DateTimeField(_('updated_at'), db_column='updated_at', default=timezone.now)
    updated_user_id = models.IntegerField(_('updated_user_id'), db_column='updated_user_id', db_index=True, default=0)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)
    is_deleted = models.BooleanField(_('is_deleted'), db_column='is_deleted', db_index=True, default=False)

    def __str__(self):
        return self.owner_name

    class Meta:
        db_table = 'owner'
        ordering = ['owner_kana', 'id']
        verbose_name = _('owner')
        verbose_name_plural = _('owners')
