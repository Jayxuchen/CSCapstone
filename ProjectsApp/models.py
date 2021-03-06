"""ProjectsApp Models

Created by Harris Christiansen on 10/02/16.
"""
from django.db import models
from AuthenticationApp.models import MyUser

class Project(models.Model):
    name = models.CharField(max_length=200)
    website = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=10000)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')
    members = models.ManyToManyField(MyUser)
    language = models.CharField(max_length=200, null=True)
    experience = models.IntegerField(null=True)
    specialty = models.CharField(max_length=200, null=True)

    # TODO Task 3.5: Add field for company relationship
    # TODO Task 3.5: Add fields for project qualifications (minimum required: programming language, years of experience, speciality)

    def __str__(self):
        return self.name
