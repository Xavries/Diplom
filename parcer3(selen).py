import sqlite3

sql_conn = sqlite3.connect('tts_urls.sqlite')
cursor = sql_conn.cursor()
itemst = []

for element in cursor.execute('SELECT items.item_name FROM items;'):
	itemst.append(element[0])

print(itemst)

f = open("ttspage6.html", "r")
t1 = f.read().split('"')
f.close()

for i in t1:
	if i == '''itemQualityClass: QualityID,
                                    text: Name''':
		print(t1[t1.index(i)+3][1:len(itemst[0])+1], end=' ><><')
		t1.pop(t1.index(i))
	if i == "text: StringResource['TraderLocation' + DBData.GuildKioskLocation[GuildKioskLocationID]]":
		print(t1[t1.index(i)+1][1:len(itemst[0])+1], end=' ><><')
		t1.pop(t1.index(i))
	if i == "text: GuildName":
		print(t1[t1.index(i)+1][1:len(itemst[0])+1], end=' ><><')
		t1.pop(t1.index(i))
	if i == "localizedNumber: UnitPrice":
		print(t1[t1.index(i)+1][1:len(itemst[0])-5], end=' ><><')
		t1.pop(t1.index(i))
	if i == "localizedNumber: Amount":
		print(t1[t1.index(i)+1][1:len(itemst[0])-7], end=' ><><')
		t1.pop(t1.index(i))
	if i == "localizedNumber: TotalPrice":
		print(t1[t1.index(i)+1][1:len(itemst[0])-2], end=' ><><')
		t1.pop(t1.index(i))
	if i == "minutesElapsed: DiscoverUnixTime":
		print(t1[t1.index(i)+1][1:len(itemst[0])], end='\n \n')
		t1.pop(t1.index(i))

