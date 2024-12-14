import json
import eel
import datetime


json_file_path = "Ugolovka.json"

def search_in_json(search_query, json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    results = []
    # Ищем по всем текстам в JSON
    for key, value in data.items():
        if search_query.lower() in value['text'].lower() or search_query.lower() == key:
            key1 = "УК " + key
            results.append({
                'key': key1,
                'text': value['text'],
                'wanted': value['wanted'],
                'punishment': value['punishment']
            })

    return results

@eel.expose
def choice(search_query: str):
    results = search_in_json(search_query, json_file_path)
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




eel.init('gui')
eel.start('index.html')
