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


class RoomMovie(models.Model):
    """
    部屋動画
    """
    id = models.AutoField(_('id'), db_column='id', primary_key=True)
    building_id = models.IntegerField(_('building_id'), db_column='building_id', db_index=True, default=0)
    room_id = models.IntegerField(_('room_id'), db_column='room_id', db_index=True, default=0)
    file_name = models.CharField(_('file_name'), db_column='file_name', max_length=255)
    cache_name = models.CharField(_('cache_name'), db_column='cache_name', max_length=255)
    movie_type_id = models.IntegerField(_('movie_type_id'), db_column='movie_type_id', db_index=True, default=0)
    is_publish_web = models.BooleanField(_('is_publish_web'), db_column='is_publish_web', db_index=True, default=True)
    is_publish_vacancy = models.BooleanField(_('is_publish_vacancy'), db_column='is_publish_vacancy', db_index=True, default=True)
    comment = models.CharField(_('comment'), db_column='comment', max_length=50, null=True, blank=True)
    note = models.CharField(_('note'), db_column='note', max_length=255, null=True, blank=True)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    created_at = models.DateTimeField(_('created_at'), db_column='created_at', default=timezone.now)
    created_user_id = models.IntegerField(_('created_user_id'), db_column='created_user_id', db_index=True, default=0)
    updated_at = models.DateTimeField(_('updated_at'), db_column='updated_at', default=timezone.now)
    updated_user_id = models.IntegerField(_('updated_user_id'), db_column='updated_user_id', db_index=True, default=0)
    is_deleted = models.BooleanField(_('is_deleted'), db_column='is_deleted', db_index=True, default=False)

    def __str__(self):
        return self.file_name

    class Meta:
        db_table = 'room_movie'
        ordering = ['building_id', 'room_id', 'priority', 'id']
        verbose_name = _('room_movie')
        verbose_name_plural = _('room_movies')
