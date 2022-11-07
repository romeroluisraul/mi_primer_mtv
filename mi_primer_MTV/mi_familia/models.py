from django.db import models

class Person(models.Model):

    MARITAL_STATUS_CHOICES = [('S', 'Single'),
                              ('M','Married'),
                              ('W','widowed'),
                              ('D', 'divorced')]

    f_name = models.CharField(max_length = 30)
    l_name = models.CharField(max_length = 50)
    birth_date = models.DateField()
    marital_status = models.CharField(max_length=1, choices= MARITAL_STATUS_CHOICES)
    alive = models.BooleanField()
    death_date = models.DateField()

