#!/usr/bin/env python

import sys, re, json

#open dataset/find business ids

def access_dataset():
	data = []

	with open('yelpdataset.json', 'rU') as yelpdataset:
		dataset = yelpdataset.read().split(',\n')
		for line in dataset:
			biz = json.loads(line)
			data.append(biz)

	for i in range(6):
		obj = data[i]
		print obj['business_id'], '\n'

def main():
	access_dataset()

#take top 5 business ids

#take top 5 highest reviews for each business

#pull reviews associated with business ids

#process by business/region and location/population

#remove stopwords

if __name__ == "__main__":
	main()
