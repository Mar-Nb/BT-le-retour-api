from django.db import models

# Create your models here.

class InfosProduit(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    tigID = models.IntegerField(default = "-1")
    name = models.CharField(max_length = 100, blank = True, default = '')
    category = models.IntegerField(default = '-1')
    price = models.FloatField(default = '0')
    unit = models.CharField(max_length = 20, blank = True, default = '')
    availability = models.BooleanField(default = True)
    sale = models.BooleanField(default = False)
    discount = models.FloatField(default = '0')
    comments = models.CharField(max_length = 100, blank = True, default = '')
    owner = models.CharField(max_length = 20, blank = True, default = 'tig')
    quantityInStock = models.IntegerField(default = "0")

    class Meta:
        ordering = ("tigID", "quantityInStock",)

class TransactionProduit(models.Model):
    date = models.DateTimeField(auto_now_add = True)
    tigID = models.IntegerField(default = "-1")
    price = models.FloatField(default = "0")
    quantity = models.IntegerField(default = "0")
    type = models.CharField(max_length = 20, blank = True, default = "")

    class Meta:
        ordering = ("date",)
