import sqlite3

sql_conn = sqlite3.connect('tts_urls.sqlite')

cursor = sql_conn.cursor()

pages_dict = {}
urls_list = []

for element in cursor.execute('SELECT urls.url || items.item_price FROM urls INNER JOIN items ON item_name = url_name;'):
	print(element[0], '\n')
	urls_list.append(element[0])

p = 0

for element in cursor.execute('SELECT items.item_name FROM items;'):
	print(element[0], '\n')
	pages_dict[element[0]] = urls_list[p]
	p+=1
	
print(pages_dict)


pages_dict0 = {"Chromium Plating":"https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=18124&ItemNamePattern=Chromium+Plating&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=130000", 
 "Zircon Plating":"https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=17799&ItemNamePattern=Zircon+Plating&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=35000", 
 "Potent Nirncrux":"https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=3790&ItemNamePattern=Potent+Nirncrux&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=21000", 
 "Prefect Roe":"https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=6132&ItemNamePattern=Perfect+Roe&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=21000",
 "Hakejio":"https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=4794&ItemNamePattern=Hakeijo&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=32500", 
 "Dreugh Wax":"https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=211&ItemNamePattern=Dreugh+Wax&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=12000", 
 "Tempering Alloy":"https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=5687&ItemNamePattern=Tempering+Alloy&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=6000"}
