from django.db import models

class Customer(models.Model):
    customerID = models.CharField(max_length = 7)
    firstName = models.CharField(max_length = 200)
    lastName = models.CharField(max_length = 200)
    userName = models.CharField(max_length = 200)
    zipCode = models.IntegerField(default = '55555')
    email = models.EmailField(max_length = 500)
    password = models.CharField(max_length = 20)
    bio = models.TextField(max_length = 1500)
    
    def __str__(self):
        return self.userName
    
class CustomerService(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    servicesID = models.CharField(max_length = 60)
    needsID = models.CharField(max_length = 60)
    
    def __str__(self):
        return self.customer.userName

class Login(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.customer.userName

    

