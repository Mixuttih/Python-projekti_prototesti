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
    sql = f"SELECT iso_country FROM airport WHERE name = {i}"
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
print(f"Which country is {question} located in?")
print(f"{answer}")
