from django.db import models

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
