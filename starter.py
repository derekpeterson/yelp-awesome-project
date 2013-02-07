#!/usr/bin/env python

import sys, re, json

def access_dataset():
	with open('yelpdataset.json', 'rU') as yelpdataset:
		data = re.sub('}\n{', '},\n{', yelpdataset.read())

	with open('prettydata.json', 'w') as dataset:
		dataset.write(data)

def main():
	access_dataset()

if __name__ == "__main__":
	main()
