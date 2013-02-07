#!/usr/bin/env python

import sys, re, json

def access_dataset():
	with open('prettydata.json', 'rU') as yelpdataset:
		print eval(yelpdataset.read())

def main():
	access_dataset()

if __name__ == "__main__":
	main()
