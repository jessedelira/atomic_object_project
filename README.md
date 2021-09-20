# Jesse De Lira Othello Submission (Atomic Object)

## Playing Game
Run command to start server locally:  

    $ java -jar othello.jar --p1-type remote --p2-type random --min-turn-time 100

Run command to enter "player" into game:

    $ python client.py

Vist **http://localhost:8080/** to see Web UI of Othello Game.

**Important Note**    
I overlooked the fact that maybe the remote "player" would also be connected in as the second player. As of now the "player" is only able to player as Player 1, since the algorithm is only registering opponent chips as the value 2 on the board.














## Development Notes
Used Python 3.8.3 for development and testing.
