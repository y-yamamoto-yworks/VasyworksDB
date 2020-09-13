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


class LayoutType(models.Model):
    """
    間取種別
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)
    name = models.CharField(_('name'), db_column='name', max_length=50)
    room_count = models.IntegerField(_('room_count'), db_column='room_count', db_index=True, default=0)
    category_id = models.IntegerField(_('category_id'), db_column='category_id', db_index=True, default=0)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'layout_type'
        ordering = ['priority', 'id']
        verbose_name = _('layout_type')
        verbose_name_plural = _('layout_types')

