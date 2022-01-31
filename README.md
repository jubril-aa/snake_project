# snake_project

This is our Snake project made with object-oriented programming and pygame. Scores are saved with a database using sqlite3. 
Through this project we wanted to deepen our knowledge about oop and learn how to use pygame and sqlite3.

### About the game

* The game.py file is where all components of the game are combined. 
    - It contains the main while loop that brings the game alive. 
    - In it, you can change e.g., screen size, speed of the game or the colour of the board.
 
* food.py creates the object that must be collected to gain more points, while serpant.py creates the snake that is controlled by the player, using the arrow keys on the computer. 
    - A player mustn’t go out of the screen or crash into to body of the snake, otherwise the game is over. 

* With after_game.py the player can enter his/her name. 
    - Their name as well as their score will be saved in the database, snakegame.db
    - Each player’s name is saved once and if the same player achieves a higher score, then his/her previous high score, the points will be overwritten. 

 
## The game itself I started by running `main.py`.

