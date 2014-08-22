from django.shortcuts import render
from django.shortcuts import render_to_response
# from django.template import loader,Context
from django.http import HttpResponse
import json
from models import Account

def  index(req):
	return render_to_response('index.html')

def acc(req,page):
	acc_list = Account.objects.all()
	test_acc_list = acc_list[0:5]
	response_data = {'accounts': test_acc_list}
	return HttpResponse(json.dumps(response_data), content_type="application/json")