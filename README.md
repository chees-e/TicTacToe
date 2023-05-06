# TicTacToe  (v1.1)
### by Shawn Lu

---

Hello everyone, I like games and today I made Player vs CPU TicTacToe in Python3! I hope you like this game.

To run the game, use the command:
```
python3 tictactoe.py
```

You will be competing against the computer program, you will always make the first move. To make a move, you need to type a coordinate.

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
> python .\tictactoe.py

Welcome to TicTacToe!


## Turn 1, Your move: ##
#                      #
#        A   B   C     #
#     1    |   |       #
#       -----------    #
#     2    |   |       #
#       -----------    #
#     3    |   |       #
#                      #
########################
Please select a square (e.g. A1) => B1

> I played B2

## Turn 2, Your move: ##
#                      #
#        A   B   C     #
#     1    | X |       #
#       -----------    #
#     2    | O |       #
#       -----------    #
#     3    |   |       #
#                      #
########################
Please select a square (e.g. A1) => A2

> I played C3

## Turn 3, Your move: ##
#                      #
#        A   B   C     #
#     1    | X |       #
#       -----------    #
#     2  X | O |       #
#       -----------    #
#     3    |   | O     #
#                      #
########################
Please select a square (e.g. A1) => A1

> I played A3

## Turn 4, Your move: ##
#                      #
#        A   B   C     #
#     1  X | X |       #
#       -----------    #
#     2  X | O |       #
#       -----------    #
#     3  O |   | O     #
#                      #
########################
Please select a square (e.g. C1) => C1

########################
#                      #
#        A   B   C     #
#     1  X | X | X     #
#       -----------    #
#     2  X | O |       #
#       -----------    #
#     3  O |   | O     #
#                      #
########################
>>> You win, Congrats! <<<

Do you want to play again (y/n) => n
I hope you enjoyed my game, bye!

```

---
## Have a nice day!