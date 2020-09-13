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


class TransferStation(models.Model):
    """
    乗換駅
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)
    station_id = models.IntegerField(_('station_id'), db_column='station_id', db_index=True, default=0)
    transfer_station_id = models.IntegerField(_('transfer_station_id'), db_column='transfer_station_id', default=0)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'transfer_station'
        ordering = ['station_id', 'id']
        verbose_name = _('transfer_station')
        verbose_name_plural = _('transfer_stations')

