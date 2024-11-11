from fuzzywuzzy import fuzz
import ugolovniy_kodeks
#import administrativniy_kodeks
#import dorojniy_kodeks
import eel
import datetime

def find_article(query):
    # Приводим запрос к нижнему регистру для нечеткого сравнения
    query = query.lower()
    
    rc = {'query': '', 'percent': 50}
    for c, v in ugolovniy_kodeks.VA_LIST.items():
        for x in v:
            vrt = fuzz.ratio(query, x)
            if vrt > rc['percent']:
                rc['query'] = c
                rc['percent'] = vrt

    ans = rc['query']
    
    return ans

@eel.expose
def choice(input_text: str):
    print(input_text)
    article = find_article(input_text)
    print(f"Наиболее подходящая статья: {article}")
    article_wanted = ugolovniy_kodeks.VA__LIST[article][1]
    article_desp = ugolovniy_kodeks.VA__LIST[article][0]
    article = str(article)
    article = "<br>Статья " + article + " " + article_wanted + "<br>"
    article = "<center><h3><strong>" + article + "</h3><strong></center>"
    article = article + article_desp +"<br><br>"
    return str(article)






def find_article2(query):
    # Приводим запрос к нижнему регистру для нечеткого сравнения
    query = query.lower()
    
    rc = {'query': '', 'percent': 50}
    for c, v in administrativniy_kodeks.VA_LIST.items():
        for x in v:
            vrt = fuzz.ratio(query, x)
            if vrt > rc['percent']:
                rc['query'] = c
                rc['percent'] = vrt

    ans = rc['query']
    
    return ans

@eel.expose
def choice2(input_text: str):
    print(input_text)
    article = find_article2(input_text)
    print(f"Наиболее подходящая статья: {article}")
    article_desp = administrativniy_kodeks.VA__LIST[article][0]
    article = "<center><h3><strong>" + article + "</h3><strong></center><br>"
    article = article + article_desp
    return str(article)





def find_article3(query):
    # Приводим запрос к нижнему регистру для нечеткого сравнения
    query = query.lower()
    
    rc = {'query': '', 'percent': 50}
    for c, v in dorojniy_kodeks.VA_LIST.items():
        for x in v:
            vrt = fuzz.ratio(query, x)
            if vrt > rc['percent']:
                rc['query'] = c
                rc['percent'] = vrt

    ans = rc['query']
    
    return ans

@eel.expose
def choice3(input_text: str):
    print(input_text)
    article = find_article3(input_text)
    print(f"Наиболее подходящая статья: {article}")
    article_desp = dorojniy_kodeks.VA__LIST[article][0]
    article = "<center><h3><strong>" + article + "</h3><strong></center><br>"
    article = article + article_desp
    return str(article)


eel.init('gui')
eel.start('index.html')
