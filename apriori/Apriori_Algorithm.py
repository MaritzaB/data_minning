#!/usr/bin/env python3

import pandas as pd
import numpy as np
from itertools import combinations

#df = pd.read_csv("apriori/Transaction.csv",header=None)
df = pd.read_csv("apriori/BD_Contaminantes_FP.csv",skiprows=1, nrows=1000)

"""
dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']]
"""
print(df.head(), "\n")

#df = pd.DataFrame(dataset)

Candidate_set = []
Frequent_set = []
items = pd.unique(df.values.ravel('K'))
items = items[~pd.isnull(items)]

print(items, "\n")

min_support = 100

for iterno in range(1,len(items)):
    Count = {}
    intermediate = []
    
    if iterno==1:
        Candidate_set.append(items)
        for txn in Candidate_set[iterno-1]:
            ctr=0
            for val in df.values:
                if txn in val:
                    ctr+=1
            Count[txn] = ctr
    else:
        Candidate_set.append(list(combinations(np.unique(np.array(Frequent_set[iterno-2]).ravel('K')),iterno)))
        for txn in Candidate_set[iterno-1]:
            ctr = 0
            for val in df.values:
                if all(i in val for i in txn):
                    ctr+=1
            Count[txn] = ctr
            
    for k in Count.keys():
        if Count[k] >= min_support:
            intermediate.append(k)

    if intermediate == []:
        print(Frequent_set, "\n")
        break

    Frequent_set.append(intermediate)
