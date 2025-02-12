# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Inventory(models.Model):
    locationid = models.OneToOneField('Location', models.DO_NOTHING, db_column='locationid', primary_key=True)  # The composite primary key (locationid, productid) found, that is not supported. The first column is selected.
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='productid')
    quantity = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory'
        unique_together = (('locationid', 'productid'),)


class Location(models.Model):
    locationid = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    state = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location'


class Product(models.Model):
    productid = models.IntegerField(primary_key=True)
    size = models.CharField(max_length=45, blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'
