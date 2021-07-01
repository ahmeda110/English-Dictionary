from difflib import get_close_matches as GCM
from re import X
import mysql.connector as SQL
#import json as JSON


# CONNECTION TO DATABASE
my_db = SQL.connect(
    host = "108.167.140.122",
    user = "ardit700_student",
    password = "ardit700_student",
    database = "ardit700_pm1database"
)


wanted_word = input('\nWord: ')


# COLLECTING NEEDED INFORMATION FROM THE DATABASE
def collect_from_database(command):
    my_cursor = my_db.cursor()
    my_cursor.execute(command)
    result = my_cursor.fetchall()
    return result


# fORMATTING OUTPUT WHEN WORD FOUND (IF) OR WHEN SIMILAR FOUND (ELIF)
def formatted_definition(key):
    my_str = f'\nBelow are the defenition(s) found for \'{key}\':\n'
    for item in collect_from_database(
            f"SELECT * FROM Dictionary WHERE Expression = '{key.lower() or key.upper() or key.capitalize()}'"):
        my_str += f'\t- {item[1]}\n'
    print(my_str)



# IF WORD FOUND IN DATABASE
if collect_from_database(
    f"SELECT * FROM Dictionary WHERE Expression = '{wanted_word.lower() or wanted_word.upper() or wanted_word.capitalize()}'"):
    formatted_definition(wanted_word) 


# IF NOT FOUND IN DATABASE -> LOOK FOR SIMILAR KEYS IN DATABASE
elif len(GCM(wanted_word, dict(collect_from_database("SELECT * FROM Dictionary")).keys())) > 0:
    all_keys = dict(collect_from_database("SELECT * FROM Dictionary")).keys()
    response = input(f'Did you mean {GCM(wanted_word, all_keys)[0]}? (Y/N) ')
    action = GCM(wanted_word, all_keys)[0] if response == 'Y' else 'Word DNE'
    formatted_definition(action)

# FINALLY IF NOTHING FOUND -> PRINT NOTHING FOUND
else:
    print(f'\nHmmm, no defenition found for \'{wanted_word}\' \n')


# WORKING WITH A JSON FILE APPROACH
"""
wanted_word = input('\nWord: ')
my_data = JSON.load(open('./data.json', 'r'))

def formatted_definition(key):
        str = f'\nDefinitions found for \'{key}\':\n'
        for item in my_data[key]:
            str += f'\t- {item}\n'
        return str

def get_definition(key):
    if key in my_data:
        return formatted_definition(key)  
    elif key.capitalize() in my_data:
        return formatted_definition(key.capitalize()) 
    elif key.upper() in my_data:
        return formatted_definition(key.upper()) 
    elif len(GCM(key, my_data.keys())) > 0:
        response = input(f'Did you mean {GCM(key, my_data.keys())[0]}? (Y/N) ')
        action = GCM(key, my_data.keys())[0] if response == 'Y' else 'Word DNE'
        return formatted_definition(action) 
    else:
        return f'\nHmmm, no defenition found for \'{key}\' \n'
    
print(get_definition(wanted_word.lower()))
"""