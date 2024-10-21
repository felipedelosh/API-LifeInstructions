# app/helpers/get_male_names.py
import json

def get_female_compound_names(lang="ES"):
    try:
        with open(f'app/ASSETS/DATA/{lang}/female_compound_names.json', 'r', encoding='utf-8') as file:
            names = json.load(file)
        return names['female_compound_names']
    except Exception as e:
        #print(f"Error al cargar nombres en {lang}: {str(e)}")
        return ["NN NN"]
