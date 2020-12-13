from django.db import models

class Product(models.Model):
        name = models.CharField(max_length = 80)
        description = models.CharField(max_length = 100)
        price = models.DecimalField(max_digits = 9, decimal_places = 2)
        quantity = models.IntegerField()

        def __str__(self):
            return self.description


class Client(models.Model):
    name = models.CharField(max_length = 60)
    telephone = models.IntegerField()
    email = models.CharField(max_length = 120)
    password = models.CharField(max_length = 220)

    def __str__(self):
        return self.name +'---\n'+self.email


class Contact_Us(models.Model):
    name = models.CharField(max_length = 80)
    telephone = models.IntegerField()
    email = models.CharField(max_length = 220)
    subject = models.CharField(max_length = 120)
    message = models.TextField()

    def __str__(self):
        return self.name + '------'+ self.subject
