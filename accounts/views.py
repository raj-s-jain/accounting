from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from .models import Client,Project,UpdatedTime
from .forms import ClientForm,ProjectForm,ProjectForm2,DateForm
import datetime
from django.utils import timezone
from datetime import timedelta


def index(request):
	
	client_list=Client.objects.all()
	template = loader.get_template('accounts/index.html')
	context= RequestContext(request, {'client_list':client_list, })
	
	return HttpResponse(template.render(context))

def client(request,client_id):
	
	try:
		client=Client.objects.get(pk=client_id)
	except Client.DoesNotExist:
		raise Http404("Client does not exist")
	return HttpResponse("You are looking at client %s"%client_id)



def detail(request,client_id):
	client=Client.objects.get(pk=client_id)
	#project=client.project_set.get(pk=project_id)
	return HttpResponse(render(request, 'accounts/detail.html',dict(client=client,)))


def addclient(request):
	if request.method == 'POST':

		form = ClientForm(request.POST)
		if form.is_valid():
			new_client = form.save()
			return HttpResponse(render(request, 'accounts/addclient.html',dict(form=form)))
	else:
		form = ClientForm()
		return HttpResponse(render(request, 'accounts/addclient.html',dict(form=form)))

    
	

def addproject(request,client_id):
	test="add project"
	#ProjectFormSet=inlineformset_factory(Client,Project,form=ProjectForm)
	if request.method == 'POST':
		test="POST"
		client=Client.objects.get(pk=client_id)
		form = ProjectForm(request.POST)
		if form.is_valid():
			test="VALID"
			client.save()
			project = form.save(commit=False)
			project.client = client
			project.save()
			timespent=project.time_spent
			current_time = timezone.now()
			UpdatedTime.objects.create(project=project, last_updated=current_time, time_spent=timespent)
			return HttpResponse(render(request, 'accounts/addproject.html',dict(client=client,form=form,test=test)))
	else:		
		test="ELSE"
		client=Client.objects.get(pk=client_id)
		form = ProjectForm()
		return HttpResponse(render(request, 'accounts/addproject.html',dict(client=client,form=form,test=test)))

	
def projectdetails(request,client_id,project_id):
	client=Client.objects.get(pk=client_id)
	project=client.project_set.get(pk=project_id)
	form=ProjectForm(request.POST,instance=project)

	# dt=datetime.datetime.today() - project.start_date
	# if dt.days>30:
	# 	months=(dt.days/30)
	# else:
	# 	months=1
	if request.method == "POST":
		test="POST"
		if form.is_valid():
			test="VALID"
			client.save()
			project=form.save(commit=False)
			project.client=client
			timespent=project.time_spent
			project.save()
			current_time = timezone.now()
			UpdatedTime.objects.create(project=project, last_updated=current_time, time_spent=timespent)
			totalcost=(project.time_spent*project.cost_per_hour)
			
			client=Client.objects.get(pk=client_id)
			project=Project.objects.get(pk=project_id)
			time=UpdatedTime.objects.all().filter(project=project)
			for t in time:
				print(t.last_updated)
			return HttpResponse(render(request,'accounts/projectdetails.html',dict(client=client,project=project,form=form,test=test,totalcost=totalcost,)))
	test="ELSE"
	form= ProjectForm(instance=project)
	totalcost=(project.time_spent*project.cost_per_hour)
	
	current_time = datetime.datetime.now()
	
	return HttpResponse(render(request,'accounts/projectdetails.html',dict(client=client,project=project,form=form,test=test,totalcost=totalcost)))
	

# def coststat(request,client_id,project_id):
# 	client=Client.objects.get(pk=client_id)
# 	project=client.project_set.get(pk=project_id)
# 	#dt=datetime.date.today() - project.start_date
# 	#print dt.days
# 	return HttpResponse(render(request,'accounts/coststat.html',dict(client=client,project=project,)))


def report(request,client_id,project_id):
	client=Client.objects.get(pk=client_id)
	project=Project.objects.get(pk=project_id)
	time=UpdatedTime.objects.all().filter(project=project)
	cost=project.cost_per_hour
	
	test="INITIAL"
	# for t in time:
	#  	print(t.last_updated)
	if request.method == "POST":
		form = DateForm(request.POST)
		test="POST"
		if form.is_valid():
			test="VALID"
			from_date=form.cleaned_data['from_date']
			to_date=form.cleaned_data['to_date']
			diffdate = to_date - from_date
			diff_days= diffdate.days
			

			newtime=UpdatedTime.objects.all().filter(project=project,last_updated__gte=from_date, last_updated__lte=to_date)
			totaltimespent=0
			for t in newtime:
				totaltimespent=totaltimespent+t.time_spent
			totalearned=totaltimespent*cost
			if(diff_days>0):
				earnperday=totalearned/diff_days
			return HttpResponse(render(request,'accounts/report.html',dict(client=client,project=project,form=form,from_date=from_date,to_date=to_date,test=test,newtime=newtime,totaltimespent=totaltimespent,totalearned=totalearned,diff_days=diff_days,earnperday=earnperday)))
	form = DateForm(request.POST)
	return HttpResponse(render(request,'accounts/report.html',dict(client=client,project=project,form=form,test=test,cost=cost)))

	











# Create your views here.
