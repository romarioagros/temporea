
import json
from pprint import pprint
with open("newsfr.json",encoding="utf-8" ) as file:
    news_file=json.load(file)
   # pprint (news_file)
    
s=[] 
    
categ1=news_file['rss']['channel']['item']
for line in categ1 : 
    mas=line['description']['__cdata'].split()
    for row in mas:
        s.append(row)
        
suma=[]
for row in s:
    if row not in suma and len(row)>6:
        suma.append(row)

listok=[]
dict_temp = {}
for row in suma:
    temp = s.count(row)
    dict_temp[row] = temp
    listok.append(temp)

listok.sort()
listok_new = listok[-10:]
#listok_new=listok_new[0:-10]
for row in dict_temp:
    if dict_temp[row] in listok_new:
        print ('"' ,row ,'"',"данное слово встречается  -" ,  dict_temp[row] , "раз" )