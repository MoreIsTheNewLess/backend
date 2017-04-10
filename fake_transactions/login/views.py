from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import urllib.request, json

# Create your views here.from django.shortcuts import render

# class login(APIView):
#     def get(self, request, *args, **kw):
#         d = getToken(request.GET.get("username"),request.GET.get("password"))
#         return Response(d, status=status.HTTP_200_OK)
#
# def auth_url(username, password):
#     return "https://corporateapiprojectwar.mybluemix.net/corporate_banking/mybank/authenticate_client?client_id={0}&password={1}".format(username, password)
#
# def getToken(username, password) :
#
#     secret_url = auth_url(username, password)
#
#     with urllib.request.urlopen(secret_url) as url:
#             data = json.loads(url.read().decode())
#             return data[0]['token']
class fake_transactions(APIView):
    def get(self, request, *args, **kw):
        acc = getToken(request.GET.get("username"))
        return Response(acc, status=status.HTTP_200_OK)

def auth_URL(username, password):
    return "https://corporateapiprojectwar.mybluemix.net/corporate_banking/mybank/authenticate_client?client_id={0}&password={1}".format(username, password)

def getToken(username, password) :
    secret_url = auth_url(username, password)
    with urllib.request.urlopen(secret_url) as url:
        data = json.loads(url.read().decode())
        return data[0]['token']

# def get_accurl(username):
#     return "https://retailbanking.mybluemix.net/banking/icicibank/participantmapping?client_id={0}".format(username)
#
# def get_acc(username):
#     acc_url = get_accurl(username)
#     with urlib.request.urlopen(acc_url) as url:
#         acc = json.loads(url.read().decode())
#         return acc[0]['rohit.rk.rk1@gmail.com']
