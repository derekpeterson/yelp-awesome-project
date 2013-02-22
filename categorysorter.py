import re

with open('totals.txt', 'rU') as totals:
	data = totals.read()

data = re.sub('"', '', data)
data = data.split('\n')
output = []
for item in data:
	if item != '':
		cat, total = item.split('\t')
		output.append([cat, int(total)])
output = sorted(output, key=lambda x: x[1], reverse=True)
for line in output:
	print line[0], line[1]
