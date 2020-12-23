from django.contrib import admin

from core.models import FIO, Type, Addresses, Phones


@admin.register(FIO)
class FIOAdmin(admin.ModelAdmin):
    pass


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Addresses)
class AddressesAdmin(admin.ModelAdmin):
    pass


@admin.register(Phones)
class PhonesAdmin(admin.ModelAdmin):
    pass
