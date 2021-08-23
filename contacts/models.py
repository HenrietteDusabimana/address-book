from django.db import models

# Create your models here.
class Contacts(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.fullname
        

    @property
    def fullname(self):
        return "%s %s" % (self.first_name, self.last_name)

        