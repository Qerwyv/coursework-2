from django.contrib import admin
from .models import *
admin.site.site_url = None


class Person_admin(admin.ModelAdmin):
    list_display = [field.name for field in Person._meta.fields]
    readonly_fields = ['person_id']
    list_filter = ['name']
    search_fields = ['name', 'person_id']

    class Meta:
        model = Person


class Monthly_payment_admin(admin.ModelAdmin):
    list_display = [field.name for field in Monthly_payment._meta.fields]
    readonly_fields = ['monthly_payment_id']


    class Meta:
        model = Monthly_payment


class Property_admin(admin.ModelAdmin):
    list_display = [field.name for field in Property._meta.fields]
    readonly_fields = ['property_id']

    class Meta:
        model = Property


class Record_admin(admin.ModelAdmin):
    list_display = [field.name for field in Record._meta.fields]
    list_filter = ['customer']
    readonly_fields = ['record_id','amount_remaining', 'month_paid']

    class Meta:
        model = Record

class Customer_admin(admin.ModelAdmin):
    list_display = [field.name for field in Customer._meta.fields]
    list_filter = ['name']
    readonly_fields = ['customer_id']

    class Meta:
        model = Customer

class Loan_admin(admin.ModelAdmin):
    list_display = [field.name for field in Loan._meta.fields]
    list_filter = ['title']
    search_fields = ['description']
    readonly_fields = ['loan_id']

    class Meta:
        model = Loan

# class Monthly_payment_record_admin(admin.ModelAdmin):
#     list_display = [field.name for field in Monthly_payment_record._meta.fields]
#     readonly_fields = ['monthly_payment_record_id']
#
#     class Meta:
#         model = Loan


class City_admin(admin.ModelAdmin):
    list_display = [field.name for field in City._meta.fields]
    readonly_fields = ['city_id']

    class Meta:
        model = City

class Property_address_admin(admin.ModelAdmin):
    list_display = [field.name for field in Property_address._meta.fields]
    readonly_fields = ['property_address_id']

    class Meta:
        model = Property_address

class Property_title_admin(admin.ModelAdmin):
    class Meta:
        model = Property_title
    list_display = [field.name for field in Property_title._meta.fields]
    readonly_fields = ['property_title_id']

class Property_type_admin(admin.ModelAdmin):
    class Meta:
        model = Property_type
    list_display = [field.name for field in Property_type._meta.fields]
    readonly_fields = ['property_type_id']


admin.site.register(Property, Property_admin)
#admin.site.register(Monthly_payment_record)
admin.site.register(Customer, Customer_admin)
admin.site.register(Loan, Loan_admin)
admin.site.register(Record, Record_admin)
admin.site.register(Person, Person_admin)
admin.site.register(Monthly_payment, Monthly_payment_admin)
admin.site.register(Property_address, Property_address_admin)
admin.site.register(Property_title, Property_title_admin)
admin.site.register(Property_type, Property_type_admin)
admin.site.register(City, City_admin)
