"""Write and create database in order to save scores and username"""

import sqlite3

conn = sqlite3.connect("snake_database.db")

cursor = conn.cursor()


def insert_score(user, score):
    """Insert score and user into database"""
    # tup = (user, score)
    # create query to check if user in db
    exist = cursor.execute("SELECT username FROM board WHERE ")
    # else create new row
    cursor.execute("INSERT INTO board (username, point) VALUES(?, ?)", (user, score))
    conn.commit()
    conn.close()
    return



def get_top():
    """"""
    cursor.execute("SELECT * FROM board WHERE board.username = ")
    pass
