import datetime
import time
import csv
import os
import glob
import re

season= "20152016"
startdate=[2015,9,29]
session = "Regular"



def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)

def get_dest_filename(source_filename):
	parts=source_filename.split('\\')
	parts.remove("Even")
	dest = "\\".join(parts)
	return dest

def get_date(date):
	parts=date.split('-')
	datestr=str(int(parts[0]))+'-'+str(int(parts[1]))+'-'+str(int(parts[2]))
	return datestr

team_types = ["hometeam","awayteam"]






teams = ["WSH","PHI","NYR","BOS","FLA","NYI","T.B","PIT","DAL","MIN","STL","S.J","L.A","NSH","CHI","ANA"]

pattern= "^[^-]+-[^-]+-[^-]+-[^-]+-(PHX-ARI|ATL-WPG|[^-]+)-(PHX-ARI|ATL-WPG|[^-]+)-\[[^\]]+]-([A-B]).csv$"
for filename in glob.glob("C:\Users\Brendan\Documents\SENG474\DataCollection\Data\StanleyCup\Even\*.csv"):

	dest_file= get_dest_filename(filename)

	parts = filename.split("\\")
	result = re.match(pattern,parts[len(parts)-1])
	with open(filename,'r') as f:
			r = csv.DictReader(f)
			evenGD=0
			for row in r :
				evenGD=row['G+/-']

	with open(dest_file,'r') as f:
		with open("C:\Users\Brendan\Documents\SENG474\DataCollection\Data\\temp.csv",'wb') as f2:
			print dest_file
			writ = csv.writer(f2)
			r = csv.reader(f)
			edit = []
			last =r.next()
			if last[len(last)-1]=='5v5G+/-':
				rm=0
			else:
				rm=1
				last.append('5v5G+/-')
				edit.append(last)
				writ.writerow(last)
				for item in r:
					item.append(evenGD)
					edit.append(item)
					writ.writerow(item)
	os.remove(dest_file)
	os.rename("C:\Users\Brendan\Documents\SENG474\DataCollection\Data\\temp.csv",dest_file)
print "done"