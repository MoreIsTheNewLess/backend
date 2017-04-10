from django.shortcuts import render
import urllib.request, json

def authURL(username, password): #TODO : use one from login or get from frontend
    return "https://corporateapiprojectwar.mybluemix.net/corporate_banking/mybank/authenticate_client?client_id={0}&password={1}".format(username, password)

def getToken(username, password): #TODO: use one defined in login or get from frontend
    secret_url = authURL(username, password)

    with urllib.request.urlopen(secret_url) as url:
        data = json.loads(url.read().decode())
        return data[0]['token']

def accountInfoURL(username):
    return "https://retailbanking.mybluemix.net/banking/icicibank/participantmapping?client_id={}".format(username) #maybe better to use just + than format?

def getAccountNumber(username):
    secret_url = accountInfoURL(username)

    with urllib.request.urlopen(secret_url) as url:
        data = json.loads(url.read().decode())
    return data[0]['account_no']

def transactionInforURL(username, token):
    return "https://retailbanking.mybluemix.net/banking/icicibank/recenttransaction?client_id={0}&token={1}&accountno={2}".format(username, token, getAccountNumber(username))

def getTransactionHistory(username, password):
    token = getToken(username, password)
    secret_url = transactionInforURL(username, token)

    with urllib.request.urlopen(secret_url) as url:
        data = json.loads(url.read().decode())

    return data

def getTransactionHistoryRemarks(username, password):
    data = getTransactionHistory(username, password)

    remarks = []
    if data[0]['code'] != 200:
        return "ERROR"
    data = data[1:]
    for i in data:
        remarks.append(i['remark'])

    return remarks
