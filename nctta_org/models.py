from django.db import models
from django.contrib.auth.models import User

"""
Players can be parsed from the spreadsheet
- all a player needs to be is a rating and maybe a link to a profile

Profile
- could put player info in the profile
- fname, lname, email, user
- picture
- school
- image

School
- name
- image
- location
- active
- division
- captain (FK to profile)

Division
- name
- location?
- director (FK to profile)
- region

Region
- name
- location?
- director?

"""

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.ForeignKey("College", blank=True, null=True)
    is_captain = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.user)

class College(models.Model):
    long_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.short_name
