# ищем развороты вер. 2 с переменным коэффициентом
import websocket
import json
import sqlite3
import time
import urllib
import hmac, hashlib
import requests
from urllib.parse import urlparse, urlencode
from urllib.request import Request, urlopen


def fCreatTable():
    try:
        conn = sqlite3.connect('test.db')

        cur = conn.cursor()
        print("База данных подключена к SQLite")
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS Cities(
                    id int(11) NOT NULL DEFAULT '0',
                    name TEXT(50) DEFAULT NULL,
                    population int(11) DEFAULT NULL,
                    founded int(11) DEFAULT NULL,
                    country_id int(11) DEFAULT NULL,
                    PRIMARY KEY (id)); """)

        cur.execute("""
                    CREATE TABLE IF NOT EXISTS Companies(
                    id int(11) NOT NULL DEFAULT '0',
                    name TEXT(50) DEFAULT NULL,
                    city_id int(11) DEFAULT NULL,
                    revenue int(11) DEFAULT NULL,
                    labors int(11) DEFAULT NULL,
                    PRIMARY KEY (id)); """)

        cur.execute("""
                    CREATE TABLE IF NOT EXISTS Countries(
                    id int(11) NOT NULL DEFAULT '0',
                    name TEXT(50) DEFAULT NULL,
                    population int(11) DEFAULT NULL,
                    gdp int(11) DEFAULT NULL,
                    PRIMARY KEY (id)); """)

        cur.close()
        conn.commit()
        print("Таблица SQLite создана")
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (conn):
            conn.close()
            print("Соединение с SQLite закрыто")


def fInsert():
    try:
        conn = sqlite3.connect('test.db')

        cur = conn.cursor()
        print("База данных подключена к SQLite")
        data = [(1, 'Ульяновск', 750000, 1648, 1),
                (2, 'Москва', 3000000, 1420, 1),
                (3, 'Ташкент', 2500000, 956, 2),
                (4, 'Урумчи', 900000, 205, 3),
                (5, 'Шанхай', 3000000, 20, 3)]
        cur.executemany("""INSERT INTO Cities
                        (id, name, population, founded, country_id)
                        VALUES (?, ?, ?, ?, ?);""", data)

        dataCountries = [(1, 'Россия', 3000000, 500000000000),
                         (2, 'Узбекистан', 1000001, 200000000000),
                         (3, 'Китай', 1000000000, 1000000000000)]
        cur.executemany("""INSERT INTO Countries
                        (id, name, population, gdp)
                        VALUES (?, ?, ?, ?);""", dataCountries)

        dataCompanies = [(1, 'Супер-софт', 1, 900000000, 700),
                         (2, 'Мегасофт', 1, 500000000, 3000),
                         (3, 'Ковер-самолет', 3, 5000000, 3000),
                         (4, 'Трах-Тибидох Development', 3, 1000000000, 500),
                         (5, 'Ур Ум Чи\'ка-1', 4, 300000, 1001),
                         (6, 'Ур Ум Чи\'ка-3', 4, 520000, 999),
                         (7, 'Пу До Нг', 5, 600000000, 160),
                         (8, 'ZBAA Dev', 5, 520000000, 2500),
                         (9, 'IBS', 2, 500, 1200),
                         (10, 'Ур Ум Чи\'ка-2', 4, 200000, 1000)]
        cur.executemany("""INSERT INTO Companies
                        (id, name, city_id, revenue, labors)
                        VALUES (?, ?, ?, ?, ?);""", dataCompanies)

        conn.commit()
        print("Таблица SQLite заполнена")
        cur.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (conn):
            conn.close()
            print("Соединение с SQLite закрыто")


def fOut():
    try:
        conn = sqlite3.connect('test.db')

        cur = conn.cursor()
        print("База данных подключена к SQLite")
        cur.execute("SELECT * FROM Cities;")
        all_results = cur.fetchall()
        print(all_results)

        cur.execute("SELECT * FROM Companies;")
        all_results = cur.fetchall()
        print(all_results)

        cur.execute("SELECT * FROM Countries;")
        all_results = cur.fetchall()
        print(all_results)

        conn.commit()
        print("Таблица SQLite создана")
        cur.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (conn):
            conn.close()
            print("Соединение с SQLite закрыто")


if __name__ == "__main__":
    fCreatTable()
    fInsert()
    fOut()
