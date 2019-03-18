from django.contrib import admin
from .models import *
from .helpers import *

# Register your models here.
class HouseAdmin(admin.ModelAdmin):
	list_display = ('name', 'pln_number', 'address', 'owner')
admin.site.register(House, HouseAdmin)

class RentAdmin(admin.ModelAdmin):
	list_display = ('house', 'penyewa', 'price', 'active')
	def penyewa(self, model_obj):
		return "%s %s" % (model_obj.renter.first_name, model_obj.renter.last_name)
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'price':
			kwargs['initial'] = [Price.objects.filter(active=True)]
			return db_field.formfield(**kwargs)
		return super(RentAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(Rent, RentAdmin)

class PaymentAdmin(admin.ModelAdmin):
	list_display = ('rumah', 'penyewa', 'harga', 'pay_date', 'start', 'end')
	def rumah(self, model_obj):
		return "%s" % model_obj.rent.house
	def harga(self, model_obj):
		return "%s" % model_obj.rent.price
	def penyewa(self, model_obj):
		return "%s %s" % (model_obj.rent.renter.first_name, model_obj.rent.renter.last_name)
admin.site.register(Payment, PaymentAdmin)

class ExpenseAdmin(admin.ModelAdmin):
	list_display = ('house', 'remark', 'date', 'biaya', 'receipt_number')
	def biaya(self, model_obj):
		return toRupiah(model_obj.nominal)

admin.site.register(Expense, ExpenseAdmin)

class PriceAdmin(admin.ModelAdmin):
	list_display = ('harga', 'active')
	def harga(self, model_obj):
		return toRupiah(model_obj.nominal)
admin.site.register(Price, PriceAdmin)

admin.site.site_header = "Pintoko Rent House"
admin.site.site_title = "Pintoko Rent House CMS"
admin.site.index_title = "House Management"