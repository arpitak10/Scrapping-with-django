from http.client import HTTPResponse
from urllib import response
from django.shortcuts import render
from .models import Quotes
import json
import requests
from myapp.models import Quotes
from . import api_test
def index(request):
    #quo = api_test.q 
    #auth = api_test.a
    #obj = Quotes(Quoation = quo,Author = auth) 
    #obj.save()
    return render(request,'index.html')













 






















#def test(request):
    #url = "https://type.fit/api/quotes"
    #resp = requests.get(url)
    #data = resp.json()
    #for i in range(-1,-6,-1):
     #   print(data[i])
    #    obj =  Quotes(Quoation =data[i]['text'],Author=data[i]['author'])
    #    obj.save()
    #return render(request,'index.html')
    #return HTTPResponse({"result": "OK"})
#def test(request):
 #   pass
  #  url = "https://type.fit/api/quotes"
   # req = Request(url,headers={'User-Agent': 'Mozilla/5.0'})
   # response = urlopen(req).read()
   # data_json = json.loads(response.decode('utf-8'))
   # for i,j in data_json.items():
   #     print(i,j)

        #obj = Quotes(Quoation =i,Author=j)
        #obj.save()
    #return HTTPResponse({"result": "OK"})
