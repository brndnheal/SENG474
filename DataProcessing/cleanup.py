import datetime
import time
import csv
import os
import glob
import re

season= "20152016"
startdate=[2015,9,29]
session = "Regular"

teams = ["ANA","BOS","BUF","CAR","CBJ","CGY","CHI","COL","DAL","DET","EDM","FLA","L.A","MIN","MTL","N.J","NSH","NYI","NYR","OTT","PHI","PIT","S.J","STL","T.B","TOR","VAN","ATL-WPG","WSH","PHX-ARI"]

#West Divisions
central=["DAL","CHI","STL","NSH","COL","MIN","ATL-WPG"]
pacific=["L.A","ANA","S.J","VAN","PHX-ARI","CGY","EDM"]

#East Divisions
atlantic=["FLA","T.B","BOS","DET","OTT","MTL","BUF","TOR"]
metropolitian=["WSH","NYR","NYI","PIT","PHI","N.J","CAR","CBJ"]

def parseGameFile(gfile):
	games=[]
	gamefieldnames= ["no","season","session","gamenumber","gcode","status","awayteam","hometeam","awayscore","homescore","date","periods","winner"]
	with open(gfile,'rb') as gamecsv:
	    gamereader = csv.DictReader(gamecsv)
	    for row in gamereader:
	    	startd = datetime.date(startdate[0], startdate[1], startdate[2]) 
	    	d,m,y = row["date"].split('/')
	    	currd = datetime.date(int(y), int(m), int(d))
	        if row["season"] == season and row["session"]==session and (currd>=startd):
	                date = row["date"]
	                away = row["awayteam"]
	                home = row["hometeam"]
	                winner = row["winner"]
	                periods = row["periods"]
	                games.append(row)
	return games


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

games = parseGameFile("games.csv")
team_types = ["hometeam","awayteam"]


for i in range(0,73):
	print "r["+str(i)+"], ",

log = {}
for team in teams:
	log[team]=0
rm=0
dates=daterange(datetime.date(2016,3,14),datetime.date(2016,3,16))
for date in dates:
	pattern= "^[^-]+-[^-]+-[^-]+-[^-]+-(PHX-ARI|ATL-WPG|[^-]+)-(PHX-ARI|ATL-WPG|[^-]+)-\[[^\]]+]-([A-B]).csv$"
	for filename in glob.glob("C:\Users\Brendan\Documents\SENG474\DataCollection\Data\\"+get_date(str(date))+"\*.csv"):
	
		with  open(filename,'rb') as f:
			with open("C:\Users\Brendan\Documents\SENG474\DataCollection\Data\\temp.csv",'wb') as f2:
				writ = csv.writer(f2)
				r = csv.reader(f)
				

				for row in r:
					if len(row)>=73:
						rm=1
						print filename
						writ.writerow( (row[0],  row[1],  row[2],  row[3],  row[4],  row[5],  row[6],  row[7],  row[8],  row[9],  row[10],  row[11],  row[12],  row[13],  row[14],  row[15],  row[16],  row[17],  row[18],  row[19],  row[20],  row[21],  row[22],  row[23],  row[24],  row[25],  row[26],  row[27],  row[28],  row[29],  row[30],  row[31],  row[32],  row[33],  row[34],  row[35],  row[36],  row[37],  row[38],  row[39],  row[40],  row[41],  row[42],  row[43],  row[44],  row[45],  row[46],  row[47],  row[48],  row[49],  row[50],  row[51],  row[52],  row[53],  row[54],  row[55],  row[56],  row[57],  row[58],  row[59],  row[60],  row[61],  row[62],  row[63],  row[64],  row[65],  row[66],  row[67],  row[68],  row[69],  row[70],  row[71],  row[72])) 


		if(rm==1):
			os.remove(filename)
			os.rename("C:\Users\Brendan\Documents\SENG474\DataCollection\Data\\temp.csv",filename)
			rm-0
print "done"