import re
import json

def main():
	with open('countsbycity.txt','r') as in_file:
		data = in_file.read()

	cities = dict()
	for line in data.split('\n'):
		if line != '':
			city, words = line.split('\t')
			city = re.sub('"', '', city)
			cities[city] = json.loads(words)

	maxes = dict()
	for city in cities:
		top = 0
		for item in cities[city]:
			for n in item:
				if item[n] > top:
					top = item[n]
					maxes[city] = (n, item[n])

	for item in maxes:
		print item, maxes[item]

if __name__ == '__main__':
	main()
