from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    owner = models.ForeignKey('auth.User',
                              related_name='contacts',
                              on_delete=models.CASCADE)

    def __str__(self):
        """human readable name"""
        return self.first_name + " " + self.last_name


class InteractionTag(models.Model):
    TYPES = (
        (1, 'Career'),
        (2, 'Social'),
        (3, 'Family'),
        (4, 'Dating'),
        (5, 'Obligation'),
        (6, 'Worthwhile'),
        (7, 'Time Waste'),
    )
    tag_name = models.IntegerField(choices=TYPES, primary_key=True)

    def __str__(self):
        return self.get_tag_name_display()


class Interaction(models.Model):
    time = models.DateTimeField(auto_now=True)
    note = models.TextField(max_length=500)
    contacts = models.ManyToManyField(Contact)
    tags = models.ManyToManyField(InteractionTag)
    owner = models.ForeignKey('auth.User',
                              related_name='interactions',
                              on_delete=models.CASCADE)

    def __str__(self):
        return self.time + " " + str(self.contacts) + " " + self.tags


# receiver handles token creation immediately when a user is created
@receiver(post_save, sender=User)
def created_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

