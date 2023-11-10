#!/usr/bin/env python3

from datasets.base import load_market_basket
from DIC.DIC import subset_generator, superset_generator, subset_checker, transaction_to_itemset
import copy

"""
dataset_file = 'BD_contaminantes_FP.csv'
#dataset_file = 'market_basket.csv'
dataset = load_market_basket(dataset_file)
dataset = dataset[:10]

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder

# convert dataset into dataframe

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

df = df.replace(False,0).replace(True,1)
df = df.values.tolist()
print(df[0])
"""

# dataset with 4 transactions of 3 items each
df = [[1,1,0],[1,0,0],[0,1,1],[0,0,0]]
unique_itemset =[{1},{2},{3}]

# dataset with 5 transactions of 6 items each
#df = [[1,1,1,0,0],[1,1,1,1,1],[1,0,1,1,0],[1,0,1,1,1],[1,1,1,1,0]]
#unique_itemset = [{i} for i in range(1,len(df[0])+1)]

print(unique_itemset)
min_supp = 25
M = 5
size = len(df)
print("Size of dataset:",size,"\n")

#4 lists are simplemented which store the state if itemsers in the df
DC = []
DS = []	
SC = []
SS = []

# 	update the DC set with all the unique items along with their counters in the df
# 	initially all their counters with 0
# 	itemset is in the form [a,b,c] -> a is itemset , b is its count , c is no_iter
DC = [[i,0,0] for i in unique_itemset]
print("Initial DC:",DC,"\n")

counter = 0
T = []
while DC!=[] or DS!=[]:
#for p in range(20):
	for i in range(counter,counter+M):				#updating counter var in each itemset
		index = i%size
		T = transaction_to_itemset(df[index])
		print("Transaction :",T)

		for item in DC:
			item[2]+=1
			if item[0].issubset(T):
				item[1]+=1
		for item in DS:
			item[2]+=1
			if item[0].issubset(T):
				item[1]+=1		

	for item in copy.copy(DC):								#transfer itemsets from DC to DS basef on min_supp
		if(item[1]>=min_supp):
			DS.append(item)
			DC.remove(item)

	for item in copy.copy(DS):								#transfer itemsets from DS to SS if it's count=size
		if(item[2]==size):
			SS.append(item)
			DS.remove(item)			
	for item in copy.copy(DC):								#transfer itemsets from DC to SC if it's count=size
		if(item[2]==size):
			SC.append(item)
			DC.remove(item)
	#print(DC)
	
	FIS = copy.copy(DS)
	FIS.extend(SS)								#check if all subsets are there in FIS for immediate supersets
	for item in FIS:
		S = superset_generator(item[0],unique_itemset)
		for i in S:
			if subset_checker(i,FIS):
				flag=1
				for x in DC:
					if x[0]==i:
						flag=0
				for x in DS:
					if x[0]==i:
						flag=0
				for x in SC:
					if x[0]==i:
						flag=0
				for x in SS:
					if x[0]==i:
						flag=0						
				if flag:
					DC.append([i,0,0])		

	counter+=M
	print("DS: ",DS)
	print("DC: ",DC)
	print("SS: ",SS)
	print("SC: ",SC,"\n")
