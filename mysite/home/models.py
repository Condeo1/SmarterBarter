from django.db import models

class Customers(models.Model):
    customerID = models.CharField(max_length = 7)
    firstName = models.CharField(max_length = 200)
    lastName = models.CharField(max_length = 200)
    zipCode = models.IntegerField(default = 0)
    email = models.CharField(max_length = 500)
    
    def __str__(self):
        return self.firstName
    
class CustomerServices(models.Model):
    customers = models.ForeignKey(Customers, on_delete=models.CASCADE)
    servicesID = models.CharField(max_length = 60)
    needsID = models.CharField(max_length = 60)
    
    def __str__(self):
        return self.customers.firstName

class Login(models.Model):
    customers = models.ForeignKey(Customers, on_delete=models.CASCADE)
    userName = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.customers.firstName

    

