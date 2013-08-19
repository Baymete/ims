from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import datetime


class Item(models.Model):
    serial_number = models.CharField(max_length=50)
    item_number = models.CharField(max_length=50, blank=True)
    asset_number = models.CharField(max_length=10, blank=True)
    entry_date = models.DateField() # Add by signal
    invoice_date = models.DateField(null=True, blank=True)
    invoice_number =models.CharField(max_length=20, blank=True)
    po_number = models.CharField(max_length=20, blank=True)
    warranty_status = models.BooleanField()
    warranty_until = models.DateField(null=True, blank=True)
    current_owner = models.ForeignKey(User)
    notes = models.TextField(blank=True)
    
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
    personnel = models.ForeignKey(Personnel)

    def __unicode__(self):
        return self.territory



