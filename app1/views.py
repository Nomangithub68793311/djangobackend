from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse 
from django.http import HttpResponse
from app1.models import team
from django.http import HttpResponse
from app1.serializers import Adddataserializer
import json
import requests
# Create your views here.
@csrf_exempt
def addalldata(request,id=0):
    if (request.method=='GET'):
        dataall=team.objects.all()
        data_ser=Adddataserializer(dataall,many=True)
        return JsonResponse(data_ser.data,safe=False)
    elif (request.method=='POST'):
        dataall=JSONParser().parse(request)
        data_ser=Adddataserializer(data=dataall)
        if data_ser.is_valid():
            data_ser.save()
            print(data_ser.data)
            return JsonResponse(data_ser.data,safe=False)
        return JsonResponse("failed")  

def check():
    return HttpResponse('checked')

def update_product(request,pk):
 
    if (request.method=='GET'):
        dataall=team.objects.get(id=pk)
        response = Adddataserializer(instance=dataall).data

        return JsonResponse(response,safe=False)

def delete_product(request,id):
   if request.method=='POST':
        dataall=team.objects.get(id=id)
        dataall.delete()
        return JsonResponse('deleted',safe=False )
    
def geT_product(request):
    # return HttpResponse("django listened")
            r = requests.get('http://localhost:5000/send_data_to_django')
            r_status = r.status_code
            print("code",r.json())
            # data=json.dumps(r)
            # return JsonResponse(data,safe=False)
            return JsonResponse(r.json())

            # if r_status == 200:
            #     data = r.json()
            #     print(data)


 
    