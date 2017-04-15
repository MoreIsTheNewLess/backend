from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import urllib.request, json
from sklearn import svm
from sklearn.model_selection import train_test_split



clf = svm.SVC(gamma=0.001, C=100.,probability=True)
data = []
target = []

test_data = []
test_target = []

print("generating random test data...")
for p in range(1,4):
    if p == 1:
        i = 7
    elif p == 2:
        i = 14
    elif p == 3:
        i = 28
    for j in range(1,13):
        temp = [int(i),int(j)]
        if j % 2 == 0:
            data.append(temp)
            target.append(int(p))
        else:
            test_data.append(temp)
            test_target.append(int(p))
        temp = [int(i) + 1,int(j)]
        if j % 2 == 0:
            data.append(temp)
            target.append(int(p))
        else:
            test_data.append(temp)
            test_target.append(int(p))
        temp = [int(i) - 1,int(j)]
        if j % 2 == 0:
            data.append(temp)
            target.append(int(p))
        else:
            test_data.append(temp)
            test_target.append(int(p))

print("training...")
clf.fit(data,target)

print("testing...")
print(clf.score(test_data, test_target))

class deals(APIView):
    def get(self, request, *args, **kw):
        d = int(request.GET.get("date"))
        m = int(request.GET.get("month"))
        l = clf.predict_proba([d,m]).tolist()
        return Response(json.dumps(l[:5]), status=status.HTTP_200_OK)
