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


class BuildingFacility(models.Model):
    """
    建物周辺施設
    """
    id = models.AutoField(_('id'), db_column='id', primary_key=True)
    building_id = models.IntegerField(_('building_id'), db_column='building_id', db_index=True, default=0)
    facility_id = models.IntegerField(_('facility_id'), db_column='facility_id', db_index=True, default=0)
    facility_name = models.CharField(_('facility_name'), db_column='facility_name', max_length=100, null=True, blank=True)
    distance = models.IntegerField(_('distance'), db_column='distance', default=0)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    building_picture_id = models.IntegerField(_('building_picture_id'), db_column='building_picture_id', default=0)
    created_at = models.DateTimeField(_('created_at'), db_column='created_at', default=timezone.now)
    created_user_id = models.IntegerField(_('created_user_id'), db_column='created_user_id', db_index=True, default=0)
    updated_at = models.DateTimeField(_('updated_at'), db_column='updated_at', default=timezone.now)
    updated_user_id = models.IntegerField(_('updated_user_id'), db_column='updated_user_id', db_index=True, default=0)
    is_deleted = models.BooleanField(_('is_deleted'), db_column='is_deleted', db_index=True, default=False)

    def __str__(self):
        return self.facility_name

    class Meta:
        db_table = 'building_facility'
        ordering = ['building_id', 'priority', 'id']
        verbose_name = _('building_facility')
        verbose_name_plural = _('building_facilities')
