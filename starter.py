#!/usr/bin/env python

import sys, re, json

#open dataset/find business ids

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

def access_dataset():
	LIMIT = 1
	with open("reviewtext.json", "rU") as yelpdataset:
		data = json.load(yelpdataset)

	# Will print every list of reviews
	# line is the business_id
	for line in data:
		print data[line]

	# Took all of the restaurants from bizbycat.json,
	# loaded their business_id into a list,
	# ran through the reviews in reviewsbybiz,
	# and added 'business_id': [reviews text],
	# to reviewtext before dumping it to
	# reviewtext.json.
	# businesses = []
	# for biz in data['Restaurants']:
	# 	businesses.append(biz['business_id'])

	# with open('reviewsbybiz.json') as reviewsbybiz:
	# 	review_data = json.load(reviewsbybiz)

	# reviewtext = dict()

	# for biz in review_data:
	# 	if biz in businesses:
	# 		texts = [rev['text'] for rev in review_data[biz]]
	# 		reviewtext[biz] = texts

	# with open('reviewtext.json', 'w') as reviewsbybiz:
	# 	json.dump(reviewtext, reviewsbybiz)

	# This goes through to print the business categories
	# which are the keys in bizbycat.json
	# with the value being a dict described below
	# for line in sorted(data.keys()):
	# 	print line

	# cats = dict()
	# for thing in data:
	# 	biz = {
	# 		'city': thing['city'],
	# 		'name': thing['name'],
	# 		'business_id': thing['business_id'],
	# 		'stars': thing['stars'],
	# 		'review_count': thing['review_count'],
	# 		'state': thing['state']
	# 	}
	# 	for category in thing['categories']:
	# 		if category in cats:
	# 			cats[category].append(biz)
	# 		else:
	# 			cats[category] = [biz]

	# with open('bizbycat.json', 'w') as out_file:
	# 	json.dump(cats, out_file)

	# reviews = dict()
	# for item in data:
	# 	biz_id = item['business_id']
	# 	review = {
	# 		'review_id': item['review_id'], 'stars': item['stars'], 'text': item['text']
	# 	}
	# 	if biz_id in reviews:
	# 		reviews[biz_id].append(review)
	# 	else:
	# 		reviews[biz_id] = [review]

	# with open('reviewsbybiz.json', 'w') as out_file:
	# 	json.dump(reviews, out_file)

	# reviews = []
	# businesses = []
	# users = []

	# for i in data:
	# 	kind = i["type"]
	# 	if kind == "review":
	# 		reviews.append(i)
	# 	elif kind == "user":
	# 		users.append(i)
	# 	elif kind == "business":
	# 		businesses.append(i)

	# with open("reviews.json", "w") as out_file:
	# 	json.dump(reviews, out_file)

	# with open("users.json", "w") as out_file:
	# 	json.dump(users, out_file)

	# with open("businesses.json", "w") as out_file:
	# 	json.dump(businesses, out_file)

def main():
	access_dataset()

#
#take top 5 business ids

#take top 5 highest reviews for each business

#pull reviews associated with business ids
#done: in reviewsbybiz.json

#process by business/region and location/population

#remove stopwords

if __name__ == "__main__":
	main()
