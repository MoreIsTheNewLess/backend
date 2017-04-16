from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import urllib.request, json
from sklearn import svm
from sklearn.model_selection import train_test_split
import csv
from . import trans_hist
import operator

clf = svm.SVC(gamma = 0.001, C = 100., probability = True)
data = []
target = []

test_data = []
test_target = []

prods = ['LB','AR','MW','ML','UX']

print("generating random test data...")
for c in range(len(prods)):
    prdt = prods[c]
    i = (c+1)*6

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
        secret_path = '/home/chinmaya/code/mnl/'  #NOTE: Change to the path of backend folder on your computer
        day = int(request.GET.get("day"))
        month = int(request.GET.get("month"))
        prob_prods = clf.predict_proba([day, month]).tolist()
        print(prob_prods)
        prod_names = dict()
        for i in range(len(prob_prods[0])):
            prod_names[prods[i]] = prob_prods[0][i]
        print(prod_names)
        prod_names = sorted(prod_names.items(), key=operator.itemgetter(1), reverse=True)
        prod_names = prod_names[:3]
        print(prod_names)

        categories = { 'UX' : 'Groceries', 'LB' : 'Electricity', 'ML' : 'Fuel','AR' : 'Groceries','MW' : 'Groceries' }

        prob_deals = []
        with open(secret_path + 'backend/api/supremereturn/SupremeDeals.csv', newline = '') as csvfile:
            deals = csv.reader(csvfile, delimiter = ',', quotechar = '|')
            for row in deals:
                for k,v in prod_names:
                    if row[0] == categories[k]:
                        temp = {}
                        temp["category"] = row[0]
                        temp["offer"] = row[1]
                        temp["product"] = row[2]
                        if row[2] == k:
                            temp["score"] = 0 
                        else:
                            temp["score"] = 1
                        prob_deals.append(temp)

        prob_deals.sort(key = lambda x: x["score"])
        prob_deals = prob_deals[:5]

        reminders = []
        for k,_ in prod_names:
            reminders.append(k)

        return Response({'Reminders' : reminders, 'Best Deals' : prob_deals}, status = status.HTTP_200_OK)
