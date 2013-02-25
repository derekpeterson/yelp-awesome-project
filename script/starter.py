#!/usr/bin/env python

import sys, re, json

# We have:
# 	- yelpdataset.json
# 	- reviews.json
# 	- businesses.json
# 	- users.json
# 	- bizbycat.json (businesses by category)
# 	- bizbycity.json (businesses by city)
# 	- reviewsbybiz.json (reviews separated by businesses)
# 		- dict with keys set to business_id
# 		- has review_id, stars, and text for each review
#		- reviewtext.json
#			- reviews for restaurants
#			- biz_id: [review1, review2, ... , reviewn]

def access_dataset():
	LIMIT = 1
	with open("reviewtext.json", "rU") as reviews:
		data = json.load(reviews)

	# Will print every list of reviews
	# line is the business_id
	for line, i in zip(data, range(LIMIT)):
		print data[line]

def collect_reviews():
	# Takes all of the restaurants from bizbycat.json,
	# loads their business_id into a list,
	# runs through the reviews in reviewsbybiz,
	# and adds 'business_id': [reviews text]
	# to reviewtext before dumping it to
	# reviewtext.json.
	with open("businesses.json", "rU") as businesses:
		data = json.load(businesses)

	with open('reviewsbybiz.json') as reviewsbybiz:
		review_data = json.load(reviewsbybiz)

	businesses = [biz for biz in data['Restaurants']]

	reviewtext = dict()

	for biz in review_data:
		if biz in businesses:
			reviewtext[biz] = [rev['text'] for rev in review_data[biz]]

	with open('reviewtext.json', 'w') as reviewsbybiz:
		json.dump(reviewtext, reviewsbybiz)

def separate_businesses_by_cat():
	with open('businesses.json', 'rU') as businesses:
		data = json.load(businesses)

	cats = dict()

	for thing in data:
		biz = {
			'city': thing['city'],
			'name': thing['name'],
			'business_id': thing['business_id'],
			'stars': thing['stars'],
			'review_count': thing['review_count'],
			'state': thing['state']
		}
		for category in thing['categories']:
			if category in cats:
				cats[category].append(biz)
			else:
				cats[category] = [biz]

def separate_reviews():
	with open('bizbycat.json', 'w') as out_file:
		json.dump(cats, out_file)

	reviews = dict()
	for item in data:
		biz_id = item['business_id']
		review = {
			'review_id': item['review_id'], 'stars': item['stars'], 'text': item['text']
		}
		if biz_id in reviews:
			reviews[biz_id].append(review)
		else:
			reviews[biz_id] = [review]

	with open('reviewsbybiz.json', 'w') as out_file:
		json.dump(reviews, out_file)

def filter_data():
	with open('yelpdataset.json', 'rU') as yelpdataset:
		reviews = []
		businesses = []
		users = []

		for i in data:
			kind = i["type"]
			if kind == "review":
				reviews.append(i)
			elif kind == "user":
				users.append(i)
			elif kind == "business":
				businesses.append(i)

		with open("reviews.json", "w") as out_file:
			json.dump(reviews, out_file)

		with open("users.json", "w") as out_file:
			json.dump(users, out_file)

		with open("businesses.json", "w") as out_file:
			json.dump(businesses, out_file)

def main():
	access_dataset()

#
#take top 5 business ids
#take top 5 highest reviews for each business
#--Aren't we not doing these because we're using everything? -Sarah

#pull reviews associated with business ids
#done: in reviewsbybiz.json

#process by business/region and location/population

#remove stopwords

if __name__ == "__main__":
	main()
