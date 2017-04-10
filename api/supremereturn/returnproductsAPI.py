import csv
datafile = open(r'C:\Users\sskaushik\Desktop\hoolixyz\productsdata.csv', 'r')
datareader = csv.reader(datafile,delimiter=';')
data = []
for row in datareader:
    data.append(row)    
print (data[1:300])
		
