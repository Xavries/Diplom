''''This script gets Unit price, Amount and Place from item page (deepest page)'''

f = open('item_page.html', 'r')
t = f.read().split()
f.close()

#print(t)

for i in t:
	if i == 'Unit':
		print(i, t[t.index(i)+1], '=', t[t.index(i)+12])
	if i == 'Amount':
		print(i, '=', t[t.index(i)+10])
	if i == 'Listed':
		for i in t[t.index(i):t.index(i)+10]:
			print(i, end=' ')
