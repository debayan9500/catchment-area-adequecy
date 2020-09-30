import numpy as np
lst=[]
a =  int(input("how many input :" ))
h = int (input("Enter error estimaton : "))
for i in range (0,a):
    print(" enter rainfal data ",i+1)
    ele = float (input())
    lst.append(ele)
b = np.sum(lst)
p = (b/a)
f = np.array(lst)
c = (f-p)
d = c*c
x = np.sum(d)
e = x/(a-1)
sig = np.sqrt(e)
cv = (100*sig/p)
n = (cv/h)*(cv/h)
print("Cv = " , cv)
print("sigma : ", sig )

print("Number of station required in this catchment: ",int(n-a+1))
print("Optimum number of station in this catchment:", int(n+1))

X = input('Press enter to continue')
print (X)