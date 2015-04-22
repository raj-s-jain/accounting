from django.contrib import admin

from .models import Client, Project


#class ProjectInline(admin.TabularInline):
	#model=Project
	#extra=1

class ClientAdmin(admin.ModelAdmin):
	model = Project
	fields = ['client_name','email','company_info']
	#inlines=[ProjectInline]


admin.site.register(Client, ClientAdmin)

# Register your models here.
