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


class BuildingGarage(models.Model):
    """
    建物駐車場
    """
    id = models.AutoField(_('id'), db_column='id', primary_key=True)
    building_id = models.IntegerField(_('building_id'), db_column='building_id', db_index=True, default=0)
    garage_name = models.CharField(_('garage_name'), db_column='garage_name', max_length=100)
    garage_fee = models.IntegerField(_('garage_fee'), db_column='garage_fee', default=0)
    garage_fee_tax_type_id = models.IntegerField(_('garage_fee_tax_type_id'), db_column='garage_fee_tax_type_id', default=0)
    garage_charge = models.IntegerField(_('garage_charge'), db_column='garage_charge', default=0)
    garage_charge_tax_type_id = models.IntegerField(_('garage_charge_tax_type_id'), db_column='garage_charge_tax_type_id', default=0)
    garage_deposit = models.IntegerField(_('garage_deposit'), db_column='garage_deposit', default=0)
    garage_deposit_tax_type_id = models.IntegerField(_('garage_deposit_tax_type_id'), db_column='garage_deposit_tax_type_id', default=0)
    certification_fee = models.IntegerField(_('certification_fee'), db_column='certification_fee', default=0)
    certification_fee_tax_type_id = models.IntegerField(_('certification_fee_tax_type_id'), db_column='certification_fee_tax_type_id', default=0)
    initial_cost_name1 = models.CharField(_('initial_cost_name1'), db_column='initial_cost_name1', max_length=100, null=True, blank=True)
    initial_cost1 = models.IntegerField(_('initial_cost1'), db_column='initial_cost1', default=0)
    initial_cost_tax_type_id1 = models.IntegerField(_('initial_cost_tax_type_id1'), db_column='initial_cost_tax_type_id1', default=0)
    initial_cost_name2 = models.CharField(_('initial_cost_name2'), db_column='initial_cost_name2', max_length=100, null=True, blank=True)
    initial_cost2 = models.IntegerField(_('initial_cost2'), db_column='initial_cost2', default=0)
    initial_cost_tax_type_id2 = models.IntegerField(_('initial_cost_tax_type_id2'), db_column='initial_cost_tax_type_id2', default=0)
    initial_cost_name3 = models.CharField(_('initial_cost_name3'), db_column='initial_cost_name3', max_length=100, null=True, blank=True)
    initial_cost3 = models.IntegerField(_('initial_cost3'), db_column='initial_cost3', default=0)
    initial_cost_tax_type_id3 = models.IntegerField(_('initial_cost_tax_type_id3'), db_column='initial_cost_tax_type_id3', default=0)
    garage_status_id = models.IntegerField(_('garage_status_id'), db_column='garage_status_id', db_index=True, default=0)
    allow_no_room = models.BooleanField(_('allow_no_room'), db_column='allow_no_room', db_index=True, default=False)
    width = models.DecimalField(_('width'), db_column='width', default=0, max_digits=12, decimal_places=2)
    length = models.DecimalField(_('length'), db_column='length', default=0, max_digits=12, decimal_places=2)
    height = models.DecimalField(_('height'), db_column='height', default=0, max_digits=12, decimal_places=2)
    comment = models.CharField(_('comment'), db_column='comment', max_length=100, null=True, blank=True)
    note = models.CharField(_('note'), db_column='note', max_length=255, null=True, blank=True)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    created_at = models.DateTimeField(_('created_at'), db_column='created_at', default=timezone.now)
    created_user_id = models.IntegerField(_('created_user_id'), db_column='created_user_id', db_index=True, default=0)
    updated_at = models.DateTimeField(_('updated_at'), db_column='updated_at', default=timezone.now)
    updated_user_id = models.IntegerField(_('updated_user_id'), db_column='updated_user_id', db_index=True, default=0)
    is_deleted = models.BooleanField(_('is_deleted'), db_column='is_deleted', db_index=True, default=False)

    def __str__(self):
        return self.garage_name

    class Meta:
        db_table = 'building_garage'
        ordering = ['building_id', 'priority', 'id']
        verbose_name = _('building_garage')
        verbose_name_plural = _('building_garages')
