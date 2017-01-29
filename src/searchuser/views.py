from django.shortcuts import render
import requests

from .serializers import DataSerializer,ReportSerializer
from .models import userSearch,queryReport
from django.utils import timezone
from datetime import date, timedelta
# Create your views here.
def search(request):
	query = request.GET.get("q")
	context_data={}
	if(query):
		r= requests.get('https://api.github.com/users/'+query)
		serializer1 = ReportSerializer(data={'requested':query})
		if(serializer1.is_valid()):
			serializer1.save()
		json = r.json()
		if len(json)>2 :
			context_data = {'title':'Search Completed'}
			try:
				check_id=json['id']
				obj=userSearch.objects.get(id=check_id)
				serializer = DataSerializer(obj,data=json)
			except userSearch.DoesNotExist:
				obj= None
				serializer = DataSerializer(data=json)
				#print serializer
			if(serializer.is_valid()):
				serializer.save()
				#print userSearch.objects.filter(timestamp.date() = today).count()
			else:
				print 'error'
		else:
			context_data={'title':'Not Valid please search other'}
	return render(request,"search.html",context_data)

def report(request):
	today=timezone.now().date()
	w=today-timedelta(days=7)
	m=today-timedelta(days=30)

	#USED PUBLISH TO CHECK THE REPORT , USE TIMSTAMP IN PLACE OF PUBLISH TO GET CORRECT DATA 

	count_user_today=userSearch.objects.filter(publish=today).count
	count_user_week=userSearch.objects.filter(publish__gte=w).count
	count_user_month=userSearch.objects.filter(publish__gte=m).count
	count_request_today = queryReport.objects.filter(timestamp=today).count
	count_request_week=queryReport.objects.filter(timestamp__gte=w).count
	count_request_month=queryReport.objects.filter(timestamp__gte=m).count
	context_data={'count_user_today':count_user_today,
	'count_user_week':count_user_week,
	'count_user_month':count_user_month,
	'count_request_today':count_request_today,
	'count_request_month':count_request_month,
	'count_request_week':count_request_week
	}
	return render(request,"report.html",context_data)