from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import urllib.request, json

# Create your views here.from django.shortcuts import render

class fundTransfer(APIView):
    def get(self, request, *args, **kw):
        acc = getFundStatus(request.GET.get("username"), request.GET.get("password"), request.GET.get("sourceAcc"), request.GET.get("destAcc"), request.GET.get("amtPayed"))
        return Response(acc, status=status.HTTP_200_OK)

def auth_url(username, password):
    return "https://corporateapiprojectwar.mybluemix.net/corporate_banking/mybank/authenticate_client?client_id={0}&password={1}".format(username, password)

def getToken(username, password) :
    secret_url = auth_url(username, password)
    with urllib.request.urlopen(secret_url) as url:
        data = json.loads(url.read().decode())
        return data[0]['token']

def getFundTransferURL(username, password, sourceAcc, destAcc, amtPayed):
    token = getToken(username, password)
    return "https://retailbanking.mybluemix.net/banking/icicibank/fundTransfer?client_id={0}&token={1}&srcAccount={2}&destAccount={3}&amt={4}&payeeDesc=NA&payeeId=NA&type_of_transaction=fuel".format(username, token,sourceAcc,destAcc, amtPayed)

def getFundStatus(username, password, sourceAcc, destAcc, amtPayed):
    fundURL = getFundTransferURL(username, password, sourceAcc, destAcc, amtPayed)
    with urllib.request.urlopen(fundURL) as url:
        data = json.loads(url.read().decode())
        return data
