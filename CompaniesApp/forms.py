"""
CompaniesApp Forms

Created by Jacob Dunbar on 10/3/2016.
"""
from django import forms
from .models import Engineer, Company

class CompanyForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    photo = forms.ImageField(label='Photo')
    description = forms.CharField(label='Description', max_length=300)
    website = forms.CharField(label='Website', max_length = 300)

class EngineerForm(forms.Form):
	company = forms.ModelChoiceField(queryset=Company.objects.all())
	alma_mater = forms.CharField(label='Alma Mater', max_length=50)
	about = forms.CharField(label='About', max_length=300)
	phone_number = forms.CharField(label='Phone Number', max_length=20)

class UpdateEngineerForm(forms.ModelForm):
	class Meta:
		model = Engineer
		fields = ('company', 'alma_mater', 'about', 'phone_number')
