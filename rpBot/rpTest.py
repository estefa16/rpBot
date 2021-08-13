from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

#List of suburbs to be searched
suburbs = ['Watsons Bay', 'Vaucluse']





######################
## BROWSER FUNCTIONS #
######################

class Scraper:

	def __init__(self, browser):

		#Initiate browser
		self.browser = browser
		browser.get('https://rpp.corelogic.com.au/')
		print("Im a Bot! :D")


	#Login and print succes
	def site_login(self, username, pwd):
	
		browser.find_element_by_id('username').send_keys(username)
		browser.find_element_by_id('password').send_keys(pwd)
		browser.find_element_by_id('login').click()

		if WebDriverWait(browser, 10).until(EC.title_contains('RP Data')) == True:
			print('Success!')

		else:
			print('poo ;(')

	#Searches for sales in input suburb 

	#TAG TO FIND#
	#<input type="search" autocomplete="off" aria-autocomplete="list" 
	#aria-controls="react-autowhatever-1" class="form-control" 
	#placeholder="Search for an address, street name, suburb, postcode, council area or state" value="">

	def search_suburb(self, suburb):

		search = WebDriverWait(browser,5).until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Search for an address, street name, suburb, postcode, council area or state"]')))
		search.send_keys(suburb)

		#option = WebDriverWait(browser, 6).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'"+suburb+"')]")))
		time.sleep(3)
		search.send_keys(Keys.DOWN, Keys.RETURN)
		#search.click().perform()
		print('Target located O.O')


	#Filters results by date 
	def filter_by_date(self):

		#date = WebDriverWait(browser,5).until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Sale Date")]')))
		date = browser.find_element_by_id('dropdownSelectedValue')
		print(date)



	#Select all properties from filtered list
	def select_all(self):
		pass

	#Download csv into folder 
	def download_csv(self, folder):
		pass


	#Extract all information from excel doc and copy it to the master doc
	def information_control(self, propertyDoc, masterDoc):
		pass


	def bye_bye(self):
		browser.close()



###############
## OPERATIONS #
###############
start_date = [24, 'May', 2021]
end_date = [10, 'June', 2021]

browser = webdriver.Chrome()

bot = Scraper(browser)
bot.site_login('EqunoxDesigns', 'RPdatateam123!')
bot.search_suburb('Artarmon NSW 2064')
#bot.filter_by_date()
bot.bye_bye()







##################
## Test Controls #
##################







