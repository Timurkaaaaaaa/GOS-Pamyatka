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
        if search_query.lower() in value['text'].lower():  # Поиск без учета регистра
            results.append({
                'key': key,
                'text': value['text'],
                'wanted': value['wanted'],
                'punishment': value['punishment']
            })

    return results

@eel.expose
def choice(search_query: str):
    results = search_in_json(search_query, json_file_path)
    return results




eel.init('gui')
eel.start('index.html')
