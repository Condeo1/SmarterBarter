from django.test import TestCase
from home.models import Customers, CustomerServices

class CustomerTestCase(TestCase):
    def setUp(self):
        Customers.objects.create(customerID = "00", firstName = "John", lastName = "Doe",
                                zipCode = 35904, email = "johndoe@yahoo.com")
        Customers.objects.create(customerID = "01", firstName = "Jane", lastName = "Doe",
                                zipCode = 35904, email = "janedoe@yahoo.com")
        Customers.objects.create(customerID = "02", firstName = "Bob", lastName = "Smith",
                                zipCode = 35954, email = "bobsmith@gmail.com")
        Customers.objects.create(customerID = "03", firstName = "Alice", lastName = "Smith",
                                zipCode = 31244, email = "alicesmith@hotmail.com")                
    
    def test_customerNameIsJohn(self):
        cusZero = Customers.objects.get(customerID = "00")
        self.assertEqual(cusZero.firstName, "John")
        
    def test_differentCustomersAreNotTheSame(self):
        cusOne = Customers.objects.get(customerID = "01")
        cusThree = Customers.objects.get(customerID = "03")
        
        self.assertNotEqual(cusOne, cusThree)
        
class CustomerServicesTestCase(TestCase):
    def setUp(self):
        Customers.objects.create(customerID = "00", firstName = "John", lastName = "Doe",
                                zipCode = 35904, email = "johndoe@yahoo.com")
        CustomerServices.objects.create(customers = Customers.objects.get(customerID = "00"), servicesID = "00", needsID = "01")
        
    def test_customerServicesOneIsCustomerOne(self):
        cusZero = CustomerServices.objects.get(customers = Customers.objects.get(customerID = "00"))
        self.assertEqual(cusZero.customers.firstName, "John")
        
    def test_customerOneOffersServiceZero(self):
        cusZero = CustomerServices.objects.get(customers = Customers.objects.get(customerID = "00"))
        self.assertEqual(cusZero.servicesID, "00")