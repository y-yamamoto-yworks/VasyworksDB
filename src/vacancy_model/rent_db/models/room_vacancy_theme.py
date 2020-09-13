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


class RoomVacancyTheme(models.Model):
    """
    部屋空室情報テーマ
    """
    id = models.AutoField(_('id'), db_column='id', primary_key=True)
    building_id = models.IntegerField(_('building_id'), db_column='building_id', db_index=True, default=0)
    room_id = models.IntegerField(_('room_id'), db_column='room_id', db_index=True, default=0)
    vacancy_theme_id = models.IntegerField(_('vacancy_theme_id'), db_column='vacancy_theme_id', db_index=True, default=0)
    created_at = models.DateTimeField(_('created_at'), db_column='created_at', default=timezone.now)
    created_user_id = models.IntegerField(_('created_user_id'), db_column='created_user_id', db_index=True, default=0)
    updated_at = models.DateTimeField(_('updated_at'), db_column='updated_at', default=timezone.now)
    updated_user_id = models.IntegerField(_('updated_user_id'), db_column='updated_user_id', db_index=True, default=0)
    is_deleted = models.BooleanField(_('is_deleted'), db_column='is_deleted', db_index=True, default=False)

    def __str__(self):
        return self.vacancy_theme_id

    class Meta:
        db_table = 'room_vacancy_theme'
        ordering = ['building_id', 'room_id', 'vacancy_theme_id', 'id']
        verbose_name = _('room_vacancy_theme')
        verbose_name_plural = _('room_vacancy_themes')
