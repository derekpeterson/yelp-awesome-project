#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re, json
from mrjob.job import MRJob

#I created a new file from Lan's code without word counts so that's what I'm using here
f = open('revbybiz.json').read()
reviews = json.loads(f)

f2 = open('bizbycity.json').read()
bizcity = json.loads(f2)

f4 = open('separated_by_city.txt', 'w')

#group reviews by city

cities = dict()

for city in bizcity:
	for biz in bizcity[city]:
		biz_id = biz['business_id']
		for r in reviews:
			if biz_id == r:
				if city not in cities:
					cities[city] = reviews[r]
				else:
					cities[city].append(reviews[r])

for city in cities:
	f4.write(unicode(city) + "\t" + unicode(cities[city]) + "\n")

#get counts/remove stopwords from reviews

class Reviews(MRJob):

	#for some reason, the file won't open without the whole path
	stops = open("/Users/Sarah/Dropbox/School/601/yelp-awesome-project/stopwords.txt", 'rU').readlines()

	global l
	l = list()
	
	for item in stops:
		l.append(item.strip())

	def mapper(self, _, line):
		line = re.sub(r"\[|\]| ", '', line)
		data = line.split("\t")
		data[1] = [item for item in data[1].split(',')]
		words = dict()
		for item in data[1]:
			item = item.strip("u'")
			if item.startswith("'") or item.startswith('"'):
				continue
			else:
				if item != '':
					if item not in l:
						if item.lower() in words:
							words[item.lower()] += 1
						else:
							words[item.lower()] = 1
		yield data[0], words

	def reducer(self, city, counts):
		yield city, [word for word in counts]

if __name__ == '__main__':
	Reviews.run()
