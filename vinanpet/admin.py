from django.contrib import admin
from .models import VinanPetLtd, Branch, Product, Tank, Pump
from django.contrib.auth.models import Group


# Register your models here.

admin.site.site_header = 'Vinan Pet Ltd Dashboard'


class VinanPetLtdAdmin(admin.ModelAdmin):
    list_display = ('transaction_Date', 'entry_Date', 'branch', 'product', 'tank_Opening', 'tank_Closing', 'tank_Difference', 'pump_Opening', 'pump_Closing', 'pump_Difference', 'price', 'amount', 'pos', 'cash', 'expenses', 'balance', 'amount_Deposited', 'teller_ID', 'teller')
    list_filter = ['branch', 'transaction_Date']
    search_fields = ['branch__branch', 'transaction_Date']



admin.site.register(VinanPetLtd, VinanPetLtdAdmin)
admin.site.register(Branch)
admin.site.register(Product)
admin.site.register(Tank)
admin.site.register(Pump)

admin.site.unregister(Group)