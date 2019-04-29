import statistics

n  = int(input("Enter the no. of inputs: "))
x = []
y = []

for i in range(0,n):
	xi = int(input("Enter x%d: " % (i+1)))
	yi = int(input("Enter y%d: " % (i+1)))
	x.append(xi)
	y.append(yi)

xmean = statistics.mean(x)
ymean = statistics.mean(y)

xx = []
yy = []
xx2 = []
xy = []

for i in range(0,n):
	a = x[i] - xmean
	b = y[i] - ymean
	c = a ** 2
	d = a * b
	xx.append(a)
	yy.append(b)
	xx2.append(c)
	xy.append(d)

b1 = sum(xy)/sum(xx2)
b0 = ymean - b1 * xmean

xpred = int(input("Enter value of x for which y is to be predicted: "))

ypred = b0 + b1*xpred
print("Prediction is: %.2f" % (ypred))

OUTPUT:

himanshu@DESKTOP-87GKBN0:/mnt/c/Sem 6/DWM/regression$ python3 reg.py
Enter the no. of inputs: 5
Enter x1: 95
Enter y1: 85
Enter x2: 85
Enter y2: 95
Enter x3: 80
Enter y3: 70
Enter x4: 70
Enter y4: 65
Enter x5: 60
Enter y5: 70
Enter value of x for which y is to be predicted: 80
Prediction is: 78.29
