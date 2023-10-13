import pandas as pd 

import sqlite3 

#CREATE DATABASE

db = sqlite3.connect('db.sqlite3')

##################
#CREATE TABLES
##################

cursor = db.cursor()

#TABLE AGRITURISMI
cursor.execute('''
    CREATE TABLE IF NOT EXISTS agriturismi(
        id INTEGER PRIMARY KEY,
        regione TEXT,
        anno INTEGER,
        arrivi INTEGER,
        presenze INTEGER
    )
''')

#TABLE CAMPEGGI
cursor.execute('''
    CREATE TABLE IF NOT EXISTS campeggi(
        id INTEGER PRIMARY KEY,
        regione TEXT,
        anno INTEGER,
        arrivi INTEGER,
        presenze INTEGER
    )
''')

#TABLE ESERCIZI ALBERGHIERI
cursor.execute('''
    CREATE TABLE IF NOT EXISTS esercizi_alberghieri(
        id INTEGER PRIMARY KEY,
        regione TEXT,
        anno INTEGER,
        arrivi INTEGER,
        presenze INTEGER
    )
''')

db.commit()
