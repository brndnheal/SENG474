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



dates=daterange(datetime.date(2015,1,1),datetime.date(2016,2,23))
for date in dates:
	for filename in glob.glob("C:\Users\Brendan\Documents\SENG474\DataCollection\Data\PowerPlay\\"+str(date)+"\*.csv"):
			temp= "C:\Users\Brendan\Documents\SENG474\DataCollection\Data\\temp.csv"
			parts = filename.split("\\")
			i=0
			for part in parts:
				if part==str(date):
					new_date=get_date(str(date))
					parts[i]=new_date
			
				if part==parts[len(parts)-1]:
					date_ends=findnth(part,'-',2)
					parts[i]=new_date+part[date_ends:]
				i=i+1


			new_folder="\\".join(parts[:len(parts)-1])
			print new_folder
			new_name="\\".join(parts)


			print new_name
			print filename

			if not os.path.exists(new_folder):
   				 os.makedirs(new_folder)
			os.rename(filename,temp)
			if not os.path.exists(new_name):
				os.rename(temp,new_name)
			else:
				os.remove(temp)

print "done"