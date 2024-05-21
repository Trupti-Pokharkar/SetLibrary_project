from django.db import models

# Create your models here.

class Library(models.Model):
    name = models.CharField(max_length=100, verbose_name="Book Name")
    author = models.CharField(max_length=100, verbose_name="Book Author")
    publisher = models.CharField(max_length=100, verbose_name="Publisher")
    publication = models.IntegerField(verbose_name="Publication")  
    pages = models.IntegerField(verbose_name="Number of pages")  
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")

    def __str__(self):
        return str(self.id)

class Student(models.Model):
    stuid=models.IntegerField(verbose_name="Student Id")
    name=models.CharField(max_length=100,verbose_name="Student Name")
    book=models.IntegerField(verbose_name="Issued Book Id")
    date= models.DateField(verbose_name="Issued Date")
    rdate = models.DateField(verbose_name="Reserved Date")

    def __str__(self):
        return str(self.id)

class Emp(models.Model):
    empid=models.IntegerField(verbose_name="Empolyee id")
    name=models.CharField(max_length=100,verbose_name="Employee Name")
    email=models.EmailField(max_length=100,verbose_name="Email")
    Mob =models.CharField(max_length=100,verbose_name="Mobile Number")
    pos=models.CharField(max_length=100,verbose_name="Position")

    def __str__(self):
        return str(self.id)


