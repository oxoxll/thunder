from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.utils import simplejson
#import json
from models import Account
from django.forms.models import model_to_dict

def  index(req):
	return render_to_response('index.html')

def acc(req,page):
	acc_list = Account.objects.all()
	test_acc_list = acc_list[0:5]
	results = [ob.as_json() for ob in test_acc_list]
	response_data = {'accounts': results}
	return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
