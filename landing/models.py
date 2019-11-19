import datetime

from django.db import models
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class Person(models.Model):
    class Meta:
        db_table = 'Person'
        ordering = ['person_id']
        verbose_name = 'Представник'
        verbose_name_plural = 'Представники'

    person_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class City(models.Model):
    class Meta:
        db_table = 'City'
        ordering = ['city_id']
        verbose_name = 'Місто'
        verbose_name_plural = 'Міста'

    city_id = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=40)

    def __str__(self):
        return self.city


class Property_address(models.Model):
    class Meta:
        db_table = 'Property_address'
        ordering = ['property_address_id']
        verbose_name = 'Адреса власності'
        verbose_name_plural = 'Адреси власностей'

    property_address_id = models.IntegerField(primary_key=True)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    street = models.CharField(max_length=100)
    apartment = models.CharField(max_length=30)

    def __str__(self):
        return "%s, %s, %s" % (self.city, self.street, self.apartment)


class Property_title(models.Model):
    class Meta:
        db_table = 'Property_title'
        ordering = ['property_title_id']
        verbose_name = 'Назва власності'
        verbose_name_plural = 'Назви власностей'

    property_title_id = models.IntegerField(primary_key=True)
    property_title = models.CharField(max_length=25)

    def __str__(self):
        return self.property_title


class Property_type(models.Model):
    class Meta:
        db_table = 'Property_type'
        ordering = ['property_type_id']
        verbose_name = 'Тип власності'
        verbose_name_plural = 'Типи власностей'

    property_type_id = models.IntegerField(primary_key=True)
    property_type = models.CharField(max_length=15)

    def __str__(self):
        return self.property_type


class Property(models.Model):
    class Meta:
        db_table = 'Property'
        ordering = ['property_id']
        verbose_name = 'Власність'
        verbose_name_plural = 'Власності'

    property_id = models.IntegerField(primary_key=True)
    property_type = models.ForeignKey(Property_type, on_delete=models.DO_NOTHING)
    property_title = models.ForeignKey(Property_title, on_delete=models.DO_NOTHING)
    assessed_value = models.FloatField()
    property_address = models.ForeignKey(Property_address, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "%s, %s" % (self.property_title, self.assessed_value)


class Monthly_payment(models.Model):
    class Meta:
        db_table = 'Monthly_payment'
        ordering = ['monthly_payment_id']
        verbose_name = 'Місячна сплата'
        verbose_name_plural = 'Місячні сплати'

    monthly_payment_id = models.IntegerField(primary_key=True)
    monthly_payment = models.FloatField()
    expiration_payment = models.FloatField()

    def __str__(self):
        return "Monthly payment %s, Expiration payment %s" % (self.monthly_payment, self.expiration_payment)


class Customer(models.Model):
    class Meta:
        db_table = 'Customer'
        ordering = ['customer_id']
        verbose_name = 'Клієнт'
        verbose_name_plural = 'Клієнти'

    customer_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    property_type = models.ForeignKey(Property, on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=40)
    person = models.ForeignKey(Person, models.DO_NOTHING)
    edrpou = models.CharField(max_length=8)

    def __str__(self):
        return self.name


class Loan(models.Model):
    class Meta:
        db_table = 'Loan'
        ordering = ['loan_id']
        verbose_name = 'Кредит'
        verbose_name_plural = 'Кредити'

    loan_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=50)
    interest_rate = models.FloatField()
    monthly_payment = models.ForeignKey(Monthly_payment, models.DO_NOTHING, default=None, blank=True, null=True)

    def __str__(self):
        return self.description


class Record(models.Model):
    class Meta:
        db_table = 'Record'
        ordering = ['record_id']
        verbose_name = 'Облік кредитів'
        verbose_name_plural = 'Облік кредитів'

    record_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    loan = models.ForeignKey(Loan, models.DO_NOTHING)
    amount = models.FloatField()
    amount_remaining = models.FloatField()
    date_granted = models.DateField()
    date_repaid = models.DateField(blank=True)
    month_paid = models.DecimalField(max_digits=10, decimal_places=8, blank=True)
    success_message = "created"

    def save(self, **kwargs):
        self.amount_remaining = self.amount * self.loan.interest_rate
        if self.amount > self.customer.property_type.assessed_value:
            return
        else:
            super(Record, self).save()

    def get_success_message(self, cleaned_data):
        return self.success_message

    def __str__(self):
        return "Record id %s/ %s/ %s/ %s" % (self.record_id, self.customer, self.loan, self.amount)


# class Monthly_payment_record(models.Model):
#     class Meta:
#         db_table = 'Monthly_payment_record'
#         unique_together = (('record', 'date'),)
#         verbose_name = 'Облік місячних сплат'
#         verbose_name_plural = 'Облік місячних сплат'
#
#     record = models.ForeignKey(Record, models.DO_NOTHING, primary_key=True)
#     amount = models.DecimalField(verbose_name="Уведіть суму", max_digits=10, decimal_places=2)
#     date = models.DateField()
#
#     def __str__(self):
#         return "%s" % (self.record)
   # def save(self, **kwargs):
    #    print('saving')
     #   self.record.month_paid += self.amount / self.record.loan.monthly_payment.monthly_payment
      #  if Monthly_payment_record.objects.all().count() < int(self.record.month_paid):
       #     self.date = self.date.month + 1
        #    super(Monthly_payment_record, self).save()


