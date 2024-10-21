# app/helpers/rnd_person_genrator.py
from app.models.person import Person
from app.helpers.get_male_names import get_male_names
from app.helpers.get_male_compound_names import get_male_compound_names
from app.helpers.get_female_names import get_female_names
from app.helpers.get_female_compound_names import get_female_compound_names
import random

def _get_rnd_male_single_name(lang):
    return random.choice(get_male_names(lang))

def _get_rnd_male_compound_name(lang):
    return random.choice(get_male_compound_names(lang))

def _get_rnd_female_single_name(lang):
    return random.choice(get_female_names(lang))

def _get_rnd_female_compound_name(lang):
    return random.choice(get_female_compound_names(lang))

def rnd_person_genrator(sex="", lang="ES"):
    rndPerson = Person(777)

    # 50-50 sex
    if sex == "":
        _isMale = True if random.randint(0, 1) == 1 else False
        if _isMale:
            rndPerson.sex = "MALE"
        else:
            rndPerson.sex = "FEMALE"
    else:
        rndPerson.sex = sex
    
    # 40% of person HAV single name
    _isSingleName = False if random.randint(0, 100) <= 40 else True
    if _isSingleName:
        if rndPerson.sex == "MALE":
            rndPerson.first_name = _get_rnd_male_single_name(lang)
        else:
            rndPerson.first_name = _get_rnd_female_single_name(lang)
    else:
        if rndPerson.sex == "MALE":
            _cmName = _get_rnd_male_compound_name(lang)
            _cmName = _cmName.split(" ")
            rndPerson.first_name = _cmName[0]
            rndPerson.middle_name = _cmName[1]
        else:
            _cmName = _get_rnd_female_compound_name(lang)
            _cmName = _cmName.split(" ")
            rndPerson.first_name = _cmName[0]
            rndPerson.middle_name = _cmName[1]

    return rndPerson
