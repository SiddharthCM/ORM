from django.db import models
from django.contrib import admin

class Amazon(models.Model):
    Product_id=models.IntegerField(primary_key=True)
    Product_name=models.CharField(max_length=100)
    Product_category=models.CharField(max_length=100)
    Product_quantity=models.IntegerField()
    Serial_number=models.IntegerField()
    Manufacturing_Date=models.DateField()
    Delivery_date=models.DateField()
    model_number=models.IntegerField()
    

class AmazonAdmin(admin.ModelAdmin):
    list_display=["Product_id","Product_name", "Product_category", "Product_quantity","Serial_number","Manufacturing_Date","Delivery_date","model_number"]