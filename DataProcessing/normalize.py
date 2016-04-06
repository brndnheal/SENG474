import datetime
import time
import csv
import os
import glob
import re

season= "20152016"
startdate=[2015,10,7]
session = "Regular"
infile="DATA.csv"

with open(infile, 'rb') as csvfile:
	games=[]
	gamereader = csv.reader(csvfile)
	max_array=[]
	min_array=[]
	j=0
	for row in gamereader:
		if j==0:
			j=j+1
		#	for i in row:
			#	print str(i)+",",
		#	print
		#	continue
		if j==1:
		    max_array=row[:]
		    min_array=row[:]

		j=j+1
		games.append(row)

		for i in range(0,len(row)):
			if float(row[i])<float(min_array[i]):
				min_array[i]=row[i]

			if float(row[i])>float(max_array[i]):
				max_array[i]=row[i]
				
	
	for row in games:
		for i in range(0,len(row):
			row[i]=((float(row[i])-float(min_array[i])) / (float(max_array[i])-float(min_array[i])))
		for i in row:
			print str(i)+",",
		print

	