import collections
import statistics
import copy

data = []
n = int(input("Enter no. of inputs: "))

for i in range(0,n):
	inp = int(input("Enter input %d: " % (i+1))) 
	data.append(inp)
no_of_clusters = int(input("Enter no. of clusters: "))
d = collections.OrderedDict()

for i in range(0,no_of_clusters):
	c = int(input("Enter c%d: " % (i+1)))
	d[c] = []

new_mean = [0 for i in range(0,no_of_clusters)]
old_mean = [1 for i in range(0,no_of_clusters)]

while new_mean != old_mean:
	for i in d.keys():
		d[i] = []
	for i in data:
		minimum = 999999
		index = 0
		for j in d.keys():
			temp = abs(j-i)
			if temp < minimum:
				minimum = temp
				index = j
		d[index].append(i)
	old_mean = copy.deepcopy(new_mean)
	k = 0
	for j in d.keys():
		new_mean[k] = statistics.mean(d[j]) 
		k += 1
	print(old_mean)	
	print(new_mean)
	print()

k = 1
for i in d.keys():
	print("Cluster %d: " % (k),end="")
	print(d[i])
	k += 1
OUTPUT:

himanshu@DESKTOP-87GKBN0:/mnt/c/Sem 6/DWM/KMEANS$ python3 kmeans.py
Enter no. of inputs: 9
Enter input 1: 1
Enter input 2: 2
Enter input 3: 6
Enter input 4: 7
Enter input 5: 8
Enter input 6: 10
Enter input 7: 15
Enter input 8: 17
Enter input 9: 20
Enter no. of clusters: 2
Enter c1: 7
Enter c2: 15
[0, 0]
[5.666666666666667, 17.333333333333332]

[5.666666666666667, 17.333333333333332]
[5.666666666666667, 17.333333333333332]

Cluster 1: [1, 2, 6, 7, 8, 10]
Cluster 2: [15, 17, 20]
