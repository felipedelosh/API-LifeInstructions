# app/helpers/get_plausible_death.py
import json

def get_plausible_death(lang="ES"):
    try:
        with open(f'app/ASSETS/DATA/{lang}/deaths.json', 'r', encoding='utf-8') as file:
            names = json.load(file)
        return names['deaths']
    except Exception as e:
        #print(f"Error al cargar nombres en {lang}: {str(e)}")
        return ["NATURAL"]