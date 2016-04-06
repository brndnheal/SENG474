import datetime
import time
import csv
import os
import glob
import re


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)



def get_date(date):
	parts=date.split('-')
	datestr=str(int((parts[0])))+'-'+str(int((parts[1])))+'-'+str(int((parts[2])))
	return datestr


def findnth(haystack, needle, n):
    parts= haystack.split(needle, n+1)
    if len(parts)<=n+1:
        return -1
    return len(haystack)-len(parts[-1])-len(needle)



dates=daterange(datetime.date(2015,9,29),datetime.date(2016,2,22))
for date in dates:
	pattern= "^[^-]+-[^-]+-[^-]+-[0-9]+-(PHX-ARI|ATL-WPG|[^-]+)-(PHX-ARI|ATL-WPG|[^-]+)-\[[^\]]+]-([A-B]).csv"
	for filename in glob.glob("C:\Users\Brendan\Documents\SENG474\DataCollection\Data\\"+str(date)+"\*.csv"):
		parts = filename.split("\\")
		result = re.match(pattern,parts[len(parts)-1])
		if(result==None):
			print filename
			os.remove(filename)
'''
		if not os.path.exists(new_folder):
				 os.makedirs(new_folder)
		os.rename(filename,temp)
		if not os.path.exists(new_name):
			os.rename(temp,new_name)
		else:
			os.remove(temp)
		if os.path.exists(filename):
				 os.remove(filename)
'''

