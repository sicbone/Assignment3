from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Order(models.Model):
    customer = models.CharField(max_length=50)
    order = models.TextField(max_length=255)
    special_request = models.CharField(max_length=50)
    contact_number = models.IntegerField(max_length=10)
    address = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
   
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk":self.pk})
   
    def __str__(self):
        return self.customer