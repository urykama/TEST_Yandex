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


def fSelect():
    try:
        conn = sqlite3.connect('test.db')

        cur = conn.cursor()
        print("База данных подключена к SQLite")

        ''' cur.execute("""SELECT
            cou.name AS Country, COUNT(com.id)
                FROM Companies com
                LEFT JOIN Cities cit                ON cit.id = com.city_id
                LEFT JOIN Countries cou                ON cit.country_id = cou.id
                WHERE  com.labors > 1000 AND city_id IN (SELECT cit2.id
                    FROM Cities cit2
                    LEFT JOIN Countries cou2                ON cit2.country_id = cou2.id
                    WHERE cou2.population > 1000000 AND cou2.gdp > 10000000000)
            GROUP BY cou.id
            HAVING SUM(com.revenue) > 1000000000
        """)'''

        cur.execute("""SELECT
            cou.name AS Country, COUNT(com.id)
                FROM Companies com
                LEFT JOIN Cities cit     ON cit.id = com.city_id
                LEFT JOIN Countries cou  ON cou.id = cit.country_id
                WHERE  com.labors >= 1000
            GROUP BY cou.id
         """)
        records = cur.fetchall()
        print("Всего строк:  ", len(records))
        print("Вывод каждой строки")
        for row in records:
            print(row)

        conn.commit()
        # print("Таблица SQLite заполнена")
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
    fSelect()
    # fOut()


# ('Россия', 3)
# ('Узбекистан', 2)
# ('Китай', 3)
