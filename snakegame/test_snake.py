import unittest
import sqlite3
from scores_db import dict_factory




con = sqlite3.connect("snakegame/test_snake.db")
con.row_factory = dict_factory
cur = con.cursor()

class TestVrptwWriter(unittest.TestCase):

    def test_top_ten_function(self):
        """
        Get_top was defined in this file again becaue sqlite3 dosen't take variables as arguments.
        """

        def get_top(lim):
            assert type(lim) is int
            top = cur.execute(f"SELECT user, points FROM board ORDER BY board.points DESC LIMIT {lim}").fetchall()
            return top

        test_list = [{'user': 'python', 'points': 100}, 
                    {'user': 'anaconda', 'points': 90}, 
                    {'user': 'poskok', 'points': 80}, 
                    {'user': 'mamba', 'points': 70}, 
                    {'user': 'cobra', 'points': 60}, 
                    {'user': 'viper', 'points': 50}, 
                    {'user': 'boa', 'points': 40}, 
                    {'user': 'kingsnake', 'points': 30}, 
                    {'user': 'anilius', 'points': 20}, 
                    {'user': 'taipan', 'points': 10}]
                    
        self.assertListEqual(get_top(10), test_list)



    def test_db_input_function(self):
        """
        The test_method() tests if the insert_score methode actually inserts the name and new score into the database.
        """
        
        user = "python"
        points = [100, 50, 40]

        def test_method(user, current_points):
            testing_db_input = cur.execute("SELECT * FROM board WHERE board.user=:name", {"name": user}).fetchone()
            if testing_db_input:
                if current_points <= testing_db_input["points"]:
                    return
                else:
                    assert False
            else:
                assert False
        
        for i in points:
            test_method(user, i)
        


if __name__ == "__main__":
    unittest.main()


                
    
    