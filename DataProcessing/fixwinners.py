import os
import glob
import datetime
import csv
season= "20152016"
startdate=[2015,9,29]
session = "Regular"
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

games = parseGameFile("games.csv")

dates=daterange(datetime.date(2015,10,7),datetime.date(2016,2,21))

for date in dates:
	for game in games:
		d,m,y = game["date"].split("/")
		gameday= datetime.date(int(y),int(m),int(d))
		if gameday==date:
			for filename in glob.glob("C:\Users\Brendan\Documents\SENG474\DataCollection\Data\\"+str(date)+"\*.csv"):

				parts=filename.split("-")
				if(parts[5]==game["gamenumber"]):
						os.rename(filename,filename[:filename.index("[")] +"["+ game["winner"]+filename[filename.index("]"):])
print "done"






