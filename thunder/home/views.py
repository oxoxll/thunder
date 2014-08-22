from django.shortcuts import render
from django.shortcuts import render_to_response
# from django.template import loader,Context
from django.http import HttpResponse
from django.utils import simplejson
from models import Account

def  index(req):
	return render_to_response('index.html')

def acc(req,page):
	acc_list = Account.objects.all()
	test_acc_list = acc_list[0:5]
	acc_str  = map(str, test_acc_list)
	return HttpResponse("<p>" + ' '.join(acc_str) + "</p>")

	# render_to_response('test.html',{'acc_list':test_acc_list})
	# acc_str = map(str,acc_list)
	# start_num=number*5
	# end_num=start_num+5
	# acc_response = acc[start_num:end_num]

	# return HttpResponse(simplejson.dumps(test_num))

