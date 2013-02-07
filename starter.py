#!/usr/bin/env python

import sys, re, json

def access_dataset():
	with open('yelpdataset.json') as yelpdataset:
		data = json.load(yelpdataset)

	for line in data:
		print line['business_id']

def main():
	access_dataset()

if __name__ == "__main__":
	main()
