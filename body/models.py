
from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    Name = models.CharField(max_length=30)
    FlagPicture = models.ImageField(upload_to='images/countryflag/')
     
    def __str__(self):
        return "%s " % (self.Name)

class UserRoles(models.Model):
    Role = models.CharField(max_length=30)
    def __str__(self):
        return "%s " % (self.Role)
    

class Currency(models.Model):
    CountryId = models.ForeignKey(Country, on_delete=models.CASCADE)
    RateToUsd = models.DecimalField(decimal_places=2, max_digits=1000000000000000)
    CurrencySymbol=models.CharField(max_length=5)
    def __str__(self):
        return "%s " % (self.CurrencySymbol)

class UnitsOfMeasurement(models.Model):
    UnitName = models.CharField(max_length=30)
    RatioToMetric = models.DecimalField(decimal_places=2,max_digits=100000000000)
    MesurementSymbol=models.CharField(max_length=5)
    def __str__(self):
        return "%s " % (self.UnitName)

class UserProfile(models.Model):
    userId= models.ForeignKey(User, on_delete=models.CASCADE)
    UserRoleId= models.ForeignKey(UserRoles, on_delete=models.CASCADE)
    Name=models.CharField(max_length=50)
    Surname=models.CharField(max_length=50)
    Cell = models.BigIntegerField()
    BirthDate = models.DateField()
 

    def __str__(self):
        return "%s " % (self.CompanyName)
class Merchants(models.Model):

    CompanyName=models.CharField(max_length=50)
    CompanyDescription=models.CharField(max_length=3000)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Email = models.EmailField(unique=True)
    Cell = models.BigIntegerField(unique=True)
    DateJoined = models.DateField()
    def __str__(self):
        return "%s " % (self.CompanyName)

class Category(models.Model):
    Name = models.CharField(max_length=30)
    RatioToMetric = models.DecimalField(decimal_places=2,max_digits=100000000000)
    PictureUrl=models.ImageField(upload_to='catagory/images/')
    ReOrderNumber=models.CharField(max_length=5)
    def __str__(self):
        return "%s " % (self.Name)

class Products(models.Model):
    Name = models.CharField(max_length=30)
    Description = models.CharField(max_length=3000)
    MerchantId= models.ForeignKey(Merchants, on_delete=models.CASCADE)
    CategoryId= models.ForeignKey(Category, on_delete=models.CASCADE)
    ProductCode = models.CharField(max_length=200)
    UnitsInStock = models.IntegerField()
    UnitsOnOrder=models.IntegerField()
    UnitsInStock_UnitsInStock= models.ForeignKey(UnitsOfMeasurement, on_delete=models.CASCADE)
    PictureUrl=models.ImageField(upload_to=f'products/images/')
    ReOrderNumber=models.CharField(max_length=5)
    Tax = models.DecimalField(decimal_places=2,max_digits=100000000000)
    TaxExclPrice= models.DecimalField(decimal_places=2,max_digits=100000000000)

    def __str__(self):
        return "%s " % (self.Name, self.SellPriceTaxExcl)

class Farm(models.Model):
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    
    def __str__(self):
        return "%s " % (self.Name)
class Field(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    AreaInUnits=models.DecimalField(decimal_places=3,max_digits=100000000000)
    UnitsOfMesurmentId_Area=models.ForeignKey(UnitsOfMeasurement, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    FarmId =models.ForeignKey(Farm, on_delete=models.CASCADE)
    def __str__(self):
        return "%s " % (self.Name)

class FieldDetails(models.Model):
    FieldId = models.ForeignKey(Field, on_delete=models.CASCADE)
    CatagoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
    ProductId =models.ForeignKey(Products, on_delete=models.CASCADE)
    UnitsOfMesurmentId_Area=models.ForeignKey(UnitsOfMeasurement, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    FarmId =models.ForeignKey(Farm, on_delete=models.CASCADE)
    def __str__(self):
        return "%s " % (self.Name)

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title