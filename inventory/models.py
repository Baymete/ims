from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Item(models.Model):
    serial_number = models.CharField(max_length=50)
    item_number = models.CharField(max_length=50, blank=True)
    asset_number = models.CharField(max_length=10, blank=True)
    entry_date = models.DateField()
    invoice_date = models.DateField(null=True, blank=True)
    invoice_number =models.CharField(max_length=20, blank=True)
    po_number = models.CharField(max_length=20, blank=True)
    warranty_status = models.BooleanField()
    warranty_until = models.DateField(null=True, blank=True)
    current_owner = models.ForeignKey(User)
    notes = models.TextField(blank=True)
    
    item_type = models.ForeignKey('ItemType', null=True)
    item_manufacturer = models.ForeignKey('ItemManufacturer', null=True)
    item_model = models.ForeignKey('ItemModel', null=True)
    operating_system = models.ForeignKey('OperatingSystem', null=True)
    storage_capacity = models.ForeignKey('StorageCapacity', null=True)
    memory_capacity = models.ForeignKey('MemoryCapacity', null=True)
    processor = models.ForeignKey('Processor', null=True)
    supplier = models.ForeignKey('Supplier', null=True)
    
    
    def __unicode__(self):
        return self.serial_number

    def save(self):
        if self.pk is None:
            self.entry_date = datetime.today()
        #self.modified = datetime.today()
        super(Item, self).save()


class Personnel(models.Model):
    personnel_number = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    domain_name = models.CharField(max_length=10)
    email= models.EmailField()
    status = models.BooleanField()
    
    def __unicode__(self):
        return ' '.join([self.name,self.surname])


class Territory(models.Model):
    territory = models.CharField(max_length=10)

    def __unicode__(self):
        return self.territory


class ItemType(models.Model):
    item_type = models.CharField(max_length=10)
    
    def __unicode__(self):
        return self.item_type
    

class ItemManufacturer(models.Model):
    item_manufacturer = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.item_manufacturer
    

class ItemModel(models.Model):
    item_model = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.item_model
    

class OperatingSystem(models.Model):
    operating_system = models.CharField(max_length=25)
    
    def __unicode__(self):
        return self.operating_system
    

class StorageCapacity(models.Model):
    storage_capacity = models.CharField(max_length=25)
    
    def __unicode__(self):
        return self.storage_capacity
    

class MemoryCapacity(models.Model):
    memory_capacity = models.CharField(max_length=10)
    
    def __unicode__(self):
        return self.memory_capacity
    

class Processor(models.Model):
    processor = models.CharField(max_length=25)
    
    def __unicode__(self):
        return self.processor
    

class Supplier(models.Model):
    supplier = models.CharField(max_length=25)
    
    def __unicode__(self):
        return self.supplier
    

class InternalDepartment(models.Model):
    internal_department = models.CharField(max_length=25)
    
    def __unicode(self):
        return self.internal_department
    
class Station(models.Model):
    station_name = models.CharField(max_length=25)
    station_territory = models.ForeignKey(Territory, null=True)
    station_notes = models.CharField(max_length=100, null=True, blank=True)
    
    def __unicode__(self):
        return self.station_name
    

class PersonTitle(models.Model):
    person_title = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.person_title
    

class Department(models.Model):
    department = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.department