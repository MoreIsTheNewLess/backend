from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100.)
data = [[29,12,2016],[18,10,2017],[22,3,2017]]
target = [1,2,3]
clf.fit(data,target)
while 1:
    test = []
    print("enter ")
    a,b,c = map(int, input().split())
    test.append(a)
    test.append(b)
    test.append(c)
    predict = []
    predict.append(test)
    print("the prediction is ")
    print(clf.predict(predict))
