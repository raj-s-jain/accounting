from django import forms

from .models import Client,Project

from django.forms.models import inlineformset_factory

class ClientForm(forms.ModelForm):
	class Meta:
		model = Client
		fields= ['client_name','company_info','email',]

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields =['project_name','tech_used','time_spent','cost_per_hour','start_date',]

class ProjectForm2(forms.ModelForm):
	class Meta:
		model= Project
		fields=['time_spent',]

class DateForm(forms.Form):
	from_date= forms.DateTimeField(label="From Date")
	to_date= forms.DateTimeField(label="To Date")

ProjectFormSet=inlineformset_factory(Client,Project,extra=0,min_num=1,form=ProjectForm,can_delete=False)

TimeFormSet=inlineformset_factory(Client,Project,extra=0,max_num=1,form=ProjectForm,fields=('time_spent',),can_delete=False)
