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


class RoomStatusLog(models.Model):
    """
    部屋状況変更ログ
    """
    id = models.AutoField(_('id'), db_column='id', primary_key=True)
    building_id = models.IntegerField(_('building_id'), db_column='building_id', db_index=True, default=0)
    room_id = models.IntegerField(_('room_id'), db_column='room_id', db_index=True, default=0)
    room_status_id = models.IntegerField(_('room_status_id'), db_column='room_status_id', db_index=True, default=0)
    last_room_status_id = models.IntegerField(_('last_room_status_id'), db_column='last_room_status_id', db_index=True, default=0)
    created_at = models.DateTimeField(_('created_at'), db_column='created_at', db_index=True, default=timezone.now)
    created_user_id = models.IntegerField(_('created_user_id'), db_column='created_user_id', db_index=True, default=0)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'room_status_log'
        ordering = ['building_id', 'room_id', 'created_at', 'id']
        verbose_name = _('room_status_log')
        verbose_name_plural = _('room_status_logs')
