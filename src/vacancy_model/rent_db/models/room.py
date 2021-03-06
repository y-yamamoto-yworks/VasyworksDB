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


class Room(models.Model):
    """
    部屋
    """
    id = models.AutoField(_('id'), db_column='id', primary_key=True)
    oid = models.CharField(_('oid'), db_column='oid', db_index=True, unique=True, max_length=50)
    building_id = models.IntegerField(_('building_id'), db_column='building_id', db_index=True, default=0)
    room_no = models.CharField(_('room_no'), db_column='room_no', max_length=20, db_index=True, null=True, blank=True)
    room_floor = models.IntegerField(_('room_floor'), db_column='room_floor', default=0)
    room_auth_level_id = models.IntegerField(_('room_auth_level_id'), db_column='room_auth_level_id', db_index=True, default=0)
    rental_type_id = models.IntegerField(_('rental_type_id'), db_column='rental_type_id', default=0)
    is_sublease = models.BooleanField(_('is_sublease'), db_column='is_sublease', db_index=True, default=False)
    is_condo_management = models.BooleanField(_('is_condo_management'), db_column='is_condo_management', db_index=True, default=False)
    condo_owner_id = models.IntegerField(_('condo_owner_id'), db_column='condo_owner_id', db_index=True, default=0)
    is_entrusted = models.BooleanField(_('is_entrusted'), db_column='is_entrusted', db_index=True, default=False)
    condo_trader_id = models.IntegerField(_('condo_trader_id'), db_column='condo_trader_id', db_index=True, default=0)
    room_status_id = models.IntegerField(_('room_status_id'), db_column='room_status_id', db_index=True, default=0)
    vacancy_status_id = models.IntegerField(_('vacancy_status_id'), db_column='vacancy_status_id', db_index=True, default=0)
    vacancy_status_note = models.TextField(_('vacancy_status_note'), db_column='vacancy_status_note', max_length=2000, null=True, blank=True)
    live_start_year = models.IntegerField(_('live_start_year'), db_column='live_start_year', default=0)
    live_start_month = models.IntegerField(_('live_start_month'), db_column='live_start_month', default=0)
    live_start_day_id = models.IntegerField(_('live_start_day_id'), db_column='live_start_day_id', default=0)
    live_start_note = models.CharField(_('live_start_note'), db_column='live_start_note', max_length=255, null=True, blank=True)
    cancel_scheduled_year = models.IntegerField(_('cancel_scheduled_year'), db_column='cancel_scheduled_year', default=0)
    cancel_scheduled_month = models.IntegerField(_('cancel_scheduled_month'), db_column='cancel_scheduled_month', default=0)
    cancel_scheduled_day_id = models.IntegerField(_('cancel_scheduled_day_id'), db_column='cancel_scheduled_day_id', default=0)
    cancel_scheduled_note = models.CharField(_('cancel_scheduled_note'), db_column='cancel_scheduled_note', max_length=255, null=True, blank=True)
    is_publish_vacancy = models.BooleanField(_('is_publish_vacancy'), db_column='is_publish_vacancy', db_index=True, default=True)
    vacancy_start_date = models.CharField(_('vacancy_start_date'), db_column='vacancy_start_date', max_length=10, db_index=True, null=True, blank=True)
    vacancy_end_date = models.CharField(_('vacancy_end_date'), db_column='vacancy_end_date', max_length=10, db_index=True, null=True, blank=True)
    vacancy_catch_copy = models.CharField(_('vacancy_catch_copy'), db_column='vacancy_catch_copy', max_length=100, null=True, blank=True)
    vacancy_appeal = models.CharField(_('vacancy_appeal'), db_column='vacancy_appeal', max_length=255, null=True, blank=True)
    vacancy_note = models.TextField(_('vacancy_note'), db_column='vacancy_note', max_length=2000, null=True, blank=True)
    pending_trader_name = models.CharField(_('pending_trader_name'), db_column='pending_trader_name', max_length=100, null=True, blank=True)
    pending_start_date = models.CharField(_('pending_start_date'), db_column='pending_start_date', max_length=10, null=True, blank=True)
    pending_end_date = models.CharField(_('pending_end_date'), db_column='pending_end_date', max_length=10, null=True, blank=True)
    pending_note = models.CharField(_('pending_note'), db_column='pending_note', max_length=255, null=True, blank=True)
    is_publish_web = models.BooleanField(_('is_publish_web'), db_column='is_publish_web', db_index=True, default=True)
    web_catch_copy = models.CharField(_('web_catch_copy'), db_column='web_catch_copy', max_length=100, null=True, blank=True)
    web_appeal = models.CharField(_('web_appeal'), db_column='web_appeal', max_length=255, null=True, blank=True)
    web_note = models.TextField(_('web_note'), db_column='web_note', max_length=2000, null=True, blank=True)
    layout_type_id = models.IntegerField(_('layout_type_id'), db_column='layout_type_id', db_index=True, default=0)
    western_style_room1 = models.DecimalField(_('western_style_room1'), db_column='western_style_room1', default=0, max_digits=5, decimal_places=2)
    western_style_room2 = models.DecimalField(_('western_style_room2'), db_column='western_style_room2', default=0, max_digits=5, decimal_places=2)
    western_style_room3 = models.DecimalField(_('western_style_room3'), db_column='western_style_room3', default=0, max_digits=5, decimal_places=2)
    western_style_room4 = models.DecimalField(_('western_style_room4'), db_column='western_style_room4', default=0, max_digits=5, decimal_places=2)
    western_style_room5 = models.DecimalField(_('western_style_room5'), db_column='western_style_room5', default=0, max_digits=5, decimal_places=2)
    western_style_room6 = models.DecimalField(_('western_style_room6'), db_column='western_style_room6', default=0, max_digits=5, decimal_places=2)
    western_style_room7 = models.DecimalField(_('western_style_room7'), db_column='western_style_room7', default=0, max_digits=5, decimal_places=2)
    western_style_room8 = models.DecimalField(_('western_style_room8'), db_column='western_style_room8', default=0, max_digits=5, decimal_places=2)
    western_style_room9 = models.DecimalField(_('western_style_room9'), db_column='western_style_room9', default=0, max_digits=5, decimal_places=2)
    western_style_room10 = models.DecimalField(_('western_style_room10'), db_column='western_style_room10', default=0, max_digits=5, decimal_places=2)
    japanese_style_room1 = models.DecimalField(_('japanese_style_room1'), db_column='japanese_style_room1', default=0, max_digits=5, decimal_places=2)
    japanese_style_room2 = models.DecimalField(_('japanese_style_room2'), db_column='japanese_style_room2', default=0, max_digits=5, decimal_places=2)
    japanese_style_room3 = models.DecimalField(_('japanese_style_room3'), db_column='japanese_style_room3', default=0, max_digits=5, decimal_places=2)
    japanese_style_room4 = models.DecimalField(_('japanese_style_room4'), db_column='japanese_style_room4', default=0, max_digits=5, decimal_places=2)
    japanese_style_room5 = models.DecimalField(_('japanese_style_room5'), db_column='japanese_style_room5', default=0, max_digits=5, decimal_places=2)
    japanese_style_room6 = models.DecimalField(_('japanese_style_room6'), db_column='japanese_style_room6', default=0, max_digits=5, decimal_places=2)
    japanese_style_room7 = models.DecimalField(_('japanese_style_room7'), db_column='japanese_style_room7', default=0, max_digits=5, decimal_places=2)
    japanese_style_room8 = models.DecimalField(_('japanese_style_room8'), db_column='japanese_style_room8', default=0, max_digits=5, decimal_places=2)
    japanese_style_room9 = models.DecimalField(_('japanese_style_room9'), db_column='japanese_style_room9', default=0, max_digits=5, decimal_places=2)
    japanese_style_room10 = models.DecimalField(_('japanese_style_room10'), db_column='japanese_style_room10', default=0, max_digits=5, decimal_places=2)
    kitchen_type_id1 = models.IntegerField(_('kitchen_type_id1'), db_column='kitchen_type_id1', default=0)
    kitchen1 = models.DecimalField(_('kitchen1'), db_column='kitchen1', default=0, max_digits=5, decimal_places=2)
    kitchen_type_id2 = models.IntegerField(_('kitchen_type_id2'), db_column='kitchen_type_id2', default=0)
    kitchen2 = models.DecimalField(_('kitchen2'), db_column='kitchen2', default=0, max_digits=5, decimal_places=2)
    kitchen_type_id3 = models.IntegerField(_('kitchen_type_id3'), db_column='kitchen_type_id3', default=0)
    kitchen3 = models.DecimalField(_('kitchen3'), db_column='kitchen3', default=0, max_digits=5, decimal_places=2)
    store_room1 = models.DecimalField(_('store_room1'), db_column='store_room1', default=0, max_digits=5, decimal_places=2)
    store_room2 = models.DecimalField(_('store_room2'), db_column='store_room2', default=0, max_digits=5, decimal_places=2)
    store_room3 = models.DecimalField(_('store_room3'), db_column='store_room3', default=0, max_digits=5, decimal_places=2)
    loft1 = models.DecimalField(_('loft1'), db_column='loft1', default=0, max_digits=5, decimal_places=2)
    loft2 = models.DecimalField(_('loft2'), db_column='loft2', default=0, max_digits=5, decimal_places=2)
    sun_room1 = models.DecimalField(_('sun_room1'), db_column='sun_room1', default=0, max_digits=5, decimal_places=2)
    sun_room2 = models.DecimalField(_('sun_room2'), db_column='sun_room2', default=0, max_digits=5, decimal_places=2)
    layout_note = models.CharField(_('layout_note'), db_column='layout_note', max_length=255, null=True, blank=True)
    room_area = models.DecimalField(_('room_area'), db_column='room_area', default=0, max_digits=5, decimal_places=2)
    direction_id = models.IntegerField(_('direction_id'), db_column='direction_id', db_index=True, default=0)
    balcony_type_id = models.IntegerField(_('balcony_type_id'), db_column='balcony_type_id', default=0)
    balcony_area = models.DecimalField(_('balcony_area'), db_column='balcony_area', default=0, max_digits=5, decimal_places=2)
    rent = models.IntegerField(_('rent'), db_column='rent', db_index=True, default=0)
    rent_upper = models.IntegerField(_('rent_upper'), db_column='rent_upper', db_index=True, default=0)
    trader_rent = models.IntegerField(_('trader_rent'), db_column='trader_rent', db_index=True, default=0)
    rent_tax_type_id = models.IntegerField(_('rent_tax_type_id'), db_column='rent_tax_type_id', default=0)
    rent_hidden = models.BooleanField(_('rent_hidden'), db_column='rent_hidden', default=False)
    condo_fees_type_id = models.IntegerField(_('condo_fees_type_id'), db_column='condo_fees_type_id', default=0)
    condo_fees = models.IntegerField(_('condo_fees'), db_column='condo_fees', default=0)
    condo_fees_tax_type_id = models.IntegerField(_('condo_fees_tax_type_id'), db_column='condo_fees_tax_type_id', default=0)
    water_cost_type_id = models.IntegerField(_('water_cost_type_id'), db_column='water_cost_type_id', default=0)
    water_cost = models.IntegerField(_('water_cost'), db_column='water_cost', default=0)
    water_cost_tax_type_id = models.IntegerField(_('water_cost_tax_type_id'), db_column='water_cost_tax_type_id', default=0)
    water_check_type_id = models.IntegerField(_('water_check_type_id'), db_column='water_check_type_id', default=0)
    payment_type_id = models.IntegerField(_('payment_type_id'), db_column='payment_type_id', default=0)
    payment_fee_type_id = models.IntegerField(_('payment_fee_type_id'), db_column='payment_fee_type_id', default=0)
    payment_fee = models.IntegerField(_('payment_fee'), db_column='payment_fee', default=0)
    payment_fee_tax_type_id = models.IntegerField(_('payment_fee_tax_type_id'), db_column='payment_fee_tax_type_id', default=0)
    monthly_cost_name1 = models.CharField(_('monthly_cost_name1'), db_column='monthly_cost_name1', max_length=100, null=True, blank=True)
    monthly_cost1 = models.IntegerField(_('monthly_cost1'), db_column='monthly_cost1', default=0)
    monthly_cost_tax_type_id1 = models.IntegerField(_('monthly_cost_tax_type_id1'), db_column='monthly_cost_tax_type_id1', default=0)
    monthly_cost_name2 = models.CharField(_('monthly_cost_name2'), db_column='monthly_cost_name2', max_length=100, null=True, blank=True)
    monthly_cost2 = models.IntegerField(_('monthly_cost2'), db_column='monthly_cost2', default=0)
    monthly_cost_tax_type_id2 = models.IntegerField(_('monthly_cost_tax_type_id2'), db_column='monthly_cost_tax_type_id2', default=0)
    monthly_cost_name3 = models.CharField(_('monthly_cost_name3'), db_column='monthly_cost_name3', max_length=100, null=True, blank=True)
    monthly_cost3 = models.IntegerField(_('monthly_cost3'), db_column='monthly_cost3', default=0)
    monthly_cost_tax_type_id3 = models.IntegerField(_('monthly_cost_tax_type_id3'), db_column='monthly_cost_tax_type_id3', default=0)
    monthly_cost_name4 = models.CharField(_('monthly_cost_name4'), db_column='monthly_cost_name4', max_length=100, null=True, blank=True)
    monthly_cost4 = models.IntegerField(_('monthly_cost4'), db_column='monthly_cost4', default=0)
    monthly_cost_tax_type_id4 = models.IntegerField(_('monthly_cost_tax_type_id4'), db_column='monthly_cost_tax_type_id4', default=0)
    monthly_cost_name5 = models.CharField(_('monthly_cost_name5'), db_column='monthly_cost_name5', max_length=100, null=True, blank=True)
    monthly_cost5 = models.IntegerField(_('monthly_cost5'), db_column='monthly_cost5', default=0)
    monthly_cost_tax_type_id5 = models.IntegerField(_('monthly_cost_tax_type_id5'), db_column='monthly_cost_tax_type_id5', default=0)
    monthly_cost_name6 = models.CharField(_('monthly_cost_name6'), db_column='monthly_cost_name6', max_length=100, null=True, blank=True)
    monthly_cost6 = models.IntegerField(_('monthly_cost6'), db_column='monthly_cost6', default=0)
    monthly_cost_tax_type_id6 = models.IntegerField(_('monthly_cost_tax_type_id6'), db_column='monthly_cost_tax_type_id6', default=0)
    monthly_cost_name7 = models.CharField(_('monthly_cost_name7'), db_column='monthly_cost_name7', max_length=100, null=True, blank=True)
    monthly_cost7 = models.IntegerField(_('monthly_cost7'), db_column='monthly_cost7', default=0)
    monthly_cost_tax_type_id7 = models.IntegerField(_('monthly_cost_tax_type_id7'), db_column='monthly_cost_tax_type_id7', default=0)
    monthly_cost_name8 = models.CharField(_('monthly_cost_name8'), db_column='monthly_cost_name8', max_length=100, null=True, blank=True)
    monthly_cost8 = models.IntegerField(_('monthly_cost8'), db_column='monthly_cost8', default=0)
    monthly_cost_tax_type_id8 = models.IntegerField(_('monthly_cost_tax_type_id8'), db_column='monthly_cost_tax_type_id8', default=0)
    monthly_cost_name9 = models.CharField(_('monthly_cost_name9'), db_column='monthly_cost_name9', max_length=100, null=True, blank=True)
    monthly_cost9 = models.IntegerField(_('monthly_cost9'), db_column='monthly_cost9', default=0)
    monthly_cost_tax_type_id9 = models.IntegerField(_('monthly_cost_tax_type_id9'), db_column='monthly_cost_tax_type_id9', default=0)
    monthly_cost_name10 = models.CharField(_('monthly_cost_name10'), db_column='monthly_cost_name10', max_length=100, null=True, blank=True)
    monthly_cost10 = models.IntegerField(_('monthly_cost10'), db_column='monthly_cost10', default=0)
    monthly_cost_tax_type_id10 = models.IntegerField(_('monthly_cost_tax_type_id10'), db_column='monthly_cost_tax_type_id10', default=0)
    monthly_cost_note = models.TextField(_('monthly_cost_note'), db_column='monthly_cost_note', max_length=2000, null=True, blank=True)
    deposit_type_id1 = models.IntegerField(_('deposit_type_id1'), db_column='deposit_type_id1', default=0)
    deposit_notation_id1 = models.IntegerField(_('deposit_notation_id1'), db_column='deposit_notation_id1', default=0)
    deposit_value1 = models.DecimalField(_('deposit_value1'), db_column='deposit_value1', default=0, max_digits=12, decimal_places=2)
    deposit_tax_type_id1 = models.IntegerField(_('deposit_tax_type_id1'), db_column='deposit_tax_type_id1', default=0)
    deposit_comment1 = models.CharField(_('deposit_comment1'), db_column='deposit_comment1', max_length=100, null=True, blank=True)
    deposit_type_id2 = models.IntegerField(_('deposit_type_id2'), db_column='deposit_type_id2', default=0)
    deposit_notation_id2 = models.IntegerField(_('deposit_notation_id2'), db_column='deposit_notation_id2', default=0)
    deposit_value2 = models.DecimalField(_('deposit_value2'), db_column='deposit_value2', default=0, max_digits=12, decimal_places=2)
    deposit_tax_type_id2 = models.IntegerField(_('deposit_tax_type_id2'), db_column='deposit_tax_type_id2', default=0)
    deposit_comment2 = models.CharField(_('deposit_comment2'), db_column='deposit_comment2', max_length=100, null=True, blank=True)
    key_money_type_id1 = models.IntegerField(_('key_money_type_id1'), db_column='key_money_type_id1', default=0)
    key_money_notation_id1 = models.IntegerField(_('key_money_notation_id1'), db_column='key_money_notation_id1', default=0)
    key_money_value1 = models.DecimalField(_('key_money_value1'), db_column='key_money_value1', default=0, max_digits=12, decimal_places=2)
    key_money_tax_type_id1 = models.IntegerField(_('key_money_tax_type_id1'), db_column='key_money_tax_type_id1', default=0)
    key_money_comment1 = models.CharField(_('key_money_comment1'), db_column='key_money_comment1', max_length=100, null=True, blank=True)
    key_money_type_id2 = models.IntegerField(_('key_money_type_id2'), db_column='key_money_type_id2', default=0)
    key_money_notation_id2 = models.IntegerField(_('key_money_notation_id2'), db_column='key_money_notation_id2', default=0)
    key_money_value2 = models.DecimalField(_('key_money_value2'), db_column='key_money_value2', default=0, max_digits=12, decimal_places=2)
    key_money_tax_type_id2 = models.IntegerField(_('key_money_tax_type_id2'), db_column='key_money_tax_type_id2', default=0)
    key_money_comment2 = models.CharField(_('key_money_comment2'), db_column='key_money_comment2', max_length=100, null=True, blank=True)
    contract_years = models.IntegerField(_('contract_years'), db_column='contract_years', default=0)
    contract_months = models.IntegerField(_('contract_months'), db_column='contract_months', default=0)
    renewal_fee_notation_id = models.IntegerField(_('renewal_fee_notation_id'), db_column='renewal_fee_notation_id', default=0)
    renewal_fee_value = models.DecimalField(_('renewal_fee_value'), db_column='renewal_fee_value', default=0, max_digits=12, decimal_places=2)
    renewal_fee_tax_type_id = models.IntegerField(_('renewal_fee_tax_type_id'), db_column='renewal_fee_tax_type_id', default=0)
    renewal_charge_existence_id = models.IntegerField(_('renewal_charge_existence_id'), db_column='renewal_charge_existence_id', default=0)
    renewal_charge = models.IntegerField(_('renewal_charge'), db_column='renewal_charge', default=0)
    renewal_charge_tax_type_id = models.IntegerField(_('renewal_charge_tax_type_id'), db_column='renewal_charge_tax_type_id', default=0)
    is_auto_renewal = models.BooleanField(_('is_auto_renewal'), db_column='is_auto_renewal', default=False)
    renewal_note = models.CharField(_('renewal_note'), db_column='renewal_note', max_length=255, null=True, blank=True)
    recontract_fee_existence_id = models.IntegerField(_('recontract_fee_existence_id'), db_column='recontract_fee_existence_id', default=0)
    recontract_fee = models.IntegerField(_('recontract_fee'), db_column='recontract_fee', default=0)
    recontract_fee_tax_type_id = models.IntegerField(_('recontract_fee_tax_type_id'), db_column='recontract_fee_tax_type_id', default=0)
    recontract_note = models.CharField(_('recontract_note'), db_column='recontract_note', max_length=255, null=True, blank=True)
    insurance_type_id = models.IntegerField(_('insurance_type_id'), db_column='insurance_type_id', default=0)
    insurance_company = models.CharField(_('insurance_company'), db_column='insurance_company', max_length=100, null=True, blank=True)
    insurance_years = models.IntegerField(_('insurance_years'), db_column='insurance_years', default=0)
    insurance_fee = models.IntegerField(_('insurance_fee'), db_column='insurance_fee', default=0)
    insurance_fee_tax_type_id = models.IntegerField(_('insurance_fee_tax_type_id'), db_column='insurance_fee_tax_type_id', default=0)
    guarantee_type_id = models.IntegerField(_('guarantee_type_id'), db_column='guarantee_type_id', default=0)
    guarantee_company = models.CharField(_('guarantee_company'), db_column='guarantee_company', max_length=100, null=True, blank=True)
    guarantee_fee = models.CharField(_('guarantee_fee'), db_column='guarantee_fee', max_length=255, null=True, blank=True)
    document_cost_existence_id = models.IntegerField(_('document_cost_existence_id'), db_column='document_cost_existence_id', default=0)
    document_cost = models.IntegerField(_('document_cost'), db_column='document_cost', default=0)
    document_cost_tax_type_id = models.IntegerField(_('document_cost_tax_type_id'), db_column='document_cost_tax_type_id', default=0)
    document_cost_comment = models.CharField(_('document_cost_comment'), db_column='document_cost_comment', max_length=100, null=True, blank=True)
    key_change_cost_existence_id = models.IntegerField(_('key_change_cost_existence_id'), db_column='key_change_cost_existence_id', default=0)
    key_change_cost = models.IntegerField(_('key_change_cost'), db_column='key_change_cost', default=0)
    key_change_cost_tax_type_id = models.IntegerField(_('key_change_cost_tax_type_id'), db_column='key_change_cost_tax_type_id', default=0)
    key_change_comment = models.CharField(_('key_change_comment'), db_column='key_change_comment', max_length=100, null=True, blank=True)
    initial_cost_name1 = models.CharField(_('initial_cost_name1'), db_column='initial_cost_name1', max_length=100, null=True, blank=True)
    initial_cost1 = models.IntegerField(_('initial_cost1'), db_column='initial_cost1', default=0)
    initial_cost_tax_type_id1 = models.IntegerField(_('initial_cost_tax_type_id1'), db_column='initial_cost_tax_type_id1', default=0)
    initial_cost_name2 = models.CharField(_('initial_cost_name2'), db_column='initial_cost_name2', max_length=100, null=True, blank=True)
    initial_cost2 = models.IntegerField(_('initial_cost2'), db_column='initial_cost2', default=0)
    initial_cost_tax_type_id2 = models.IntegerField(_('initial_cost_tax_type_id2'), db_column='initial_cost_tax_type_id2', default=0)
    initial_cost_name3 = models.CharField(_('initial_cost_name3'), db_column='initial_cost_name3', max_length=100, null=True, blank=True)
    initial_cost3 = models.IntegerField(_('initial_cost3'), db_column='initial_cost3', default=0)
    initial_cost_tax_type_id3 = models.IntegerField(_('initial_cost_tax_type_id3'), db_column='initial_cost_tax_type_id3', default=0)
    initial_cost_name4 = models.CharField(_('initial_cost_name4'), db_column='initial_cost_name4', max_length=100, null=True, blank=True)
    initial_cost4 = models.IntegerField(_('initial_cost4'), db_column='initial_cost4', default=0)
    initial_cost_tax_type_id4 = models.IntegerField(_('initial_cost_tax_type_id4'), db_column='initial_cost_tax_type_id4', default=0)
    initial_cost_name5 = models.CharField(_('initial_cost_name5'), db_column='initial_cost_name5', max_length=100, null=True, blank=True)
    initial_cost5 = models.IntegerField(_('initial_cost5'), db_column='initial_cost5', default=0)
    initial_cost_tax_type_id5 = models.IntegerField(_('initial_cost_tax_type_id5'), db_column='initial_cost_tax_type_id5', default=0)
    initial_cost_name6 = models.CharField(_('initial_cost_name6'), db_column='initial_cost_name6', max_length=100, null=True, blank=True)
    initial_cost6 = models.IntegerField(_('initial_cost6'), db_column='initial_cost6', default=0)
    initial_cost_tax_type_id6 = models.IntegerField(_('initial_cost_tax_type_id6'), db_column='initial_cost_tax_type_id6', default=0)
    initial_cost_name7 = models.CharField(_('initial_cost_name7'), db_column='initial_cost_name7', max_length=100, null=True, blank=True)
    initial_cost7 = models.IntegerField(_('initial_cost7'), db_column='initial_cost7', default=0)
    initial_cost_tax_type_id7 = models.IntegerField(_('initial_cost_tax_type_id7'), db_column='initial_cost_tax_type_id7', default=0)
    initial_cost_name8 = models.CharField(_('initial_cost_name8'), db_column='initial_cost_name8', max_length=100, null=True, blank=True)
    initial_cost8 = models.IntegerField(_('initial_cost8'), db_column='initial_cost8', default=0)
    initial_cost_tax_type_id8 = models.IntegerField(_('initial_cost_tax_type_id8'), db_column='initial_cost_tax_type_id8', default=0)
    initial_cost_name9 = models.CharField(_('initial_cost_name9'), db_column='initial_cost_name9', max_length=100, null=True, blank=True)
    initial_cost9 = models.IntegerField(_('initial_cost9'), db_column='initial_cost9', default=0)
    initial_cost_tax_type_id9 = models.IntegerField(_('initial_cost_tax_type_id9'), db_column='initial_cost_tax_type_id9', default=0)
    initial_cost_name10 = models.CharField(_('initial_cost_name10'), db_column='initial_cost_name10', max_length=100, null=True, blank=True)
    initial_cost10 = models.IntegerField(_('initial_cost10'), db_column='initial_cost10', default=0)
    initial_cost_tax_type_id10 = models.IntegerField(_('initial_cost_tax_type_id10'), db_column='initial_cost_tax_type_id10', default=0)
    initial_cost_note = models.TextField(_('initial_cost_note'), db_column='initial_cost_note', max_length=2000, null=True, blank=True)
    free_rent_type_id = models.IntegerField(_('free_rent_type_id'), db_column='free_rent_type_id', default=0)
    free_rent_months = models.IntegerField(_('free_rent_months'), db_column='free_rent_months', default=0)
    free_rent_limit_year = models.IntegerField(_('free_rent_limit_year'), db_column='free_rent_limit_year', default=0)
    free_rent_limit_month = models.IntegerField(_('free_rent_limit_month'), db_column='free_rent_limit_month', default=0)
    cancel_notice_limit = models.IntegerField(_('cancel_notice_limit'), db_column='cancel_notice_limit', default=0)
    cancel_note = models.CharField(_('cancel_note'), db_column='cancel_note', max_length=255, null=True, blank=True)
    short_cancel_note = models.CharField(_('short_cancel_note'), db_column='short_cancel_note', max_length=255, null=True, blank=True)
    cleaning_type_id = models.IntegerField(_('cleaning_type_id'), db_column='cleaning_type_id', default=0)
    cleaning_cost = models.IntegerField(_('cleaning_cost'), db_column='cleaning_cost', default=0)
    cleaning_cost_tax_type_id = models.IntegerField(_('cleaning_cost_tax_type_id'), db_column='cleaning_cost_tax_type_id', default=0)
    cleaning_note = models.CharField(_('cleaning_note'), db_column='cleaning_note', max_length=255, null=True, blank=True)
    special_agreement = models.TextField(_('special_agreement'), db_column='special_agreement', max_length=2000, null=True, blank=True)
    electric_type_id = models.IntegerField(_('electric_type_id'), db_column='electric_type_id', default=0)
    electric_comment = models.CharField(_('electric_comment'), db_column='electric_comment', max_length=100, null=True, blank=True)
    gas_type_id = models.IntegerField(_('gas_type_id'), db_column='gas_type_id', default=0)
    gas_comment = models.CharField(_('gas_comment'), db_column='gas_comment', max_length=100, null=True, blank=True)
    bath_type_id = models.IntegerField(_('bath_type_id'), db_column='bath_type_id', default=0)
    bath_comment = models.CharField(_('bath_comment'), db_column='bath_comment', max_length=100, null=True, blank=True)
    toilet_type_id = models.IntegerField(_('toilet_type_id'), db_column='toilet_type_id', default=0)
    toilet_comment = models.CharField(_('toilet_comment'), db_column='toilet_comment', max_length=100, null=True, blank=True)
    kitchen_range_type_id = models.IntegerField(_('kitchen_range_type_id'), db_column='kitchen_range_type_id', default=0)
    kitchen_range_comment = models.CharField(_('kitchen_range_comment'), db_column='kitchen_range_comment', max_length=100, null=True, blank=True)
    internet_type_id = models.IntegerField(_('internet_type_id'), db_column='internet_type_id', default=0)
    internet_comment = models.CharField(_('internet_comment'), db_column='internet_comment', max_length=100, null=True, blank=True)
    washer_type_id = models.IntegerField(_('washer_type_id'), db_column='washer_type_id', default=0)
    washer_comment = models.CharField(_('washer_comment'), db_column='washer_comment', max_length=100, null=True, blank=True)
    pet_type_id = models.IntegerField(_('pet_type_id'), db_column='pet_type_id', default=0)
    pet_comment = models.CharField(_('pet_comment'), db_column='pet_comment', max_length=100, null=True, blank=True)
    instrument_type_id = models.IntegerField(_('instrument_type_id'), db_column='instrument_type_id', default=0)
    live_together_type_id = models.IntegerField(_('live_together_type_id'), db_column='live_together_type_id', default=0)
    children_type_id = models.IntegerField(_('children_type_id'), db_column='children_type_id', default=0)
    share_type_id = models.IntegerField(_('share_type_id'), db_column='share_type_id', default=0)
    non_japanese_type_id = models.IntegerField(_('non_japanese_type_id'), db_column='non_japanese_type_id', default=0)
    only_woman_type_id = models.IntegerField(_('only_woman_type_id'), db_column='only_woman_type_id', default=0)
    only_man_type_id = models.IntegerField(_('only_man_type_id'), db_column='only_man_type_id', default=0)
    corp_contract_type_id = models.IntegerField(_('corp_contract_type_id'), db_column='corp_contract_type_id', default=0)
    student_type_id = models.IntegerField(_('student_type_id'), db_column='student_type_id', default=0)
    new_student_type_id = models.IntegerField(_('new_student_type_id'), db_column='new_student_type_id', default=0)
    welfare_type_id = models.IntegerField(_('welfare_type_id'), db_column='welfare_type_id', default=0)
    office_use_type_id = models.IntegerField(_('office_use_type_id'), db_column='office_use_type_id', default=0)
    constraint_note = models.CharField(_('constraint_note'), db_column='constraint_note', max_length=255, null=True, blank=True)
    reform_comment = models.CharField(_('reform_comment'), db_column='reform_comment', max_length=100, null=True, blank=True)
    reform_year = models.IntegerField(_('reform_year'), db_column='reform_year', default=0)
    reform_month = models.IntegerField(_('reform_month'), db_column='reform_month', default=0)
    reform_note = models.CharField(_('reform_note'), db_column='reform_note', max_length=255, null=True, blank=True)
    trader_publish_type_id = models.IntegerField(_('trader_publish_type_id'), db_column='trader_publish_type_id', default=0)
    trader_publish_note = models.CharField(_('trader_publish_note'), db_column='trader_publish_note', max_length=255, null=True, blank=True)
    trader_portal_type_id = models.IntegerField(_('trader_portal_type_id'), db_column='trader_portal_type_id', default=0)
    trader_portal_note = models.CharField(_('trader_portal_note'), db_column='trader_portal_note', max_length=255, null=True, blank=True)
    ad_type_id = models.IntegerField(_('ad_type_id'), db_column='ad_type_id', default=0)
    ad_value = models.DecimalField(_('ad_value'), db_column='ad_value', default=0, max_digits=12, decimal_places=2)
    ad_tax_type_id = models.IntegerField(_('ad_tax_type_id'), db_column='ad_tax_type_id', default=0)
    trader_ad_type_id = models.IntegerField(_('trader_ad_type_id'), db_column='trader_ad_type_id', default=0)
    trader_ad_value = models.DecimalField(_('trader_ad_value'), db_column='trader_ad_value', default=0, max_digits=12, decimal_places=2)
    trader_ad_tax_type_id = models.IntegerField(_('trader_ad_tax_type_id'), db_column='trader_ad_tax_type_id', default=0)
    owner_fee_type_id = models.IntegerField(_('owner_fee_type_id'), db_column='owner_fee_type_id', default=0)
    key_no = models.CharField(_('key_no'), db_column='key_no', max_length=50, null=True, blank=True)
    key_place_note = models.CharField(_('key_place_note'), db_column='key_place_note', max_length=255, null=True, blank=True)
    private_note = models.TextField(_('private_note'), db_column='private_note', max_length=2000, null=True, blank=True)
    management_note = models.TextField(_('management_note'), db_column='management_note', max_length=2000, null=True, blank=True)
    created_at = models.DateTimeField(_('created_at'), db_column='created_at', default=timezone.now)
    created_user_id = models.IntegerField(_('created_user_id'), db_column='created_user_id', db_index=True, default=0)
    updated_at = models.DateTimeField(_('updated_at'), db_column='updated_at', default=timezone.now)
    updated_user_id = models.IntegerField(_('updated_user_id'), db_column='updated_user_id', db_index=True, default=0)
    is_deleted = models.BooleanField(_('is_deleted'), db_column='is_deleted', db_index=True, default=False)

    def __str__(self):
        return self.room_no

    class Meta:
        db_table = 'room'
        ordering = ['building_id', 'room_no', 'id']
        verbose_name = _('room')
        verbose_name_plural = _('rooms')
