from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import random
import time
import sqlite3

#getting data from tts_urls.sqlite to form dict for farther web requests
sql_conn = sqlite3.connect('tts_urls.sqlite')
cursor = sql_conn.cursor()

pages_dict = {}
urls_list = []
p = 0

for element in cursor.execute('SELECT urls.url || items.item_price FROM urls INNER JOIN items ON item_name = url_name;'):
	urls_list.append(element[0])

for element in cursor.execute('SELECT items.item_name FROM items;'):
	pages_dict[element[0]] = urls_list[p]
	p+=1

print(pages_dict)

def get_pages(pages_dict):
	'''This func's job is getting web pages source cod WITH dynamic data suppplied from
	sites API for future data parcing. Also it is made in such manner to avoid CAPTCHA, 
	though not always succesful. So, if site has CAPTCHA implemented and it noticed
	our small bot -  you should pass a test... Nothing to do with it.
	
	Input data for func is dict key =_name given to page_, value =_page's url_
	'''
	 
	start_time = time.time()
	
	#here load strategy may be chosen. Default is standard strategy. It is more like human.
	options = Options()
	'''options.page_load_strategy = "eager"'''
	
	#making random user agent for webdriver broswer
	ua = UserAgent()
	userAgent = ua.random
	print(userAgent)
	options.add_argument(f'user-agent={userAgent}')
	
	#charging profile. Programm is using your own browser profile. If trying to use flase
	# profile - CAPTCHA will easily notice a bot.
	#"/home/linp/.mozilla/firefox/xjlukkfp.default-release" - firefox profile path
	# with just "()" it also use your default profile
	profile = webdriver.FirefoxProfile()
	print(webdriver.FirefoxProfile())
	PROXY_HOST = "51.05.23.594"
	PROXY_PORT = "6142"
	profile.set_preference("network.proxy.type", 1)
	profile.set_preference("network.proxy.http", PROXY_HOST)
	profile.set_preference("network.proxy.http_port", int(PROXY_PORT))
	profile.set_preference("dom.webdriver.enabled", False)
	profile.set_preference('useAutomationExtension', False)
	profile.update_preferences()
	
	#launching webdriver browser
	driver = webdriver.Firefox(firefox_options=options, firefox_profile=profile)
	driver.maximize_window()
	
	j = 0
	f = open("ttspage6.html", "w")
	for i in pages_dict:
		ttspage = "div>"
		while len(ttspage.split("div")) < 100:
			#changing userAgent
			userAgent = ua.random
			options.add_argument(f'user-agent={userAgent}')
			print(userAgent)
			#gettig page
			time.sleep(random.uniform(1, 2))
			print("--- %s seconds ---" % (time.time() - start_time))
			driver.get(pages_dict.get(i))
			time.sleep(random.uniform(2, 3))
			print("--- %s seconds ---" % (time.time() - start_time))
			#cut the page to get only half after <search-result-view>
			element = driver.find_element_by_id("search-result-view")
			#getting html from a page
			ttspage = element.get_attribute("outerHTML")
			#print(ttspage)
			print(len(ttspage.split("div")), j)
			j += 1
			#this if statement is added ONLY to give possibility and time
			# to pass CAPTCHA test. There are not too many ways to bypass it.
			# We can wait when some of false user Agents work and went throut,
			# but in half of all cases it takes too much time. Easier to pass CAPTCHA test.
			if len(ttspage.split("div")) < 100:
				print("<>ATTENTION!<> Most likely CAPTCHA noticed the bot. Pass a test, please, and after press ENTER in Terminal")
				input()
		print(f'------------------------------------{i}------------------------------------------')
		f.write(ttspage)
	
	print("Done.")
	
	driver.quit()

if __name__ == "main":
	get_pages(pages_dict)
