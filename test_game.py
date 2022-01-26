"""
module authors: Peter Pernhaupt, Florian Weiß and Jubril Ayomide Ajao
This module test some logic behind the snake game
"""

import unittest
import sqlite3
from snakegame import food, scores_db

X, Y = 700, 540


class TestFood(unittest.TestCase):
    """Test food module in snakegame"""

    def setUp(self):
        self.food = food.Food(width=X, height=Y, board=(X, Y))

    def test_grow_new_food(self):
        """Test if the generated coordinates for food are in the valid given range"""
        possible_range_y = range(35, self.food.width - 20)
        possible_range_x = range(20, self.food.width - 20)

        self.assertIn(self.food.x, possible_range_x)
        self.assertIn(self.food.y, possible_range_y)


class TestScoreDatabase(unittest.TestCase):
    """Test the interaction the database"""

    # create a database no memory
    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def setUp(self):
        self.con = sqlite3.connect("snakegame/snakegame.db")
        self.con.row_factory = self.dict_factory
        self.cur = self.con.cursor()
        self.user_old = ("flo", 1100)
        self.user_new = ("black_mamba", 70)

    def test_insert_score_known(self):
        """Test creating updating an old object/row and create new user"""

        old_entry = self.cur.execute("SELECT * FROM board WHERE board.user=:user",
                                     {"user": self.user_old[0]}).fetchone()

        scores_db.insert_score(self.user_old[0], self.user_old[1])
        get_user = self.cur.execute("SELECT * FROM board WHERE board.user=:user",
                                    {"user": self.user_old[0]}).fetchone()

        self.assertNotEqual(None, get_user)
        self.assertEqual(self.user_old[1], get_user["points"])
        # set back to old entry
        self.cur.execute("UPDATE board SET points=:points WHERE user=:user",
                         {"user": self.user_old[0], "points": old_entry["points"]})
        # in order to check if the old entry is in the database again
        get_user_again = self.cur.execute("SELECT * FROM board WHERE board.user=:user",
                                          {"user": self.user_old[0]}).fetchone()
        self.assertEqual(old_entry, get_user_again)
        self.con.commit()

        """Create new user into the database"""
        get_user_2 = self.cur.execute("SELECT * FROM board WHERE board.user=:user",
                                      {"user": self.user_new[0]}).fetchone()
        self.assertEqual(None, get_user_2)
        # insert now
        self.cur.execute("INSERT INTO board (user, points) VALUES(?, ?)",
                         (self.user_new[0], self.user_new[1]))

        # check if entry is in the database
        get_new_user = self.cur.execute("SELECT * FROM board WHERE board.user=:user",
                                        {"user": self.user_new[0]}).fetchone()
        self.assertEqual(self.user_new[0], get_new_user["user"])
        self.assertEqual(self.user_new[1], get_new_user["points"])

        # delete afterwards
        self.cur.execute("DELETE FROM board WHERE board.user=:user", {"user": self.user_new[0]})
        # validate again
        to_delete = self.cur.execute("SELECT * FROM board WHERE board.user=:user",
                                     {"user": self.user_new[0]}).fetchone()
        self.assertEqual(None, to_delete)
        self.con.commit()

        self.con.close()

    def test_get_top(self):
        """Test get_top from scores_db"""
        # check if only takes integers as argument
        self.assertRaises(AssertionError, scores_db.get_top, "foo")
        n = 10
        # check if the numbers really sorted
        top_10 = [element["points"] for element in scores_db.get_top(n)]
        self.assertEqual(sorted(top_10, reverse=True), top_10)


if __name__ == '__main__':
    unittest.main()

# python test_game.py
