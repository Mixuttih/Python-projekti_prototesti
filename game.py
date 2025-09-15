import random

import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    port=3307,
    database='flight_game',
    user='root',
    password='mikasana',
    autocommit=True
)
print("Welcome to 'Who Wants to be a Millionaire?' Airport Edition!")
username = input('Enter your username: ')
