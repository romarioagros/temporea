
# -*- coding: utf-8 -*-cod


cook_book = {
    'Омлет': {
        'name': 'Омлет',
        'type': '2-е',
        'ingridients': [
                {'product' : 'Яйца', 'quantity': 2, 'unit': 'шт'},
                {'product' : 'Молоко', 'quantity': 50, 'unit': 'мл'},
                {'product' : 'Помидор', 'quantity': 100, 'unit': 'г'},
        ]
    }, 
    'Яблочный пирог': { 
        'name': 'Яблочный пирог',
        'type': 'Десерт',
        'ingridients': [
                {'product' : 'Яйца', 'quantity': 1, 'unit': 'шт'},
                {'product' : 'Мука', 'quantity': 300, 'unit': 'г'},
                {'product' : 'Масло', 'quantity': 60, 'unit': 'г'},
                {'product' : 'Яблоки', 'quantity': 80, 'unit': 'г'},
        ]
    },
    'Суп': {
        'name': 'Суп',
        'type': '1-е',
        'ingridients': [
                {'product' : 'Вода', 'quantity': 100, 'unit': 'мл'},
                {'product' : 'Помидор', 'quantity': 300, 'unit': 'г'},
        ]
    }, 
}


import json
from pprint import pprint
with open("cook_book9.json" , "w", encoding="utf-8") as f:
    json.dump(cook_book,f,)



#json.dump(cook_book,f,ensure_ascii=False)
