import json
import eel
import datetime
import requests

@eel.expose
def check_for_updates():
    version = "1.3"
    url = "https://raw.githubusercontent.com/Timurkaaaaaaa/GOS-Pamyatka/refs/heads/main/version.json"
    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()
        print(json_data['version'])
        if json_data['version'] != version:
            return -1
        else:
            return 0

def search_in_json1(search_query):
    with open("Ugolovka.json", 'r', encoding='utf-8') as file:
        data = json.load(file)

    results = []
    # Ищем по всем текстам в JSON
    for key, value in data.items():
        if search_query.lower() in value['text'].lower() or search_query.lower() in key:
            print(key)
            key1 = "УК " + key
            results.append({
                'key': key1,
                'text': value['text'],
                'wanted': value['wanted'],
                'punishment': value['punishment']
            })

    for result in results:
        if result['wanted']=="1":
            result['wanted'] = "★"
        elif result['wanted']=="2":
            result['wanted'] = "★★"
        elif result['wanted']=="3":
            result['wanted'] = "★★★"
        elif result['wanted']=="4":
            result['wanted'] = "★★★★"
        elif result['wanted']=="5":
            result['wanted'] = "★★★★★"

    return results

def search_in_json2(search_query):
    with open("Administrativka.json", 'r', encoding='utf-8') as file:
        data = json.load(file)

    results = []
    for key, value in data.items():
        if search_query.lower() in value['text'].lower() or search_query.lower() in key:
            key1 = "АК " + key
            results.append({
                'key': key1,
                'text': value['text'],
                'punishment': value['punishment'],
                'wanted': ''
            })

    return results

def search_in_json3(search_query):
    with open("Dorojka.json", 'r', encoding='utf-8') as file:
        data = json.load(file)

    results = []
    for key, value in data.items():
        if search_query.lower() in value['text'].lower() or search_query.lower() in (key + "ДК"):
            key1 = "ДК " + key
            results.append({
                'key': key1,
                'text': value['text'],
                'punishment': value['punishment'],
                'wanted': ''
            })

    return results

@eel.expose
def choice(search_query: str):
    results1 = search_in_json1(search_query)
    results2 = search_in_json2(search_query)
    results3 = search_in_json3(search_query)

    results = results1 + results2 + results3

    return results




eel.init('gui')
eel.start('index.html')
