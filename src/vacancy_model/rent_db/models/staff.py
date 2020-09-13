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


class Staff(models.Model):
    """
    スタッフ
    """
    id = models.AutoField(_('id'), db_column='id', primary_key=True)
    department_id = models.IntegerField(_('department_id'), db_column='department_id', db_index=True, default=0)
    first_name = models.CharField(_('first_name'), db_column='first_name', max_length=50, null=True, blank=True)
    last_name = models.CharField(_('last_name'), db_column='last_name', max_length=50, null=True, blank=True)
    post_name = models.CharField(_('post_name'), db_column='post_name', max_length=50, null=True, blank=True)
    vacancy_name = models.CharField(_('vacancy_name'), db_column='vacancy_name', max_length=100, null=True, blank=True)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    tel1 = models.CharField(_('tel1'), db_column='tel1', max_length=20, null=True, blank=True)
    tel2 = models.CharField(_('tel2'), db_column='tel2', max_length=20, null=True, blank=True)
    mail = models.EmailField(_('mail'), db_column='mail', null=True, blank=True)
    is_pm_staff = models.BooleanField(_('is_pm_staff'), db_column='is_pm_staff', db_index=True, default=True)
    is_publish_vacancy = models.BooleanField(_('is_publish_vacancy'), db_column='is_publish_vacancy', db_index=True, default=True)
    created_at = models.DateTimeField(_('created_at'), db_column='created_at', default=timezone.now)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)
    is_deleted = models.BooleanField(_('is_deleted'), db_column='is_deleted', db_index=True, default=False)

    def __str__(self):
        return self.last_name + ' ' + self.first_name

    class Meta:
        db_table = 'staff'
        ordering = ['priority', 'id']
        verbose_name = _('staff')
        verbose_name_plural = _('staffs')
