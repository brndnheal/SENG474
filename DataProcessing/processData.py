from os import listdir
from os.path import isdir
import os
import commands


linetoinsert=[]
for dirName in listdir("."):
	if isdir(dirName):
		currdir = "./"+dirName+"/"
		for fileName in  listdir(currdir):
			f=fileName.split('.')
			
			if f[-1] == "csv":
				gameinfo = f[0].split("-")
				if len(gameinfo) == 8:
					#print gameinfo
					
					win=gameinfo[6]
					win=win.replace("[","")
					win=win.replace("]","")
					hometeam=gameinfo[4]
					awayteam=gameinfo[5]
					
					
					#print fileName
					if gameinfo[-1] == 'A':
						teamName = hometeam
					elif gameinfo[-1] == 'B':
						teamName = awayteam	

					s= commands.getoutput("head -n 2 "+ dirName+"/"+ fileName+" | tail -n 1 | cut -d',' -f 2-8,12-13,37-38,73-76")
					
					if teamName == win:
						 s = s + "," + "1"
					else:
						s = s+","+"0"

					print s



					







			#for line in open(dirName+"/"+fileName):
			#	print line
			#print "new file"

				 