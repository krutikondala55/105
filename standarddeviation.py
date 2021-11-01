import csv
import math

with open('data.csv',newline='')as f:
     reader=csv.reader(f)
     fileData=list(reader)

data=fileData[0]

def mean(data):
    n=len(data)
    total=0
    for k in data:
        total=total+int(k)
    mean=total/n
    print(mean)
    return mean 

squaredlist=[]
for j in data:
    a=int(j)-mean(data)
    a=a**2
    squaredlist.append(a)

sum=0
for t in squaredlist:
    sum=sum+t

result=sum/(len(data)-1)
standarddeviation=math.sqrt(result)
print(standarddeviation)