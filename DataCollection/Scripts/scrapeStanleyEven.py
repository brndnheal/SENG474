from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
import autoit
import time
import csv
import os
import glob

season= "20152016"
session= "Regular"
startdate=[2016,2,21]

#Web driver 
'''
chromedriver = "C:\Users\Brendan\chromedriver\chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
browser.get("http://www.google.com")
time.sleep(10)
browser.quit()
'''

def createFFProfile():
	profile = webdriver.FirefoxProfile()
	profile.set_preference("browser.download.folderList", 2)
	profile.set_preference("browser.download.manager.showWhenStarting", False)
	profile.set_preference("browser.download.dir", 'C:\Users\Brendan\Documents\SENG474\DataCollection\Data')
	profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv,application/vnd.ms-excel,application/csv")
	profile.set_preference("browser.helperApps.alwaysAsk.force", False)
	return profile

def initDriver():
	profile=createFFProfile()
	browser = webdriver.Firefox(firefox_profile=profile)
	return browser

#game file parsing

#Date Format for input tocapture snapshot from website using selenium: year-month-day-1 (day before game)
def formatDateA(date):
	parts = date.split("/")
	formDate = parts[2] + "-" + parts[1]+"-"+str(int(parts[0])-1)
	return formDate

#Date Format for printing/file naming: year-month-day
def formatDateB(date):
	parts = date.split("/")
	formDate =  str(int(parts[2])) + "-" + str(int(parts[1]))+"-"+str(int(parts[0]))
	return formDate
#time.sleep(5)
teams = ["WSH","PHI","NYR","BOS","FLA","NYI","T.B","PIT","DAL","MIN","STL","S.J","L.A","NSH","CHI","ANA"]
for team in teams:
		print "Getting info for: "+team
		browser=initDriver()
		element = browser.get("http://war-on-ice.com/teambygame.html")
		print "Waiting for browser..."
		#Find the iframe
		try:
		    element = WebDriverWait(browser, 100).until(
		        EC.presence_of_element_located((By.ID, 'vincerlink'))
		    )
		    frame = browser.find_element_by_id('vincerlink')
		finally:
			print "done"
		try:
		
			wait = WebDriverWait(browser, 100).until(EC.frame_to_be_available_and_switch_to_it(frame))
			
			#browser.find_element_by_xpath("//div[@id='daterange']/input[1]").clear()

			wait = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.ID, 'DataTables_Table_0')))
			
			start = browser.find_element_by_xpath("//div[@id='daterange']/input[1]")
			start.clear()
			start.send_keys(season[:4]+"-08-1")
			end = browser.find_element_by_xpath("//div[@id='daterange']/input[2]")
			end.clear()
			end.send_keys("2016-03-25")
			end = browser.find_element_by_xpath("//div[@id='daterange']/input[2]")
			strengths= browser.find_element_by_xpath("//div[@id='onload.1']/div/div[1]")
			strengths.click()
			strengths= browser.find_element_by_xpath("//div[@id='onload.1']/div/div[2]/div/div[text()='Even Strength 5v5']")
			strengths.click()
			teamlink= browser.find_element_by_xpath("//div[@id='onload.4']/div/div[1]")
			teamlink.click()
			print team
			teamlink= browser.find_element_by_xpath("//div[@id='onload.4']/div/div[2]/div/div[text()='"+team+"']")
			teamlink.click()
			wait = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.ID, 'gametable')))
		
			time.sleep(2)
			wait = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.ID, 'downloadSData')))

			wait = WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.ID,'downloadSData')))
			button = browser.find_element_by_id("downloadSData")
			button.click()
			#AutoIT to handle the dialog window
			autoit.win_wait_active("[CLASS:MozillaDialogClass]", 10)
			autoit.send("{ALTDOWN}s{ALTUP}")
			time.sleep(1)
			autoit.send("{ENTER}")
			time.sleep(1)
		finally:
			print "Closing Browser"
			browser.close()
			#Now Move the file to a good folder
			if((teams.index(team)%2)==0):
				letter="A" 
			else: 
				letter="B"


			new_dir="C:\Users\Brendan\Documents\SENG474\DataCollection\Data\StanleyCup\Even"
			new_file=new_dir+"\\" + team+"-"+letter+".csv"
			if not os.path.exists(new_dir):
   				 os.makedirs(new_dir)
   			for filename in glob.glob("C:\Users\Brendan\Documents\SENG474\DataCollection\Data\*.csv"):
	   			if not os.path.exists(new_file):
					os.rename(filename, new_file)
				else:
					os.remove(filename)

browser.quit()



	


