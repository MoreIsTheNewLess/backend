from django.shortcuts import render

import urllib.request, json

# Create your views here.
def index(request) :
    return request

def auth_url(username, password):
    return "https://corporateapiprojectwar.mybluemix.net/corporate_banking/mybank/authenticate_client?client_id={0}&password={1}".format(username, password)

def getToken(username, password) :

    secret_url = auth_url(username, password)

    with urllib.request.urlopen(secret_url) as url:
            data = json.loads(url.read().decode())
            return data
