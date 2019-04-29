import collections
import itertools

items = collections.OrderedDict()
item_list = []
# transactions = []
n = int(input("Enter no. of items: "))

for i in range(0,n):
	item = input("Input item %d: " % (i+1))
	item_list.append(item)
	items[item] = 0

n = int(input("Enter no. of transactions: "))
print("**PRESS ENTER TO MOVE TO THE NEXT TRANSACTION**")

transactions = [[] for i in range(0,n)]

for i in range(0,n):
	print("Enter t%d: " % (i+1))
	while True:
		item = input()
		if not item:
			break
		transactions[i].append(item)
		items[item] += 1

print(item_list)
print(items)
print(transactions)		

min_support = float(input("Enter min support in %: "))
min_confidence = int(input("Enter min confidence in %: "))

min_support = (min_support/100) * n
print(min_support)

combination = list(itertools.combinations(list(item_list),1))
l = [[] for i in range(0,6)]

for i in range(0,6):
	print("*******************")
	for j in combination:
		j = frozenset(j)
		count = 0
		print(j,end="  ")
		for t in transactions:
			if j <= frozenset(t):
				count += 1

		print(count)

		if(count < min_support and i == 0):
			item_list.remove(list(j)[0])
			print(item_list)
		if(count >= min_support):
			d = dict({j:count})
			l[i].append(d)

		print(l)

	combination = list(itertools.combinations(list(item_list),i+2))

	if not l[i]:
		index = i - 1
		break

for i in l[index]:
	print("***********")
	rule_count = 0
	rule = list(list(i.keys())[0])
	for t in transactions:
		if set(rule) <= set(t):
			rule_count += 1
	print(count)
	for j in range(1,len(rule)):
		combination = list(itertools.combinations(rule,j))
		for k in combination:
			count = 0
			print("For rule {0} -> {1}: ".format(set(k),set(rule)-set(k)),end="")
			for t in transactions:
				if set(k) <= set(t):
					count += 1
			confidence = (rule_count/count) * 100
			print(confidence,end="  ")

			if(confidence < min_confidence):
				print("RULE NOT SELECTED")
			else:
				print("***RULE SELECTED***")
OUTPUT:

himanshu@DESKTOP-87GKBN0:/mnt/c/Sem 6/DWM$ python3 apriori.py
Enter no. of items: 6
Input item 1: A
Input item 2: B
Input item 3: C
Input item 4: D
Input item 5: E
Input item 6: F
Enter no. of transactions: 4
**PRESS ENTER TO MOVE TO THE NEXT TRANSACTION**
Enter t1:
A
B
C

Enter t2:
A
C

Enter t3:
A
D

Enter t4:
B
E
F

['A', 'B', 'C', 'D', 'E', 'F']
OrderedDict([('A', 3), ('B', 2), ('C', 2), ('D', 1), ('E', 1), ('F', 1)])
[['A', 'B', 'C'], ['A', 'C'], ['A', 'D'], ['B', 'E', 'F']]
Enter min support in %: 50
Enter min confidence in %: 50
2.0
*******************
frozenset({'A'})  3
[[{frozenset({'A'}): 3}], [], [], [], [], []]
frozenset({'B'})  2
[[{frozenset({'A'}): 3}, {frozenset({'B'}): 2}], [], [], [], [], []]
frozenset({'C'})  2
[[{frozenset({'A'}): 3}, {frozenset({'B'}): 2}, {frozenset({'C'}): 2}], [], [], [], [], []]
frozenset({'D'})  1
['A', 'B', 'C', 'E', 'F']
[[{frozenset({'A'}): 3}, {frozenset({'B'}): 2}, {frozenset({'C'}): 2}], [], [], [], [], []]
frozenset({'E'})  1
['A', 'B', 'C', 'F']
[[{frozenset({'A'}): 3}, {frozenset({'B'}): 2}, {frozenset({'C'}): 2}], [], [], [], [], []]
frozenset({'F'})  1
['A', 'B', 'C']
[[{frozenset({'A'}): 3}, {frozenset({'B'}): 2}, {frozenset({'C'}): 2}], [], [], [], [], []]
*******************
frozenset({'B', 'A'})  1
[[{frozenset({'A'}): 3}, {frozenset({'B'}): 2}, {frozenset({'C'}): 2}], [], [], [], [], []]
frozenset({'C', 'A'})  2
[[{frozenset({'A'}): 3}, {frozenset({'B'}): 2}, {frozenset({'C'}): 2}], [{frozenset({'C', 'A'}): 2}], [], [], [], []]
frozenset({'B', 'C'})  1
[[{frozenset({'A'}): 3}, {frozenset({'B'}): 2}, {frozenset({'C'}): 2}], [{frozenset({'C', 'A'}): 2}], [], [], [], []]
*******************
frozenset({'B', 'C', 'A'})  1
[[{frozenset({'A'}): 3}, {frozenset({'B'}): 2}, {frozenset({'C'}): 2}], [{frozenset({'C', 'A'}): 2}], [], [], [], []]
***********
1
For rule {'C'} -> {'A'}: 100.0  ***RULE SELECTED***
For rule {'A'} -> {'C'}: 66.66666666666666  ***RULE SELECTED***
