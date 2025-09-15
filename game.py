import random

import mysql.connector

yhteys = mysql.connector.connect(
    host='localhost',
    port=3307,
    database='flight_game',
    user='root',
    password='mikasana',
    autocommit=True
)


def kysymys():
    sql = f"SELECT name FROM airport ORDER BY RAND() LIMIT 1"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    for rivi in tulos:
        return rivi
    return None

def oikea_vastaus(i):
    sql = f"SELECT name FROM country WHERE iso_country in(SELECT iso_country FROM airport WHERE name = '{i}')"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    for rivi in tulos:
        return rivi
    return None

def vaara_vastaus(i):
    sql = f"SELECT name FROM country WHERE NOT name = '{i}' ORDER BY RAND() LIMIT 1"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    for rivi in tulos:
        return rivi
    return None


print("Welcome to 'Who Wants to be a Millionaire?' Airport Edition!")
username = input('Enter your username: ')

print(f"Alright, {username}! Your first question is...")
question = kysymys()

answer = oikea_vastaus(question)

wrong_answer1 = vaara_vastaus(answer)
wrong_answer2 = vaara_vastaus(answer)
wrong_answer3 = vaara_vastaus(answer)

vastauslista = [answer, wrong_answer1, wrong_answer2, wrong_answer3]
random.shuffle(vastauslista)

print(f"Which country is {question} located in?")

print(f"A. {vastauslista[0]}")
print(f"B. {vastauslista[1]}")
print(f"C. {vastauslista[2]}")
print(f"D. {vastauslista[3]}")

vastaus = input("Your answer: ")
if vastaus == "A":
    if vastauslista[0] == answer:
        print("Correct answer!")
    else:
        print(f"Wrong answer, the correct answer was {answer}.")
elif vastaus == "B":
    if vastauslista[1] == answer:
        print("Correct answer!")
    else:
        print(f"Wrong answer, the correct answer was {answer}.")
elif vastaus == "C":
    if vastauslista[2] == answer:
        print("Correct answer!")
    else:
        print(f"Wrong answer, the correct answer was {answer}.")
elif vastaus == "D":
    if vastauslista[3] == answer:
        print("Correct answer!")
    else:
        print(f"Wrong answer, the correct answer was {answer}.")