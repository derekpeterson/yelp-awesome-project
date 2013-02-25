from nltk.stem import WordNetLemmatizer
import json, string, re

wnl = WordNetLemmatizer()
c = open('bizbycat.json')
r = open('reviewtext.json')
cats = json.load(c)
revs = json.load(r)


#get list of all food categories
foodcats = []
#catlist.text is shortened list of categories
cfile = open('catlist.txt')
for line in cfile:
    line = line.strip()
    foodcats.append(line)

#get dict of categories:business ids
catdict = {}
for k in cats:
    if k in foodcats:
        for entry in cats[k]:
            val = entry['business_id']
            catdict[k] = catdict.get(k, [])
            catdict[k].append(val)

#write dict to text file for reference
writefile = open('yelpcategories2.txt', 'w')
for k,v in catdict.items():
    writefile.write(k + ': ' + str(v) + '\n')
writefile.close()

#get all reviews in category:text dict 
revcat = {}
for id,txt in revs.items():
    #encode text and strip it of \ns and punctuation
    for review in txt:
        text = []
        review = review.encode('utf-8')
        review = review.replace('\n', ' ')
        review = review.translate(None, string.punctuation)
        text.append(review)
        
    for cat,lst in catdict.items():
        if id in lst:
            revcat[cat] = revcat.get(cat, [])
            revcat[cat].extend(text)
    
#get stopwords ready
#check "Chanda's stopwords.txt" for additional stopwords
stopf = open('stopwords.txt')
stop = []
for line in stopf:
    line = line.strip()
    line = line.translate(None, string.punctuation)
    stop.append(line)

#join reviews into string, lemmatize words, and count words per category
#lemmatizer isn't perfect - check Chanda's stopwords.txt for some others I combined
writefile = open('countsbycat.csv', 'w')
for cat,text in revcat.items(): 
    count = {}
    text = ' '.join(text)
    text = text.split()
    for word in text:
        word = wnl.lemmatize(word)
        word = word.lower()
        if word in stop:
            continue
        else:
            count[word] = count.get(word, 0) + 1

#write word counts to .csv file, if count > 5
    for k,v in count.items():
        #get rid of all numbers
        if re.match('^[0-9]', k):
            continue
        if v >= 5:
            try:
                writefile.write(cat + ',' + k + ',' + str(v) + '\n')
            #to check words that get caught in encoding errors
            except:
                print k,v
                continue
writefile.close()
