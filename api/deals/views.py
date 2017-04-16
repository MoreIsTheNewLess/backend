from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import urllib.request, json
from sklearn import svm
from sklearn.model_selection import train_test_split
import csv


clf = svm.SVC(gamma = 0.001, C = 100., probability = True)
data = []
target = []

test_data = []
test_target = []

print("generating random test data...")
for p in range(1,4):
    if p == 1:
        prdt = 'UX'
        i = 7
    elif p == 2:
        prdt = 'LB'
        i = 14
    elif p == 3:
        prdt = 'ML'
        i = 28
    for j in range(1,13):
        temp = [int(i), int(j)]
        if j % 2 == 0:
            data.append(temp)
            target.append(prdt)
        else:
            test_data.append(temp)
            test_target.append(prdt)
        temp = [int(i) + 1, int(j)]
        if j % 2 == 0:
            data.append(temp)
            target.append(prdt)
        else:
            test_data.append(temp)
            test_target.append(prdt)
        temp = [int(i) - 1, int(j)]
        if j % 2 == 0:
            data.append(temp)
            target.append(prdt)
        else:
            test_data.append(temp)
            test_target.append(prdt)

print("training...")
clf.fit(data,target)

print("testing...")
print(clf.score(test_data, test_target))

class deals(APIView):
    def get(self, request, *args, **kw):
        secret_path = 'Users\Siddharth Saha\Downloads\MoreIsTheNewLess'  #NOTE: Change to the path of backend folder on your computer
        day = int(request.GET.get("day"))
        month = int(request.GET.get("month"))
        BuyNLargeList = clf.predict_proba([day, month]).tolist()
        bestProduct = 0

        categories = { 'UX' : 'Groceries', 'LB' : 'Electricity', 'ML' : 'Fuel' }

        if BuyNLargeList[0][0] > BuyNLargeList[0][1] and BuyNLargeList[0][0] > BuyNLargeList[0][2]:#TODO: Better product matching
            bestProduct = 'ML'
        elif BuyNLargeList[0][1] > BuyNLargeList[0][2]:
            bestProduct = 'LB'
        else:
            bestProduct = 'UX'

        less = ''
        with open(secret_path + 'backend/api/supremereturn/SupremeDeals.csv', newline = '') as csvfile:
            deals = csv.reader(csvfile, delimiter = ',', quotechar = '|')
            for row in deals:
                if bestProduct in row[-1]:
                    less = row
                    break

        return Response(json.dumps({'Reminder!' : bestProduct, 'Best Deals' : less}), status = status.HTTP_200_OK)
