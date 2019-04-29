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