# TicTacToe  (v1.0)
### by Shawn Lu

---

Hello everyone, I like games and today I made PvP TicTacToe in Python3! I hope you like this game.

To run the game, use the command:
```
python3 tictactoe.py
```

Because the game is so complicated it may take up to 30 seconds to load. 

After the game has loaded, you can find a friend and take turns typing out the moves (specified by a coordinate). 
Note: if you cannot find a friend you can always challenge yourself!

A coordinate is represented with the column letter + row number. As follows:

```
   A    B    C
1  A1 | B1 | C1
  --------------
2  A2 | B2 | C2
  --------------
3  A3 | B3 | C3
```

Here is a sample run of a game:
```
> python .\out.py

Welcome to TicTacToe!


### Turn 1, Player 1 ###
#                      #
#        A   B   C     #
#     1    |   |       #
#       -----------    #
#     2    |   |       #
#       -----------    #
#     3    |   |       #
#                      #
########################
Please select a square (e.g. A1) => B2

### Turn 1, Player 2 ###
#                      #
#        A   B   C     #
#     1    |   |       #
#       -----------    #
#     2    | X |       #
#       -----------    #
#     3    |   |       #
#                      #
########################
Please select a square (e.g. A1) => B1

### Turn 2, Player 1 ###
#                      #
#        A   B   C     #
#     1    | O |       #
#       -----------    #
#     2    | X |       #
#       -----------    #
#     3    |   |       #
#                      #
########################
Please select a square (e.g. A1) => A3

### Turn 2, Player 2 ###
#                      #
#        A   B   C     #
#     1    | O |       #
#       -----------    #
#     2    | X |       #
#       -----------    #
#     3  X |   |       #
#                      #
########################
Please select a square (e.g. A1) => A1

### Turn 3, Player 1 ###
#                      #
#        A   B   C     #
#     1  O | O |       #
#       -----------    #
#     2    | X |       #
#       -----------    #
#     3  X |   |       #
#                      #
########################
Please select a square (e.g. C1) => C1

########################
#                      #
#        A   B   C     #
#     1  O | O | X     #
#       -----------    #
#     2    | X |       #
#       -----------    #
#     3  X |   |       #
#                      #
########################
>>> Player 1 wins! <<<

Do you want to play again (y/n) => n
I hope you enjoyed my game, bye!

```

---
## Have a nice day!