from django.shortcuts import render
import time
from django.http.response import HttpResponse
# Create your views here.
from django.views import View
from  datetime import datetime

class Templates_demo(View):
    def get(self, request):

        context = {
            'city':'北京',
            'data_list' : [ 'A','B' , 'C' , 'D'],
            'data_dict':{
                'name':'张三',
                'age':18,
                'gender':True,
            },
            'score': 59,
            'safe_data':'<a href="#"> safe模式下 我是有样子的！！</a>',
            'time':time.ctime(),
            'date':datetime.now()
        }
        return render(request,'jinja_2.html',context=context)