from django.db import models
from django import forms
# Create your models here.
class Device(models.Model): #tablename
    types = models.CharField(max_length = 100 , blank = False) #columname
    price = models.IntegerField()

    choices = (
        ('AVAIABLE','Item Ready To Be Purchased'),
        ('SOLD','Item is Sold'),
        ('RESTOCKING','Item Restocking in Few Days')
    )
    status = models.CharField(max_length = 100 , choices = choices, default = "SOLD") #Avaiable,sold,restocking
    issues = models.CharField(max_length = 100 , default = "NO issues")

    class Meta:
        abstract = True

    #ef _str_(self):
     #   return 'Types : {0} Price : {1}'.format(self.types,self.price)

class Laptop(Device):
    pass

class Desktop(Device):
    pass

class Mobile(Device):
    pass



#form
class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ['types','price','status','issues']

class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktop
        fields = ['types','price','status','issues']