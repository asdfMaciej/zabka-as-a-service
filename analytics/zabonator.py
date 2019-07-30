import os
import csv
from datetime import datetime

PATH = 'C:/zabka'

def open_zabka(path, filename):
	promki = []
	date = datetime.fromtimestamp(int(filename)).strftime('%Y-%m-%d %H:%M:%S')
	with open(path+'/'+filename, 'r', encoding='utf-8') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			break  # get rid of the first row

		for row in reader:
			if 'Pepsi Cola w litrowej butelce' in row[5]:
				row[3] = 'Pepsi Cola w litrowej butelce'
			if 'Pepsi Cola w dużej butelce' in row[5]:
				row[3] = 'Pepsi Cola w dużej butelce'

			promki.append([date] + row)
	return promki

promki = []
for filename in os.listdir(PATH):
	promki += open_zabka(PATH, filename)

with open('zabkabigdata.csv', 'w', newline='', encoding='utf-8') as f:
	writer = csv.writer(f)
	headers = ['date', 'email', 'barcode', 'timeout', 'name', 'price', 'desc', 'img', 'imgsmall']
	writer.writerow(headers)
	for row in promki:
		writer.writerow(row)
