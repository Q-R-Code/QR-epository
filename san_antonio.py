# -*- coding: utf8 -*-
import random

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes!",
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre.",
    "l'habit ne fait pas le moine"
]
characters = [
    "Alvin et les Chipmunks",
    "Babar",
    "Betty boop",
    "calimero",
    "Casper",
    "Le chat potté",
    "kirikou"
]

def message(character, quote):
    n_character = character.capitalize()
    n_quote = quote.capitalize()
    return "{} a dit: {}".format(n_character, n_quote)

def show_random_quote(my_list):
    random_quote = random.randint(0, len(my_list) -1)
    quote = my_list[random_quote]
    # print(quote)
    return quote



#Programm

print("B I E N V E N U E !")

user_answer = input("Appuyez sur entrée pour connaitre une citation.")

while user_answer !="B" :
  print(message(show_random_quote(characters),show_random_quote(quotes)))
  user_answer = input("Tapez entrée pour connaitre une autre citation ou B pour quitter le programme")

if user_answer == "B":
    print("Merci de votre visite, à bientôt!")
    print("A U   R E V O I R !")







