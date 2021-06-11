import sqlite3
import webbrowser

sql_conn = sqlite3.connect('tts_urls.sqlite')
cursor = sql_conn.cursor()
itemst = []

for element in cursor.execute('SELECT items.item_name FROM items;'):
	itemst.append(element[0])

print(itemst)

f = open("ttspage6.html", "r")
t = f.read().split('<')
f.close()

f = open("ttspage_edited.html", "w")

for i in t:
	if 'img' in i:
		t.pop(t.index(i))
		print('img')
		continue
	'''if 'CurrentPage' in i:
		t.pop(t.index(i))
		print('CurrentPage')
		continue'''
	'''elif 'Hour' in i:
		j = 500
		g = t.index(i)
		while j > 0:
			t.pop(g-j)
			j -= 1
		print('hour')
		continue'''
	f.write('<'+i)
	print(i)

f.close()

webbrowser.open_new_tab('/home/linp/Beetroot/diplom/ttspage_edited.html')
