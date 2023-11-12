#!/usr/bin/python

# mlxtend provides fim using apriori

from  datasets.base import load_market_basket

#dataset_file = 'market_basket.csv'
dataset_file = "exercise_6.csv"
dataset = load_market_basket(dataset_file)

#dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
#           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
#           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
#           ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
#           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']]

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder

# convert dataset into dataframe
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

print(df)

from mlxtend.frequent_patterns import apriori

print(apriori(df, min_support=0.6, use_colnames=True))
