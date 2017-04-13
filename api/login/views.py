from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import urllib.request, json

class login(APIView):
    def get(self, request, *args, **kw):
        d = getToken(request.GET.get("username"),request.GET.get("password"))

        if len(d) > 0:
            return Response(d, status=status.HTTP_200_OK)
        return Response(d, status=status.HTTP_401_UNAUTHORIZED)

def auth_url(username, password):
    return "https://corporateapiprojectwar.mybluemix.net/corporate_banking/mybank/authenticate_client?client_id={0}&password={1}".format(username, password)

def getToken(username, password) :

    secret_url = auth_url(username, password)

    with urllib.request.urlopen(secret_url) as url:
        data = json.loads(url.read().decode())
        return data[0]['token']
