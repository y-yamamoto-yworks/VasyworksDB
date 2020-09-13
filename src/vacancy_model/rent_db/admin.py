"""
System Name: Vasyworks
Project Name: vacancy_model
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import AdType
from .models import AllowType
from .models import Area
from .models import ArrivalType
from .models import User
from .models import VacancyLevel
from .models import VacancyUser
from .models import BalconyType
from .models import BathType 
from .models import BikeParkingType 
from .models import Building 
from .models import BuildingFacility 
from .models import BuildingFile 
from .models import BuildingGarage 
from .models import BuildingLandmark 
from .models import BuildingMovie
from .models import BuildingPanorama 
from .models import BuildingPicture
from .models import BuildingType 
from .models import City 
from .models import CityArea
from .models import CityElementarySchool
from .models import CityJuniorHighSchool
from .models import CleaningType
from .models import Company
from .models import CondoFeesType
from .models import Department
from .models import DepositNotation
from .models import DepositType
from .models import Direction 
from .models import DocumentFile
from .models import ElectricType
from .models import ElementarySchool
from .models import Equipment
from .models import EquipmentCategory
from .models import Existence
from .models import Facility
from .models import FreeRentType
from .models import GarageStatus
from .models import GarageType
from .models import GasType
from .models import GuaranteeCompany
from .models import GuaranteeType
from .models import InsuranceCompany
from .models import InsuranceType
from .models import InternetType
from .models import JuniorHighSchool
from .models import KeyMoneyNotation
from .models import KeyMoneyType
from .models import KitchenRangeType
from .models import KitchenType
from .models import Landmark
from .models import LandmarkType
from .models import LayoutType
from .models import LayoutTypeCategory
from .models import ManagementInfo
from .models import ManagementType
from .models import MonthDay
from .models import MovieType
from .models import Owner
from .models import OwnerFeeType
from .models import PanoramaType
from .models import PaymentFeeType
from .models import PaymentType
from .models import PetType
from .models import PictureType
from .models import PostalCode
from .models import Pref 
from .models import Railway
from .models import RenewalFeeNotation
from .models import RentalType
from .models import Room
from .models import RoomAuthLevel
from .models import RoomEquipment
from .models import RoomMovie
from .models import RoomPanorama
from .models import RoomPicture
from .models import RoomStatus
from .models import RoomStatusLog
from .models import RoomVacancyTheme
from .models import Staff
from .models import Station
from .models import Structure
from .models import TaxType
from .models import ToiletType
from .models import Trader
from .models import TraderGroup
from .models import TransferStation
from .models import VacancyInputBikeParking
from .models import VacancyInputCancelNotice
from .models import VacancyInputChangeLock
from .models import VacancyInputCleaning
from .models import VacancyInputDocumentPrice
from .models import VacancyInputElectric
from .models import VacancyInputGarage
from .models import VacancyInputGas
from .models import VacancyInputGuarantee
from .models import VacancyInputGuarantorLimit
from .models import VacancyInputInsurance
from .models import VacancyInputInternet
from .models import VacancyInputPayment
from .models import VacancyInputRenewalCharge
from .models import VacancyInputShortCancel
from .models import VacancyInputWater
from .models import VacancyStatus
from .models import VacancyTheme
from .models import WasherType
from .models import WaterCheckType
from .models import WaterCostType


@admin.register(User)
class AdminUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': (
            'last_name',
            'first_name',
            'email',
            'staff_id'
        )}),
        (_('Permissions'), {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'is_company',
            'is_company_admin',
            'groups',
            'user_permissions'
        )}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'last_name', 'first_name', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    filter_horizontal = ('groups', 'user_permissions')


@admin.register(VacancyUser)
class AdminVacancyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': (
            'display_name',
            'email',
        )}),
        (_('Permissions'), {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'level_id',
            'allow_org_image',
            'groups',
            'user_permissions'
        )}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'display_name', 'is_staff')
    search_fields = ('username', 'display_name', 'email', 'department')
    filter_horizontal = ('groups', 'user_permissions')


admin.site.register(AdType)
admin.site.register(AllowType)
admin.site.register(Area)
admin.site.register(ArrivalType)
admin.site.register(VacancyLevel)
admin.site.register(BalconyType)
admin.site.register(BathType)
admin.site.register(BikeParkingType)
admin.site.register(Building)
admin.site.register(BuildingFacility)
admin.site.register(BuildingFile)
admin.site.register(BuildingGarage)
admin.site.register(BuildingLandmark)
admin.site.register(BuildingMovie)
admin.site.register(BuildingPanorama)
admin.site.register(BuildingPicture)
admin.site.register(BuildingType)
admin.site.register(City)
admin.site.register(CityArea)
admin.site.register(CityElementarySchool)
admin.site.register(CityJuniorHighSchool)
admin.site.register(CleaningType)
admin.site.register(Company)
admin.site.register(CondoFeesType)
admin.site.register(Department)
admin.site.register(DepositNotation)
admin.site.register(DepositType)
admin.site.register(Direction)
admin.site.register(DocumentFile)
admin.site.register(ElectricType)
admin.site.register(ElementarySchool)
admin.site.register(Equipment)
admin.site.register(EquipmentCategory)
admin.site.register(Existence)
admin.site.register(Facility)
admin.site.register(FreeRentType)
admin.site.register(GarageStatus)
admin.site.register(GarageType)
admin.site.register(GasType)
admin.site.register(GuaranteeCompany)
admin.site.register(GuaranteeType)
admin.site.register(InsuranceCompany)
admin.site.register(InsuranceType)
admin.site.register(InternetType)
admin.site.register(JuniorHighSchool)
admin.site.register(KeyMoneyNotation)
admin.site.register(KeyMoneyType)
admin.site.register(KitchenRangeType)
admin.site.register(KitchenType)
admin.site.register(Landmark)
admin.site.register(LandmarkType)
admin.site.register(LayoutType)
admin.site.register(LayoutTypeCategory)
admin.site.register(ManagementInfo)
admin.site.register(ManagementType)
admin.site.register(MonthDay)
admin.site.register(MovieType)
admin.site.register(Owner)
admin.site.register(OwnerFeeType)
admin.site.register(PanoramaType)
admin.site.register(PaymentFeeType)
admin.site.register(PaymentType)
admin.site.register(PetType)
admin.site.register(PictureType)
admin.site.register(PostalCode)
admin.site.register(Pref)
admin.site.register(Railway)
admin.site.register(RenewalFeeNotation)
admin.site.register(RentalType)
admin.site.register(Room)
admin.site.register(RoomAuthLevel)
admin.site.register(RoomEquipment)
admin.site.register(RoomMovie)
admin.site.register(RoomPanorama)
admin.site.register(RoomPicture)
admin.site.register(RoomStatus)
admin.site.register(RoomStatusLog)
admin.site.register(RoomVacancyTheme)
admin.site.register(Staff)
admin.site.register(Station)
admin.site.register(Structure)
admin.site.register(TaxType)
admin.site.register(ToiletType)
admin.site.register(Trader)
admin.site.register(TraderGroup)
admin.site.register(TransferStation)
admin.site.register(VacancyInputBikeParking)
admin.site.register(VacancyInputCancelNotice)
admin.site.register(VacancyInputChangeLock)
admin.site.register(VacancyInputCleaning)
admin.site.register(VacancyInputDocumentPrice)
admin.site.register(VacancyInputElectric)
admin.site.register(VacancyInputGarage)
admin.site.register(VacancyInputGas)
admin.site.register(VacancyInputGuarantee)
admin.site.register(VacancyInputGuarantorLimit)
admin.site.register(VacancyInputInsurance)
admin.site.register(VacancyInputInternet)
admin.site.register(VacancyInputPayment)
admin.site.register(VacancyInputRenewalCharge)
admin.site.register(VacancyInputShortCancel)
admin.site.register(VacancyInputWater)
admin.site.register(VacancyStatus)
admin.site.register(VacancyTheme)
admin.site.register(WasherType)
admin.site.register(WaterCheckType)
admin.site.register(WaterCostType)
