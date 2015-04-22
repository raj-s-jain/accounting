from django.db import models
import datetime
from django.utils import timezone

class Client(models.Model):

    client_name = models.CharField(max_length=90,blank=False)
    email = models.EmailField(max_length=90,blank=False)
    company_info= models.CharField(max_length=90,blank=False)
    def __unicode__(self):
		return self.client_name

class Project(models.Model):
	client = models.ForeignKey(Client,null=True)
	project_name=models.CharField(max_length=90,blank=False)
	tech_used=models.CharField(max_length=90,blank=False)
	time_spent=models.FloatField(default=0.0,blank=False)
	start_date=models.DateTimeField(default=datetime.datetime.now(),blank=False)
	cost_per_hour=models.FloatField(default=0.0,blank=False)

	def __unicode__(self):
		return self.project_name

class UpdatedTime(models.Model):
	project=models.ForeignKey(Project,null=True)
	last_updated=models.DateTimeField(default=datetime.datetime.now(),blank=False)
	time_spent=models.FloatField(default=0.0,blank=False)

	# def __unicode__(self):
	# 	return self.last_updated
# Create your models here.
