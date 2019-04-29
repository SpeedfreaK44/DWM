import math

class Node :
	def __init__(self,pname=None,data=None,next_node=[]) :
		self.pname=pname
		self.data=data	
		self.next_node=next_node
	
	def printf(self):
		print (self.pname)
		print (self.data)
		for i in range(len(self.next_node)):
			print (self.next_node[i])
	def setNextNode(self,val):
		self.next_node=val


	
HEAD=Node(None,None,None)
head=HEAD
listcat=['age','competition','type','profit','abc']

data=[['old', 'yes' ,'software',0],
	   ['old', 'no' ,'software',0],
	   ['old', 'no' ,'hardware',0],
	   ['mid', 'yes' ,'software',0],
	   ['mid', 'yes' ,'hardware',0],
	   ['mid', 'no' ,'hardware',1],
	   ['mid', 'no' ,'software',1],
	   ['new', 'yes' ,'software',1],
	   ['new', 'no' ,'hardware',1],
	   ['new', 'no' ,'software',1]]

def predict(array,start):
	for i in range(0,len(array)):
		for j in range(len(start.next_node)):
			if start.next_node[j].data==array[i]:
				start=start.next_node[j]
				for k in range(len(start.next_node)):
					if start.next_node[k].data=='0':
						return 0
					elif start.next_node[k].data=='1':
						return 1
				break

def printTree(start):
	if start.next_node==None:
		return
	else:
		for j in range(len(start.next_node)):
			print(start.next_node[j].data)
			printTree(start.next_node[j])

def maximum(array):
	if len(array)>1:
		tdata=array[0][1]
		pos=array[0][0]
		min=array[0][2]
		for i in range(1,len(array)):
			if array[i][2]>min:
				min=array[i][2]
				tdata=array[i][1]
				pos=array[i][0]
		return [pos,tdata,min]
	else:
		return array[0]

def addNode(start,string,list1,colNo):
	if start.next_node==None and start==head:
		start.data=string
		node_list=[]
		for i in range(len(getSubArgs(list1,colNo))):
			node_list.append(Node(string,getSubArgs(list1,colNo)[i],None))
		start.setNextNode(node_list)
	elif start.data==string:
		node_list=[]
		for i in range(len(getSubArgs(list1,colNo))):
			node_list.append(Node(string,str(getSubArgs(list1,colNo)[i]),None))
		start.setNextNode(node_list)
	elif start.next_node==None:
		return
	else:
		for i in range(len(start.next_node)):
			addNode(start.next_node[i],string,list1,colNo)

def getSubArgs(listdata,column):
	temp=[]
	check=0
	for i in range(len(listdata)):
		check=0
		if i==0:
			temp.append(listdata[i][column])
		for j in range(len(temp)):
			if temp[j]==listdata[i][column] :
				check=1
		if check==0:
			temp.append(listdata[i][column])
	return temp

def entropy(p,n):
	if p==0 or n==0 :
		return 0.0
	else:
		total=float(p+n)
		ptemp=float(p/total)
		ntemp=float(n/total)
		logp=float(ptemp*math.log(ptemp,2))
		logn=float(ntemp*math.log(ntemp,2))
		return float(-logp-logn)

def decisonTree(list1,string):
	gain=[]
	for i in range(0,len(list1[0])-1):
		p=0
		n=0
		I=0
		E=0
		pin=0
		nin=0
		G=0
		for j in range(len(list1)):
			if list1[j][len(list1[0])-1]==1:
				p=p+1
			else: 
				n=n+1
		I=entropy(p,n)
		for k in range(len(getSubArgs(list1,i))):
			pin=0
			nin=0
			for l in range(len(list1)):
				if list1[l][i]==getSubArgs(list1,i)[k] and list1[l][len(list1[0])-1]==1:
					pin+=1
				elif list1[l][i]==getSubArgs(list1,i)[k] and list1[l][len(list1[0])-1]==0:
					nin+=1
			E=E+float(float(pin+nin)/float(p+n))*entropy(pin,nin)
		G=float(I)-float(E)
		gain.append((i,listcat[i],G))
	if maximum(gain)[2]==0.0:
		addNode(head,string,list1,len(list1[0])-1)
	else:
		addNode(head,string,list1,maximum(gain)[0])
		for i in range(len(getSubArgs(list1,maximum(gain)[0]))):
			newlist=[]
			for x in range(len(list1)):
				if list1[x][maximum(gain)[0]]==getSubArgs(list1,maximum(gain)[0])[i]:
					row=[]
					for y in range(1,len(list1[x])):
						row.append(list1[x][y])
					newlist.append(row)
			decisonTree(newlist,getSubArgs(list1,maximum(gain)[0])[i])

decisonTree(data,None)

pred = []

print("The tree is: ")
printTree(head)
print()
pred.append(input("AGE\nold/mid/new: "))
pred.append(input("COMPETITION\nyes/no: "))
pred.append(input("TYPE\nhardware/software: "))
print("\nPrediction: %s" % (predict(pred,head)))