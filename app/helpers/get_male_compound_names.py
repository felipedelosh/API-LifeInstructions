# app/helpers/get_male_compound_names.py
import json

def get_male_compound_names(lang="ES"):
    try:
        with open(f'app/ASSETS/DATA/{lang}/male_compound_names.json', 'r', encoding='utf-8') as file:
            names = json.load(file)
        return names['male_compound_names']
    except Exception as e:
        #print(f"Error al cargar nombres en {lang}: {str(e)}")
        return ["NN NN"]
