#!/usr/bin/env python

#get word counts

import re, json

f = open('reviewtext.json').read()
reviews = json.loads(f)

f2 = open('bizbycity.json').read()
bizcity = json.loads(f2)

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

#remove stopwords from reviews

f3 = open('stopwords.txt', 'rU').read()
f4 = open('reviews_nostop.txt', 'w')

cities_nostop = dict()

for city in cities:
	for item in cities[city]:
		item = json.dumps(item)
		item = item.split(' ')
		for w in item:
			w = w.lower()
			w = re.sub('[,".()!?/]', '', w)
			if city not in cities_nostop:
				cities_nostop[city] = w
			else:
				cities_nostop[city] += (' ' + w)
		print item					

for city in cities_nostop:
	json.dump((city, cities_nostop[city]), f4)
	
