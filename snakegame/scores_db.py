"""
module author: Peter Pernhaupt, Jubril Ayomide Ajao
Write and create database in order to save scores and username"""

import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def open_db():
    """Open the database
    Returns a connection object from sqlite3"""
    con = sqlite3.connect("snakegame/snakegame.db")
    con.row_factory = dict_factory
    return con


def insert_score(user, score):
    """Insert score and user into database"""

    cur = open_db().cursor()
    # create query to check if user in db
    exist = cur.execute("SELECT * FROM board WHERE board.user=:name", {"name": user}).fetchone()
    if exist:
        # change the point
        if exist["points"] < score:
            cur.execute("UPDATE board SET points=:points WHERE user=:user", {"user": user, "points": score})
    # else create new row
    else:
        cur.execute("INSERT INTO board (user, points) VALUES(?, ?)", (user, score))
    # Save (commit) the changes
    open_db().commit()
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed, or they will be lost.
    open_db().close()
    return


def get_top(lim):
    """Get data out of the database but limited by LIMIT
    lim - must be an integer"""

    assert type(lim) is int
    cur = open_db().cursor()
    # name is a Row object
    top = cur.execute(f"SELECT user, points FROM board ORDER BY board.points DESC LIMIT {lim}").fetchall()

    open_db().close()
    return top
