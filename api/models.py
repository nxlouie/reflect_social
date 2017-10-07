from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        """human readable name"""
        return self.first_name + " " + self.last_name


class Interaction(models.Model):
    time = models.DateTimeField(auto_now=True)
    note = models.TextField(max_length=500)
    contacts = models.ManyToManyField(Contact)

    def __str__(self):
        return self.time + " " + str(self.contacts)