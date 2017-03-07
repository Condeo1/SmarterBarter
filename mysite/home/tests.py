from django.test import TestCase
from home.models import Customer, CustomerService

class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(customerID = "00", firstName = "John", lastName = "Doe", userName = "Johnny", zipCode = 35904, email = "johndoe@yahoo.com", password = "Fire0", bio = "I love fish")
        Customer.objects.create(customerID = "01", firstName = "Jane", lastName = "Doe", userName = "Janey", zipCode = 35904, email = "janedoe@yahoo.com", password = "Water0", bio = "Some useless info")
        Customer.objects.create(customerID = "02", firstName = "Bob", lastName = "Smith", userName = "Bobby", zipCode = 35954, email = "bobsmith@gmail.com", password = "Earth0", bio = "What up broham!!!")
        Customer.objects.create(customerID = "03", firstName = "Alice", lastName = "Smith", userName = "Ali", zipCode = 31244, email = "alicesmith@hotmail.com", password = "Air0", bio = "I like the way I can jump through handles upwards.")                
    
    def test_customerNameIsJohn(self):
        cusZero = Customer.objects.get(customerID = "01")
        self.assertEqual(cusZero.firstName, "John")
        
    def test_differentCustomerAreNotTheSame(self):
        cusOne = Customer.objects.get(customerID = "01")
        cusThree = Customer.objects.get(customerID = "03")
        
        self.assertNotEqual(cusOne, cusThree)
        
    def test_customerUserNameIsBobby(self):
        cusZero = Customer.objects.get(customerID = "02")
        self.assertEqual(cusZero.userName, "Bobby")
        
    def test_customerBioWorks(self):
        cusZero = Customer.objects.get(customerID = "00")
        self.assertEqual(cusZero.bio, "I love fish")
    
    def test_customerNameIsJohn(self):
        cusZero = Customer.objects.get(customerID = "00")
        self.assertEqual(cusZero.password, "Fire0")
        
class CustomererviceTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(customerID = "00", firstName = "John", lastName = "Doe", userName = "Johnny", zipCode = 35904, email = "johndoe@yahoo.com", password = "Fire0", bio = "I love fish")
        CustomerService.objects.create(customer = Customer.objects.get(customerID = "00"), servicesID = "00", needsID = "01")
        
    def test_CustomerServiceOneIsCustomerOne(self):
        cusZero = CustomerService.objects.get(customer = Customer.objects.get(customerID = "00"))
        self.assertEqual(cusZero.customer.firstName, "John")
        
    def test_customerOneOffersServiceZero(self):
        cusZero = CustomerService.objects.get(customer = Customer.objects.get(customerID = "00"))
        self.assertEqual(cusZero.servicesID, "00")
        
    def test_addServiceToCustomerZero(self):
        newService = "02"
        cusZero = CustomerService.objects.get(customer = Customer.objects.get(customerID = "00"))
        cusZero.servicesID += "," + newService
        cusZero.save()
        idArray = cusZero.servicesID.split(",")
        for i in range(0, len(idArray)):
            if(idArray[i] == newService):
                selectedService = idArray[i]
        self.assertEqual(selectedService, "02")
        self.assertEqual(cusZero.servicesID, "00,02")
        
    #def test_databasePreservesTheDataAcrossTests(self):
     #   cusZero = CustomerService.objects.get(Customer = Customer.objects.get(customerID = "00"))
      #  self.assertEqual(cusZero.servicesID, "00,02")

    def test_removeServiceFromCustomerOne(self):
        serviceToRemove = "00"
        newService = "02"
        cusZero = CustomerService.objects.get(customer = Customer.objects.get(customerID = "00"))
        cusZero.servicesID += "," + newService
        self.assertEqual(cusZero.servicesID, "00,02")
        idArray = cusZero.servicesID.split(",")
        idArray.remove(serviceToRemove)
        cusZero.servicesID = ""
        for i in range(0, len(idArray)):
            cusZero.servicesID += idArray[i]
        self.assertEqual(cusZero.servicesID, "02")