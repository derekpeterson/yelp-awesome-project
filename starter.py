#!/usr/bin/env python

import sys, re, json

#open dataset/find business ids

def access_dataset():
	with open('yelpdataset.json', 'rU') as yelpdataset:
		data = re.sub('}\n{', '},\n{', yelpdataset.read())

	with open('prettydata.json', 'w') as dataset:
		dataset.write(data)

def main():
	access_dataset()

#take top 5 business ids

#take top 5 highest reviews for each business

#pull reviews associated with business ids

#process by business/region and location/population

#remove stopwords

if __name__ == "__main__":
	main()
