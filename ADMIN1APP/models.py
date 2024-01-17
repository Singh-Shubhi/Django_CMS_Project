from django.db import models



# Create your models here.
class Employee1(models.Model):
    status_option = (("Active","Active"),("Inactive","Inactive"))
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    status = models.CharField(max_length=20,choices=status_option)

    def __str__(self):
        return self.email
    
class Product1(models.Model):
    product_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='media')
    product_price = models.DecimalField(default=0,max_digits=50,decimal_places=2)
    entered_by = models.ForeignKey(Employee1, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
    
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialisation = models.CharField(max_length=200)
    contact_number = models.BigIntegerField()
    location = models.CharField(max_length=100)
    entered_by = models.ForeignKey(Employee1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date_of_schedule = models.DateField()
    time_of_schedule = models.TimeField()
    entered_by = models.ForeignKey(Employee1,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.doctor} - {self.date_of_schedule} - {self.time_of_schedule}"
    
    
class Deal(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    product_name1 = models.ForeignKey(Product1,on_delete=models.CASCADE)
    quantity_ordered = models.IntegerField()
    entered_by = models.ForeignKey(Employee1,on_delete=models.CASCADE)




# admin password 
# project 
# project123