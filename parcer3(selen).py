import random
f = open("ttspage1.html", "r")
t = f.read().split("div")
f.close()
'''
k=4
while len(t)>k:
	print(t[k], '\n', k)
	k+=1
'''
#first way of getting data
itemst = ['Chromium Plating', 'Zircon Plating', 'Potent Nirncrux', 'Perfect Roe', 'Hakeijo', 'Dreugh Wax', 'Tempering Alloy']
'''
n = 0
b = 140
for i in itemst:
	print('\n', f"------------------<<<{i}>>----------------------- {n}, {b}", '\n')
	while n < b:
		print(t[4+n][119:], '\n', t[10+n][101:], '\n', t[12+n][28:],'\n', t[13+n][165:190], '\n', t[15+n][61:72], '\n', t[17+n][60:85], '\n', t[17+n][283:300], '\n')
		n += 14
	n += 22
	b += 162
'''

f = open("ttspage5.html", "r")
t1 = f.read().split('"')
f.close()

#second way of getting data

for i in t1:
	if i == '''itemQualityClass: QualityID,
                                    text: Name''':
		print(t1[t1.index(i)+3][1:len(itemst[0])+1])
		t1.pop(t1.index(i))
	if i == "text: StringResource['TraderLocation' + DBData.GuildKioskLocation[GuildKioskLocationID]]":
		print(t1[t1.index(i)+1][:30])
		t1.pop(t1.index(i))
	if i == "text: GuildName":
		print(t1[t1.index(i)+1][1:len(itemst[0])+1])
		t1.pop(t1.index(i))
	if i == "localizedNumber: UnitPrice":
		print(t1[t1.index(i)+1][1:len(itemst[0])])
		t1.pop(t1.index(i))
	if i == "localizedNumber: Amount":
		print(t1[t1.index(i)+1][1:len(itemst[0])])
		t1.pop(t1.index(i))
	if i == "localizedNumber: TotalPrice":
		print(t1[t1.index(i)+1][1:len(itemst[0])])
		t1.pop(t1.index(i))
	if i == "minutesElapsed: DiscoverUnixTime":
		print(t1[t1.index(i)+1][1:len(itemst[0])])
		t1.pop(t1.index(i))

