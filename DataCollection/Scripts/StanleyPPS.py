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
	parts.remove("PowerPlay")
	dest = "\\".join(parts)
	return dest

def get_date(date):
	parts=date.split('-')
	datestr=str(int(parts[0]))+'-'+str(int(parts[1]))+'-'+str(int(parts[2]))
	return datestr

team_types = ["hometeam","awayteam"]






teams = ["WSH","PHI","NYR","BOS","FLA","NYI","T.B","PIT","DAL","MIN","STL","S.J","L.A","NSH","CHI","ANA"]

pattern= "^[^-]+-[^-]+-[^-]+-[^-]+-(PHX-ARI|ATL-WPG|[^-]+)-(PHX-ARI|ATL-WPG|[^-]+)-\[[^\]]+]-([A-B]).csv$"
for filename in glob.glob("C:\Users\Brendan\Documents\SENG474\DataCollection\Data\StanleyCup\PowerPlay\*.csv"):

	dest_file= get_dest_filename(filename)

	parts = filename.split("\\")
	result = re.match(pattern,parts[len(parts)-1])
	pkga=0
	with open(filename,'r') as f:
			r = csv.DictReader(f)
			ppg=0
			for row in r :
				ppg=row['GF']
	with open(dest_file,'r') as d:
		r2 = csv.DictReader(d)
		for row2 in r2:
			if float(row2['PN-'])==0:
				PPsuccess= 100.0
			else:
				PPsuccess=float(ppg)/float(row2['PN-'])*100.0
			print PPsuccess

	with open(dest_file,'r') as f:
			with open("C:\Users\Brendan\Documents\SENG474\DataCollection\Data\\temp.csv",'wb') as f2:
				writ = csv.writer(f2)
				r = csv.reader(f)
				edit = []
				last =r.next()
				last.append('PPSuccess')
				edit.append(last)
				writ.writerow(last)
				for item in r:
					item.append(PPsuccess)
					edit.append(item)
					writ.writerow(item)
	os.remove(dest_file)
	os.rename("C:\Users\Brendan\Documents\SENG474\DataCollection\Data\\temp.csv",dest_file)
print "done"