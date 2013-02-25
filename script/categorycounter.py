#!/usr/bin/env python

from mrjob.job import MRJob
import json

class Counter(MRJob):

	def mapper(self, _, line):
		data = json.loads(line)
		for item in data:
			categories = item.get('categories', None)
			if 'Restaurants' in categories:
				for cat in categories:
					yield cat, 1

	def reducer(self, key, values):
		yield key, sum(values)

if __name__ == '__main__':
	Counter.run()
