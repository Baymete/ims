from django.db import models


class Item(models.Model):
    serial_number = models.CharField(max_length=50)
    item_number = models.CharField(max_length=50)
    asset_number = models.CharField(max_length=10)
    entry_date = models.DateField()
    invoice_date = models.DateField()
    invoice_number =models.CharField(max_length=20)
    po_number = models.CharField(max_length=20)
    warranty_status = models.BooleanField()
    warranty_until = models.DateField()
    current_owner = models.ForeignKey('Personnel')

    def __unicode__(self):
        return self.serial_number


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
