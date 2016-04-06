import os
import glob
import datetime


startdate="2016-02-06"
enddate="2016-02-21"

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)
files=[]

dates=daterange(datetime.date(2016,2,6),datetime.date(2016,2,21))

for date in dates:
			for filename in glob.glob("C:\Users\Brendan\Documents\SENG474\DataCollection\Data\\"+str(date)+"\*.csv"):
				files.append(filename)
	   			'''
	   			if not os.path.exists(new_file):
					os.rename(filename, new_file)
				else:
					os.remove(filename)
				'''

counter =len(files)
temp = "C:\Users\Brendan\Documents\SENG474\DataCollection\Data\\temp.csv"
placeholder = "C:\Users\Brendan\Documents\SENG474\DataCollection\Data\placeholder.csv"
os.rename(files[counter-1],temp)
while (counter>1):
	counter=counter-1
	os.rename(files[counter-1], placeholder)
	os.rename(temp,files[counter-1])
	os.rename(placeholder,temp)
print "success"
	
