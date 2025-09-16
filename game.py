import random

import mysql.connector

#SQL yhteys
yhteys = mysql.connector.connect(
    host='localhost',
    port=3307,
    database='flight_game',
    user='root',
    password='mikasana',
    autocommit=True
)

#Haetaan tietokannasta kysyttävän lentokentän nimi randomisti
def kysymys():
    sql = f"SELECT name FROM airport ORDER BY RAND() LIMIT 1"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    for rivi in tulos:
        return rivi
    return None

#Haetaan kysymyksen lentokenttää vastaavan maan nimi
def oikea_vastaus(i):
    sql = f"SELECT name FROM country WHERE iso_country in(SELECT iso_country FROM airport WHERE name = '{i}')"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    for rivi in tulos:
        return rivi
    return None

#Haetaan maa joka ei ole oikea vastaus
def vaara_vastaus(i):
    sql = f"SELECT name FROM country WHERE NOT name = '{i}' ORDER BY RAND() LIMIT 1"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    for rivi in tulos:
        return rivi
    return None

#Alkuteksti
print("Welcome to 'Who Wants to be a Millionaire?' Airport Edition!")
username = input('Enter your username: ')

#Muuttuja joka määrittää kysytäänkö kysymyksiä
game_over = False
money = 0
round = 0

print(f"Alright, {username}! Your first question is...")

#Loop joka kysyy kysymyksiä kunnes yksi menee väärin
while game_over == False:
    #Haetaan kysymykseen data
    question = kysymys()

    #Haetaan oikeaan vastaukseen data
    answer = oikea_vastaus(question)

    #Haetaan väärä vastaus kolme kertaa
    wrong_answer1 = vaara_vastaus(answer)
    wrong_answer2 = vaara_vastaus(answer)
    wrong_answer3 = vaara_vastaus(answer)

    #Luodaan lista vastauksista
    vastauslista = [answer, wrong_answer1, wrong_answer2, wrong_answer3]
    #Sekoitetaan vastaukset
    random.shuffle(vastauslista)

    #Printataan kysymys ja vastaukset
    round += 1
    print(f"Which country is {question} located in?")

    print(f"A. {vastauslista[0]}")
    print(f"B. {vastauslista[1]}")
    print(f"C. {vastauslista[2]}")
    print(f"D. {vastauslista[3]}")

    #Käyttäjän vastauskenttä
    vastaus = input("Your answer: ")

    #Tarkastetaan vastasiko käyttäjä oikein
    if vastaus == "A":
        if vastauslista[0] == answer:
            print("Correct answer!")
            reward = 100 * round
            money = money + reward
            print(f"You have earned ${reward}! You now have ${money}!")
            print("Your next question is...")
        else:
            print(f"Wrong answer, the correct answer was {answer}.")
            game_over = True
    elif vastaus == "B":
        if vastauslista[1] == answer:
            print("Correct answer!")
            reward = 100 * round
            money = money + reward
            print(f"You have earned ${reward}! You now have ${money}!")
            print("Your next question is...")
        else:
            print(f"Wrong answer, the correct answer was {answer}.")
            game_over = True
    elif vastaus == "C":
        if vastauslista[2] == answer:
            print("Correct answer!")
            reward = 100 * round
            money = money + reward
            print(f"You have earned ${reward}! You now have ${money}!")
            print("Your next question is...")
        else:
            print(f"Wrong answer, the correct answer was {answer}.")
            game_over = True
    elif vastaus == "D":
        if vastauslista[3] == answer:
            print("Correct answer!")
            reward = 100 * round
            money = money + reward
            print(f"You have earned ${reward}! You now have ${money}!")
            print("Your next question is...")
        else:
            print(f"Wrong answer, the correct answer was {answer}.")
            game_over = True
    else:
        print("Error")
        game_over = True
print("Game over")