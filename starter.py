#!/usr/bin/env python

import sys, re, json

#open dataset/find business ids

def access_dataset():
	with open('yelpdataset.json') as yelpdataset:
		data = json.load(yelpdataset)

	for line in data:
		print line['business_id']

def main():
	access_dataset()

#take top 5 business ids

#take top 5 highest reviews for each business
#pull reviews associated with business ids

#process by business/region and location/population

#remove stopwords

if __name__ == "__main__":
	main()