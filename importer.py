import os
import requests
import time

if not os.path.exists("json/"):
    os.mkdir("json/")
    print("json Directory Created ")

ShortAttack = 'https://raw.githubusercontent.com/Micha854/pogoProtos/master/ShortAttack.json'
r = requests.get(ShortAttack, allow_redirects=True)
if open('json/ShortAttack.json', 'wb').write(r.content):
    try:
        print("ShortAttack has been updated")
        time.sleep(1)
    except:
        print("could not update ShortAttack")
        time.sleep(1)

LoadAttack = 'https://raw.githubusercontent.com/Micha854/pogoProtos/master/LoadAttack.json'
r = requests.get(LoadAttack, allow_redirects=True)
if open('json/LoadAttack.json', 'wb').write(r.content):
    try:
        print("LoadAttack has been updated")
        time.sleep(1)
    except:
        print("could not update LoadAttack")
        time.sleep(1)

Pokemon = 'https://raw.githubusercontent.com/Micha854/pogoProtos/master/Pokemon.json'
r = requests.get(Pokemon, allow_redirects=True)
if open('json/Pokemon.json', 'wb').write(r.content):
    try:
        print("Pokemon has been updated")
        time.sleep(1)
    except:
        print("could not update Pokemon")
        time.sleep(1)

Form = 'https://raw.githubusercontent.com/Micha854/pogoProtos/master/Form.json'
r = requests.get(Form, allow_redirects=True)
if open('json/Form.json', 'wb').write(r.content):
    try:
        print("Form has been updated")
        time.sleep(1)
    except:
        print("could not update Form")
        time.sleep(1)

Costume = 'https://raw.githubusercontent.com/Micha854/pogoProtos/master/Costume.json'
r = requests.get(Costume, allow_redirects=True)
if open('json/Costume.json', 'wb').write(r.content):
    try:
        print("Costume has been updated")
        time.sleep(1)
    except:
        print("could not update Costume")
        time.sleep(1)