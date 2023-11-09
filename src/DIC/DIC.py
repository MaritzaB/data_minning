"""
This is the basic implementation of DIC(Dynamic itemset algotithm)
Referred from : http://www2.cs.uregina.ca/~dbd/cs831/notes/itemsets/DIC.html
"""

import itertools 

def subset_generator(S,n):
	"""
	takes in a set S and size of the subsets to generate.
	generates all subsets of size len(s)-1
	"""
	print(S)
	a = itertools.combinations(S,n)
	result = []
	for i in a:
		result.append(set(i))
	return(result)	

def superset_generator(S,unique_itemset):
	"""
	Takes in a set S and generates it's 
	immediate superset from the unique itemset
	"""
	#print(S)
	result = []
	a = set()
	for i in unique_itemset:
		if i.intersection(S)==set():
			a = i.union(S)
			result.append(a)
			a = set()

	return(result)		

def subset_checker(S,FIS):
	"""
	takes in a set S and check if all if its len(s)-1 subsets 
	are there in FIS
	"""
	subset = subset_generator(S,len(S)-1)
	flag = 1
	temp = []

	for i in FIS:
		temp.append(i[0])

	FIS = temp
	for i in subset:
		if i not in FIS:
			flag=0
			break

	if flag:
		return(True)
	else:
		return(False)

def transaction_to_itemset(T):
	"""
	Converts each record of a database in to a itemset format
	"""
	result = set()
	for i in range(len(T)):
		if T[i]!=0:
			result.add(i+1)

	return(result)		
