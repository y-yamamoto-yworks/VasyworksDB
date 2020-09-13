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


class VacancyTheme(models.Model):
    """
    空室情報テーマ
    """
    id = models.AutoField(_('id'), db_column='id', primary_key=True)
    name = models.CharField(_('name'), db_column='name', max_length=50)
    title = models.CharField(_('title'), db_column='title', max_length=100, null=True, blank=True)
    description = models.CharField(_('description'), db_column='description', max_length=255, null=True, blank=True)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    room_auth_level_id = models.IntegerField(_('room_auth_level_id'), db_column='room_auth_level_id', db_index=True, default=0)
    is_publish = models.BooleanField(_('is_publish'), db_column='is_publish', default=False)
    created_at = models.DateTimeField(_('created_at'), db_column='created_at', default=timezone.now)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'vacancy_theme'
        ordering = ['priority', 'id']
        verbose_name = _('vacancy_theme')
        verbose_name_plural = _('vacancy_themes')
