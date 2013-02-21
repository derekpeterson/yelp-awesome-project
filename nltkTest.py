#!/usr/bin/env python

from nltk.stem import WordNetLemmatizer
import nltk
import io
import urllib2
import json
import collections

# Get business IDs
connection = open('businesses.json')
businesses = connection.read()
bjson = json.loads(businesses)


# Get reviews
connection = open('reviewtext.json')
reviews = connection.read()
rjson = json.loads(reviews)

# List of tokenized reviews
processedWords = []
count = 1
# CHANGE SCHOOL (make sure spelling is consistent with API)
#school = 'Columbia University'

# CHANGE CATEGORY (make sure spelling is consistent with API)
#category = 'Coffee & Tea'

# Loop through each business in the business JSON object
for b in bjson:
	# String variable to collect all reviews
	tempReviewStr = ""

	# If the school is in the list of schools listed for the business AND the category is in the list of categories listed
#	if school in b['schools'] and category in b['categories'] and rjson.has_key(b['business_id']):
	if rjson.has_key(b['business_id']):
		# Print border
#		print '************************************************'
#		print '************************************************'
		
		# Print school
#		print 'Schools:', school
		
		# Print categories
		categoriesStr = ""
		for c in b['categories']:
			categoriesStr += c + ', '
#		print 'Categories:', categoriesStr

		# Print business name
#		print 'Business Name:', b['name']
#		print 'Business ID:', b['business_id']
#		print 'REVIEWS:'

		# Print reviews
		for review in rjson[str(b['business_id'])]:
			#print type(review)
#			print '*****'
			tempReviewStr += ' ' + review
		# Tokenize all reviews
		tReviews = nltk.word_tokenize(tempReviewStr)
		lwords = []
		wnl = WordNetLemmatizer()
		for tword in tReviews:
			# Strip the word of punctuation
			tword = tword.strip(',')
			tword = tword.strip('.')
			lwords.append(wnl.lemmatize(tword))
		wordCounts = {}
		for word in sorted(lwords):
			if wordCounts.has_key(word) == False:
				wordCounts[word] = 1
			else:
				wordCounts[word] += 1
#		print wordCounts
		processedWords.append([b['business_id'], collections.OrderedDict(sorted(wordCounts.items()))])

		# Write output to text file
		output = open('output.txt', 'w')
#		print processedWords
#		output.write(str(processedWords))
		print str(count) + 'written to output.txt'
		count += 1
#		tokenizedReviews['business_id'] = b['business_id']
#		tokenizedReviews['tokenizedReviews'] = tReviews

#for business in processedWords:
#	print business[1]	
# lemmatize words for ALL business

#each business, combine all reviews and lemmatize, remove stop words, and create dictionary of word counts
#final output: dictionary or word counts.
#
#keep business id, city, state
#remove stars
