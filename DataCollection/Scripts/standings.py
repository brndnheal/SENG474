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

def get_standings(points):
	cen=[]
	pac=[]
	atl=[]
	met=[]

	for team in central:
		cen.append((team,log[team]))
	for team in pacific:
		pac.append((team,log[team]))
	for team in atlantic:
		atl.append((team,log[team]))
	for team in metropolitian:
		met.append((team,log[team]))
	
	cen.sort(key=lambda tup: tup[1])
	pac.sort(key=lambda tup: tup[1])
	atl.sort(key=lambda tup: tup[1])
	met.sort(key=lambda tup: tup[1])

	#1st and second place
	Wtop = [cen.pop(),pac.pop()]
	Etop = [atl.pop(),met.pop()]

	#3rd and 4th place
	Wtop2 = [cen.pop(),pac.pop()]
	Etop2 = [atl.pop(),met.pop()]

	#5th and 6th place
	Wtop3 = [cen.pop(),pac.pop()]
	Etop3 = [atl.pop(),met.pop()]

	#The Rest
	WWild=cen+pac
	EWild=atl+met

	Wtop.sort(key=lambda tup: tup[1])
	Etop.sort(key=lambda tup: tup[1])
	Wtop2.sort(key=lambda tup: tup[1])
	Etop2.sort(key=lambda tup: tup[1])
	Wtop3.sort(key=lambda tup: tup[1])
	Etop3.sort(key=lambda tup: tup[1])
	WWild.sort(key=lambda tup: tup[1])
	EWild.sort(key=lambda tup: tup[1])
	WStandings = Wtop[::-1]+Wtop2[::-1]+Wtop3[::-1]+WWild[::-1]
	EStandings = Etop[::-1]+Etop2[::-1]+Etop3[::-1]+EWild[::-1]
	print WStandings
	print EStandings
	return WStandings, EStandings
	

def get_date(date):
	parts=date.split('-')
	datestr=str(int(parts[0]))+'-'+str(int(parts[1]))+'-'+str(int(parts[2]))
	return datestr


games = parseGameFile("games.csv")
team_types = ["hometeam","awayteam"]




log = {}
for team in teams:
	log[team]=0

dates=daterange(datetime.date(2016,3,14),datetime.date(2016,3,16))
for date in dates:
	curr_range=daterange(datetime.date(2015,9,29),date)
	for curr_date in curr_range:
		for game in games:
			
			d,m,y = game["date"].split("/")
			gameday= datetime.date(int(y),int(m),int(d))

			if gameday == curr_date:
				if game["winner"] == game["hometeam"]:
					winner = "hometeam"
					loser = "awayteam"
				elif game["winner"]==game["awayteam"]:
					winner = "awayteam"
					loser = "hometeam"
				else:
					continue
				log[game[winner]] = log[game[winner]]+2
				if int(game["periods"])>3:
					log[game[loser]] = log[game[loser]]+1

	Wstandings,Estandings=get_standings(log)
	wList=[y[0] for y in Wstandings]
	eList=[y[0] for y in Estandings]
	#Have standings, now, to get them into the file.
	#Open the the corresponding date folder, and put the standing for each team in. 
	#[y[0] for y in tuple_list].index('ARI')
	
	#Regex for dual team case
	pattern= "^[^-]+-[^-]+-[^-]+-[^-]+-(PHX-ARI|ATL-WPG|[^-]+)-(PHX-ARI|ATL-WPG|[^-]+)-\[[^\]]+]-([A-B]).csv$"
	for filename in glob.glob("C:\Users\Brendan\Documents\SENG474\DataCollection\Data\\"+get_date(str(date))+"\*.csv"):
		parts = filename.split("\\")
		result = re.match(pattern,parts[len(parts)-1])

		with open(filename,'r') as f:
			with open("C:\Users\Brendan\Documents\SENG474\DataCollection\Data\\temp.csv",'wb') as f2:
				writ = csv.writer(f2)
				r = csv.reader(f)
				edit = []
				last =r.next()
				last.append('Standing')
				edit.append(last)
				writ.writerow(last)
			
				for item in r:
					if result.group(3)=="A":
						if result.group(1) in wList:
							index=wList.index(result.group(1))  
						else:
							index=eList.index(result.group(1))  
					else:
						if result.group(2) in wList:
							index=wList.index(result.group(2))  
						else:
							index=eList.index(result.group(2)) 
					item.append(str(index+1))
					edit.append(item)
					writ.writerow(item)
		os.remove(filename)
		os.rename("C:\Users\Brendan\Documents\SENG474\DataCollection\Data\\temp.csv",filename)
	for team in teams:
		log[team]=0

print "done"