from django.db import models


class DigitalForensicHub(models.Model):
    name = models.CharField(max_length=50)
    submissions_authorised = models.IntegerField(default=0)
    submissions_pending = models.IntegerField(default=0)
    submissions_processing = models.IntegerField(default=0)
    submissions_holding = models.IntegerField(default=0)
    submissions_completed = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Practitioner(models.Model):
    rank = models.CharField(max_length=10, default='PSE')
    force_number = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.rank} {self.force_number} {self.last_name}'
