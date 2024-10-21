# app/helpers/get_last_names.py
import json

def get_last_names(lang="ES"):
    try:
        with open(f'app/ASSETS/DATA/{lang}/last_names.json', 'r', encoding='utf-8') as file:
            names = json.load(file)
        return names['last_names']
    except Exception as e:
        #print(f"Error al cargar nombres en {lang}: {str(e)}")
        return ["NN"]
