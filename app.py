#!/usr/bin/python3
import random
import pprint
from pyfiglet import Figlet
from pymongo import MongoClient

mongo_uri = '<url de tu base de datos mongodb>'
client = MongoClient(mongo_uri)

db = client['pypassword']   # nombre de la base de datos
collection = db['mypass']   # coleccion de la db

print('')
custom_fig1 = Figlet(font='digital')
custom_fig2 = Figlet(font='hex')
print(custom_fig1.renderText('save yor password!!!!'))

print("by: https://github.com/Davidf98")
print('')


def opc():
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input("elije una opcion: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero valido')
            print('')

    return num


salir = False
opcion = 0

while not salir:
    print('1. Save password')
    print('2. Generate password')
    print('3. My password lists')
    print('4. Exit')
    print('')
    # print('Elije una opcion')

    opcion = opc()

    if opcion == 1:
        print('')
        print('Save password')
        cuenta = input('acount: ')
        user = input('user: ')
        pass_g = input('password: ')

        # campos a guardar
        collection.insert_one({"acount": cuenta, "user": user, "pass": pass_g})
        print('')

    elif opcion == 2:
        print('')
        print('Generate yor password')
        valor = int(input('number of characters: '))
        password_length = valor
        possible_characters = "abcdefghijklmnopqrstuvwxyz1234567890!_-$#."
        random_character_list = [random.choice(possible_characters) for i in range(password_length)]
        random_password = "".join(random_character_list)
        print('password: '+random_password)
        print('')

    elif opcion == 3:
        print('')
        print('my password list')
        # pprint.pprint(collection.find_one()) #para un solo elemento
        # listar contraseñas guardadas
        for post in collection.find({}, {'_id': 0}):    # para muchos elementos
            pprint.pprint(post)
            print('')

    elif opcion == 4:
        salir = True

    else:
        print('Introduce un numero entre 1 y 3')
