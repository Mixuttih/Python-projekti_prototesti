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

#Helppo kysymys: Haetaan tietokannasta kysyttävän lentokentän nimi randomisti
def helppo_kysymys():
    sql = f"SELECT name FROM airport ORDER BY RAND() LIMIT 1"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    for rivi in tulos:
        return rivi
    return None

#Haetaan kysymyksen lentokenttää vastaavan maan nimi
def helppo_oikea_vastaus(i):
    sql = f"SELECT name FROM country WHERE iso_country in(SELECT iso_country FROM airport WHERE name = '{i}')"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    for rivi in tulos:
        return rivi
    return None

#Haetaan maa joka ei ole oikea vastaus
def helppo_vaara_vastaus(i):
    sql = f"SELECT name FROM country WHERE NOT name = '{i}' ORDER BY RAND() LIMIT 1"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    for rivi in tulos:
        return rivi
    return None

#Keskivaikea kysymys: Haetaan tietokannasta kysyttävän lentokentän nimi randomisti
def keski_kysymys():
    sql = f"SELECT name FROM airport ORDER BY RAND() LIMIT 1"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    for rivi in tulos:
        return rivi
    return None

#Haetaan kysymyksen lentokenttää vastaavan ICAO -koodi
def keski_oikea_vastaus(i):
    sql = f"SELECT ident FROM airport WHERE name = '{i}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    for rivi in tulos:
        return rivi
    return None

#Haetaan ICAO -koodi joka ei ole oikea vastaus
def keski_vaara_vastaus(i):
    sql = f"SELECT ident FROM airport WHERE NOT ident = '{i}' ORDER BY RAND() LIMIT 1"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    for rivi in tulos:
        return rivi
    return None

#Vaikea kysymys: Haetaan ICAO -koodi
def vaikea_kysymys():
    sql = f"SELECT ident FROM airport ORDER BY RAND() LIMIT 1"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    for rivi in tulos:
        return rivi
    return None

#Haetaan kysymyksen koodia vastaavan lentokentän nimi
def vaikea_oikea_vastaus(i):
    sql = f"SELECT name FROM airport WHERE ident = '{i}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    for rivi in tulos:
        return rivi
    return None

#Haetaan lentokentän nimi joka ei ole oikea vastaus
def vaikea_vaara_vastaus(i):
    sql = f"SELECT name FROM airport WHERE NOT name = '{i}' ORDER BY RAND() LIMIT 1"
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

#Pelaajan raha ja edistyminen
money = 0
current_round = 0

print(f"Welcome, {username}! Let's play!")

#Loop joka kysyy kysymyksiä kunnes yksi menee väärin
while game_over == False:
    current_round += 1
    if current_round <= 5:
        #Haetaan helppoon kysymykseen data
        question = helppo_kysymys()

        #Haetaan oikeaan vastaukseen data
        answer = helppo_oikea_vastaus(question)

        #Haetaan väärä vastaus kolme kertaa
        wrong_answer1 = helppo_vaara_vastaus(answer)
        wrong_answer2 = helppo_vaara_vastaus(answer)
        wrong_answer3 = helppo_vaara_vastaus(answer)
    elif 5 < current_round <= 10:
        # Haetaan keskivaikeaan kysymykseen data
        question = keski_kysymys()

        # Haetaan oikeaan vastaukseen data
        answer = keski_oikea_vastaus(question)

        # Haetaan väärä vastaus kolme kertaa
        wrong_answer1 = keski_vaara_vastaus(answer)
        wrong_answer2 = keski_vaara_vastaus(answer)
        wrong_answer3 = keski_vaara_vastaus(answer)
    elif 10 < current_round <= 15:
        # Haetaan vaikeaan kysymykseen data
        question = vaikea_kysymys()

        # Haetaan oikeaan vastaukseen data
        answer = vaikea_oikea_vastaus(question)

        # Haetaan väärä vastaus kolme kertaa
        wrong_answer1 = vaikea_vaara_vastaus(answer)
        wrong_answer2 = vaikea_vaara_vastaus(answer)
        wrong_answer3 = vaikea_vaara_vastaus(answer)

    #Luodaan lista vastauksista
    vastauslista = [answer, wrong_answer1, wrong_answer2, wrong_answer3]
    #Sekoitetaan vastaukset
    random.shuffle(vastauslista)

    #Printataan kysymys ja vastaukset
    print(f"Round {current_round}: This question is worth ${100 * current_round}!")
    print("Your question is...")
    if current_round <= 5:
        print(f"Which country is {question} located in?")
    elif 5 < current_round <= 10:
        print(f"Which ICAO code is for {question}?")
    elif 10 < current_round <= 15:
        print(f"Which airport is {question} code for?")
    elif current_round == 16:
        print(f"You win! You have collected ${money}!")
        game_over = True

    print(f"A. {vastauslista[0]}")
    print(f"B. {vastauslista[1]}")
    print(f"C. {vastauslista[2]}")
    print(f"D. {vastauslista[3]}")

    #Käyttäjän vastauskenttä
    vastaus = input("Your answer: ").upper()

    #Tarkastetaan vastasiko käyttäjä oikein
    if vastaus == "A":
        if vastauslista[0] == answer:
            print("Correct answer!")
            #Palkitaan pelaajaa oikeasta vastauksesta
            reward = 100 * current_round
            money = money + reward
            print(f"You have earned ${reward}! You now have ${money}!")
        else:
            print(f"Wrong answer, the correct answer was {answer}.")
            game_over = True

    elif vastaus == "B":
        if vastauslista[1] == answer:
            print("Correct answer!")
            reward = 100 * current_round
            money = money + reward
            print(f"You have earned ${reward}! You now have ${money}!")
        else:
            print(f"Wrong answer, the correct answer was {answer}.")
            game_over = True

    elif vastaus == "C":
        if vastauslista[2] == answer:
            print("Correct answer!")
            reward = 100 * current_round
            money = money + reward
            print(f"You have earned ${reward}! You now have ${money}!")
        else:
            print(f"Wrong answer, the correct answer was {answer}.")
            game_over = True

    elif vastaus == "D":
        if vastauslista[3] == answer:
            print("Correct answer!")
            reward = 100 * current_round
            money = money + reward
            print(f"You have earned ${reward}! You now have ${money}!")
        else:
            print(f"Wrong answer, the correct answer was {answer}.")
            game_over = True
    #Jos pelaaja syöttää virheellisen vastauksen
    else:
        print("Error")
        game_over = True
#Game over
print("Game over.")