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
#processedWords = []
processedWords = {}
count = 1

output = open('outputNotAlphabetized.json', 'w')

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
#		processedWords.append([b['business_id'], collections.OrderedDict(sorted(wordCounts.items()))])
		processedWords[b['business_id']] = wordCounts
#		print processedWords[b['business_id']]
		print str(count) + ' Reviews for ' + str(b['business_id']) + ' tokenized, lemmatized, and added to dictionary.'

		# Write output to text file
#		output = open('output.txt', 'w')
#		output.write(str(processedWords))
		print str(count) + ' processed'
		count += 1
str = json.dumps(processedWords)
output.write(str)
output.close()
print 'processedWords written to outputNotAlphabetized.json'
