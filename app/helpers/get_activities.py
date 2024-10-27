# app/helpers/get_activities.py
import json

def get_activities(lang="ES"):
    try:
        with open(f'app/ASSETS/DATA/{lang}/actions.json', 'r', encoding='utf-8') as file:
            names = json.load(file)
        return names['actions']
    except Exception as e:
        #print(f"Error al cargar nombres en {lang}: {str(e)}")
        return []