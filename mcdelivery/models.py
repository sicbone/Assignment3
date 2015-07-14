from django.db import models

# Create your models here.
class Order(models.Model):
    customer = models.CharField(max_length=50)
    order = models.TextField(max_length=255)
    special_request = models.CharField(max_length=50)
    contact_number = models.IntegerField(max_length=10)
    address = models.CharField(max_length=50)
   
    def __unicode__(self):
        return self.customer