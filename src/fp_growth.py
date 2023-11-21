#!/usr/bin/env python

from fpgrowth_py import fpgrowth

from  datasets.base import load_market_basket

#dataset_file = 'market_basket.csv'
dataset_file = "exercise_6.csv"
dataset = load_market_basket(dataset_file)

freqItemSet, rules = fpgrowth(dataset, minSupRatio=0.6, minConf=0.8)

print("Frequent Itemset \n",freqItemSet, "\n")

print("Association Rules \n", rules, "\n")
