import queue
import threading, time, random
import sqlite3
from get_page import get_pages
from parcer import tts_table

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

#get_pages(pages_dict)
t = threading.Thread(target = get_pages(pages_dict))
t.start()
while t.isAlive():
    pass

tts_table()

