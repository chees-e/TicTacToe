# TicTacToe Game in Python3
# Written by chees-e (Shawn Lu), May 5th, 2023


# Main game
def game():
    print("\nWelcome to TicTacToe!\n")
    while True:
        print("\n## Turn 1, Your move: ##\n"
            "#                      #\n"
            "#        A   B   C     #\n"
            "#     1    |   |       #\n"
            "#       -----------    #\n"
            "#     2    |   |       #\n"
            "#       -----------    #\n"
            "#     3    |   |       #\n"
            "#                      #\n"
            "########################"
        )
        move = input("Please select a square (e.g. A1) => ").upper()
        if move == "A1":
            print("\n> I played B2")
            while True:
                print("\n## Turn 2, Your move: ##\n"
                    "#                      #\n"
                    "#        A   B   C     #\n"
                    "#     1  X |   |       #\n"
                    "#       -----------    #\n"
                    "#     2    | O |       #\n"
                    "#       -----------    #\n"
                    "#     3    |   |       #\n"
                    "#                      #\n"
                    "########################"
                )
                move = input("Please select a square (e.g. B1) => ").upper()
                if move == "B1":
                    print("\n> I played C1")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1  X | X | O     #\n"
                            "#       -----------    #\n"
                            "#     2    | O |       #\n"
                            "#       -----------    #\n"
                            "#     3    |   |       #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A2) => ").upper()
                        if move == "A2":
                            print("\n> I played A3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X | X | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O |   |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played A3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X | X | O     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  O |   |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A3":
                            print("\n> I played A2")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X | X | O     #\n"
                                    "#       -----------    #\n"
                                    "#     2  O | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3  X |   |       #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. C2) => ").upper()
                                if move == "C2":
                                    print("\n> I played C3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X |   | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B3":
                                    print("\n> I played C2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | X |       #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C3":
                                    print("\n> I played C2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X |   | X     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "B3":
                            print("\n> I played A3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X | X | O     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O | X |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C3":
                            print("\n> I played A3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X | X | O     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "C1":
                    print("\n> I played B1")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1  X | O | X     #\n"
                            "#       -----------    #\n"
                            "#     2    | O |       #\n"
                            "#       -----------    #\n"
                            "#     3    |   |       #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A2) => ").upper()
                        if move == "A2":
                            print("\n> I played B3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3    | O |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played B3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    | O |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A3":
                            print("\n> I played B3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X | O |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played C3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3    | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A2) => ").upper()
                                if move == "A2":
                                    print("\n> I played A3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C2) => ").upper()
                                        if move == "C2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "C2":
                                    print("\n> I played A3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2    | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A2) => ").upper()
                                        if move == "A2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "A3":
                                    print("\n> I played A2")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C2) => ").upper()
                                        if move == "C2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "C3":
                            print("\n> I played B3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3    | O | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "A2":
                    print("\n> I played A3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1  X |   |       #\n"
                            "#       -----------    #\n"
                            "#     2  X | O |       #\n"
                            "#       -----------    #\n"
                            "#     3  O |   |       #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. B1) => ").upper()
                        if move == "B1":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X | X | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O |   |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C1":
                            print("\n> I played B1")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2  X | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3  O |   |       #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. C2) => ").upper()
                                if move == "C2":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | O |       #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "B3":
                                    print("\n> I played C3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C2) => ").upper()
                                        if move == "C2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "C3":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O |       #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | O | X     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "C2":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  O |   |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O | X |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C3":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "C2":
                    print("\n> I played C3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1  X |   |       #\n"
                            "#       -----------    #\n"
                            "#     2    | O | X     #\n"
                            "#       -----------    #\n"
                            "#     3    |   | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. B1) => ").upper()
                        if move == "B1":
                            print("\n> I played C1")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X | X | O     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3    |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A2) => ").upper()
                                if move == "A2":
                                    print("\n> I played A3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O |   | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "A3":
                                    print("\n> I played A2")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X |   | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B3":
                                    print("\n> I played A3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "C1":
                            print("\n> I played B1")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3    |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A2) => ").upper()
                                if move == "A2":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3    | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "A3":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "B3":
                                    print("\n> I played A3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2    | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A2) => ").upper()
                                        if move == "A2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "A2":
                            print("\n> I played A3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  X | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3  O |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X |       #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C1":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "B3":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "A3":
                            print("\n> I played A2")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  O | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3  X |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played C1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X |   | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "C1":
                                    print("\n> I played B1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X |   | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B3":
                                    print("\n> I played C1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X |   | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B1) => ").upper()
                                        if move == "B1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "B3":
                            print("\n> I played A3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3  O | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C1":
                                    print("\n> I played B1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2    | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A2) => ").upper()
                                        if move == "A2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "A2":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        else:
                            print("Invalid move, try again")
                elif move == "A3":
                    print("\n> I played A2")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1  X |   |       #\n"
                            "#       -----------    #\n"
                            "#     2  O | O |       #\n"
                            "#       -----------    #\n"
                            "#     3  X |   |       #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. B1) => ").upper()
                        if move == "B1":
                            print("\n> I played C2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X | X |       #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C1":
                            print("\n> I played C2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played C3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  O | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3  X |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played C1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X |   | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "C1":
                                    print("\n> I played B1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X |   | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B3":
                                    print("\n> I played C1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X |   | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B1) => ").upper()
                                        if move == "B1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "B3":
                            print("\n> I played C2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   |       #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3  X | X |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C3":
                            print("\n> I played C2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   |       #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "B3":
                    print("\n> I played C3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1  X |   |       #\n"
                            "#       -----------    #\n"
                            "#     2    | O |       #\n"
                            "#       -----------    #\n"
                            "#     3    | X | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. B1) => ").upper()
                        if move == "B1":
                            print("\n> I played C1")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X | X | O     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3    | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A2) => ").upper()
                                if move == "A2":
                                    print("\n> I played C2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3    | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C2":
                                    print("\n> I played A3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "A3":
                                    print("\n> I played C2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "C1":
                            print("\n> I played B1")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3    | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A2) => ").upper()
                                if move == "A2":
                                    print("\n> I played A3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C2) => ").upper()
                                        if move == "C2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "C2":
                                    print("\n> I played A3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2    | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A2) => ").upper()
                                        if move == "A2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "A3":
                                    print("\n> I played A2")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C2) => ").upper()
                                        if move == "C2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "A2":
                            print("\n> I played A3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  X | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3  O | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O |       #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C1":
                                    print("\n> I played B1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C2) => ").upper()
                                        if move == "C2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "C2":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "C2":
                            print("\n> I played A3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3  O | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C1":
                                    print("\n> I played B1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2    | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A2) => ").upper()
                                        if move == "A2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "A2":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "A3":
                            print("\n> I played A2")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  O | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3  X | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played C2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X |       #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C1":
                                    print("\n> I played C2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C2":
                                    print("\n> I played C1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X |   | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B1) => ").upper()
                                        if move == "B1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        else:
                            print("Invalid move, try again")
                elif move == "C3":
                    print("\n> I played C2")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1  X |   |       #\n"
                            "#       -----------    #\n"
                            "#     2    | O | O     #\n"
                            "#       -----------    #\n"
                            "#     3    |   | X     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. B1) => ").upper()
                        if move == "B1":
                            print("\n> I played A2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X | X |       #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3    |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C1":
                            print("\n> I played A2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3    |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played A3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  X | O | O     #\n"
                                    "#       -----------    #\n"
                                    "#     3  O |   | X     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O |   | X     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C1":
                                    print("\n> I played B1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O |   | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B3":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | X     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "A3":
                            print("\n> I played A2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   |       #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played A2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   |       #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3    | X | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                else:
                    print("Invalid move, try again")
        elif move == "B1":
            print("\n> I played B2")
            while True:
                print("\n## Turn 2, Your move: ##\n"
                    "#                      #\n"
                    "#        A   B   C     #\n"
                    "#     1    | X |       #\n"
                    "#       -----------    #\n"
                    "#     2    | O |       #\n"
                    "#       -----------    #\n"
                    "#     3    |   |       #\n"
                    "#                      #\n"
                    "########################"
                )
                move = input("Please select a square (e.g. A1) => ").upper()
                if move == "A1":
                    print("\n> I played C1")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1  X | X | O     #\n"
                            "#       -----------    #\n"
                            "#     2    | O |       #\n"
                            "#       -----------    #\n"
                            "#     3    |   |       #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A2) => ").upper()
                        if move == "A2":
                            print("\n> I played A3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X | X | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O |   |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played A3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X | X | O     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  O |   |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A3":
                            print("\n> I played A2")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X | X | O     #\n"
                                    "#       -----------    #\n"
                                    "#     2  O | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3  X |   |       #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. C2) => ").upper()
                                if move == "C2":
                                    print("\n> I played C3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X |   | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B3":
                                    print("\n> I played C2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | X |       #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C3":
                                    print("\n> I played C2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X |   | X     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "B3":
                            print("\n> I played A3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X | X | O     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O | X |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C3":
                            print("\n> I played A3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X | X | O     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "C1":
                    print("\n> I played A1")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1  O | X | X     #\n"
                            "#       -----------    #\n"
                            "#     2    | O |       #\n"
                            "#       -----------    #\n"
                            "#     3    |   |       #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A2) => ").upper()
                        if move == "A2":
                            print("\n> I played C3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X | X     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3    |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played C3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A3":
                            print("\n> I played C3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played C3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C3":
                            print("\n> I played C2")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  O | X | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O | O     #\n"
                                    "#       -----------    #\n"
                                    "#     3    |   | X     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A2) => ").upper()
                                if move == "A2":
                                    print("\n> I played A3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  O | X | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O |   | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "A3":
                                    print("\n> I played A2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  O | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X |   | X     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "B3":
                                    print("\n> I played A2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  O | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3    | X | X     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        else:
                            print("Invalid move, try again")
                elif move == "A2":
                    print("\n> I played C3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    | X |       #\n"
                            "#       -----------    #\n"
                            "#     2  X | O |       #\n"
                            "#       -----------    #\n"
                            "#     3    |   | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played A3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X | X |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  X | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3  O |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. C1) => ").upper()
                                if move == "C1":
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O |       #\n"
                                        "#       -----------    #\n"
                                        "#     3  O |   | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> You win, Congrats! <<<\n")
                                    return
                                elif move == "C2":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X |       #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "B3":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O |       #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "C1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X | X     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3    |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "C2":
                    print("\n> I played C3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    | X |       #\n"
                            "#       -----------    #\n"
                            "#     2    | O | X     #\n"
                            "#       -----------    #\n"
                            "#     3    |   | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played C1")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X | X | O     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3    |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A2) => ").upper()
                                if move == "A2":
                                    print("\n> I played A3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O |   | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "A3":
                                    print("\n> I played A2")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X |   | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B3":
                                    print("\n> I played A3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "C1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "A3":
                    print("\n> I played C3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    | X |       #\n"
                            "#       -----------    #\n"
                            "#     2    | O |       #\n"
                            "#       -----------    #\n"
                            "#     3  X |   | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played A2")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X | X |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  O | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3  X |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. C1) => ").upper()
                                if move == "C1":
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | O |       #\n"
                                        "#       -----------    #\n"
                                        "#     3  X |   | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> You win, Congrats! <<<\n")
                                    return
                                elif move == "C2":
                                    print("\n> I played C1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X |   | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B3":
                                    print("\n> I played C2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X |       #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "C1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "B3":
                    print("\n> I played C3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    | X |       #\n"
                            "#       -----------    #\n"
                            "#     2    | O |       #\n"
                            "#       -----------    #\n"
                            "#     3    | X | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played C1")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X | X | O     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3    | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A2) => ").upper()
                                if move == "A2":
                                    print("\n> I played C2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3    | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C2":
                                    print("\n> I played A3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "A3":
                                    print("\n> I played C2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "C1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "C3":
                    print("\n> I played A3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    | X |       #\n"
                            "#       -----------    #\n"
                            "#     2    | O |       #\n"
                            "#       -----------    #\n"
                            "#     3  O |   | X     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X | X | O     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C1":
                            print("\n> I played C2")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1    | X | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O | O     #\n"
                                    "#       -----------    #\n"
                                    "#     3  O |   | X     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A1) => ").upper()
                                if move == "A1":
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O |   | X     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> You win, Congrats! <<<\n")
                                    return
                                elif move == "A2":
                                    print("\n> I played A1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  O | X | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O |   | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B3":
                                    print("\n> I played A2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1    | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | X     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "A2":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    | X | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    | X | O     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  O |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    | X | O     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O | X | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                else:
                    print("Invalid move, try again")
        elif move == "C1":
            print("\n> I played B2")
            while True:
                print("\n## Turn 2, Your move: ##\n"
                    "#                      #\n"
                    "#        A   B   C     #\n"
                    "#     1    |   | X     #\n"
                    "#       -----------    #\n"
                    "#     2    | O |       #\n"
                    "#       -----------    #\n"
                    "#     3    |   |       #\n"
                    "#                      #\n"
                    "########################"
                )
                move = input("Please select a square (e.g. A1) => ").upper()
                if move == "A1":
                    print("\n> I played B1")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1  X | O | X     #\n"
                            "#       -----------    #\n"
                            "#     2    | O |       #\n"
                            "#       -----------    #\n"
                            "#     3    |   |       #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A2) => ").upper()
                        if move == "A2":
                            print("\n> I played B3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3    | O |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played B3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    | O |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A3":
                            print("\n> I played B3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X | O |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played C3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3    | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A2) => ").upper()
                                if move == "A2":
                                    print("\n> I played A3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C2) => ").upper()
                                        if move == "C2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "C2":
                                    print("\n> I played A3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2    | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A2) => ").upper()
                                        if move == "A2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "A3":
                                    print("\n> I played A2")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C2) => ").upper()
                                        if move == "C2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "C3":
                            print("\n> I played B3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3    | O | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "B1":
                    print("\n> I played A1")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1  O | X | X     #\n"
                            "#       -----------    #\n"
                            "#     2    | O |       #\n"
                            "#       -----------    #\n"
                            "#     3    |   |       #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A2) => ").upper()
                        if move == "A2":
                            print("\n> I played C3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X | X     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3    |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played C3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A3":
                            print("\n> I played C3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played C3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C3":
                            print("\n> I played C2")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  O | X | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O | O     #\n"
                                    "#       -----------    #\n"
                                    "#     3    |   | X     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A2) => ").upper()
                                if move == "A2":
                                    print("\n> I played A3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  O | X | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O |   | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "A3":
                                    print("\n> I played A2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  O | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X |   | X     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "B3":
                                    print("\n> I played A2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  O | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3    | X | X     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        else:
                            print("Invalid move, try again")
                elif move == "A2":
                    print("\n> I played C3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   | X     #\n"
                            "#       -----------    #\n"
                            "#     2  X | O |       #\n"
                            "#       -----------    #\n"
                            "#     3    |   | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played A3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2  X | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3  O |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O |       #\n"
                                        "#       -----------    #\n"
                                        "#     3  O |   | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> You win, Congrats! <<<\n")
                                    return
                                elif move == "C2":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "B3":
                                    print("\n> I played B1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C2) => ").upper()
                                        if move == "C2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "B1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X | X     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3    |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "C2":
                    print("\n> I played C3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   | X     #\n"
                            "#       -----------    #\n"
                            "#     2    | O | X     #\n"
                            "#       -----------    #\n"
                            "#     3    |   | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played B1")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3    |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A2) => ").upper()
                                if move == "A2":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3    | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "A3":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "B3":
                                    print("\n> I played A3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2    | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A2) => ").upper()
                                        if move == "A2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "B1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "A3":
                    print("\n> I played C2")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   | X     #\n"
                            "#       -----------    #\n"
                            "#     2    | O | O     #\n"
                            "#       -----------    #\n"
                            "#     3  X |   |       #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played A2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B1":
                            print("\n> I played A2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    | X | X     #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played A1")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  O |   | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2  X | O | O     #\n"
                                    "#       -----------    #\n"
                                    "#     3  X |   |       #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played C3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  O | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X |   | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "B3":
                                    print("\n> I played C3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  O |   | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C3":
                                    print("\n> I played B3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  O |   | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | O | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B1) => ").upper()
                                        if move == "B1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | O | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "B3":
                            print("\n> I played A2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3  X | X |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C3":
                            print("\n> I played A2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "B3":
                    print("\n> I played C3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   | X     #\n"
                            "#       -----------    #\n"
                            "#     2    | O |       #\n"
                            "#       -----------    #\n"
                            "#     3    | X | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played B1")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3    | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A2) => ").upper()
                                if move == "A2":
                                    print("\n> I played A3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C2) => ").upper()
                                        if move == "C2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "C2":
                                    print("\n> I played A3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2    | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A2) => ").upper()
                                        if move == "A2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "A3":
                                    print("\n> I played A2")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C2) => ").upper()
                                        if move == "C2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "B1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "C3":
                    print("\n> I played C2")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   | X     #\n"
                            "#       -----------    #\n"
                            "#     2    | O | O     #\n"
                            "#       -----------    #\n"
                            "#     3    |   | X     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played A2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3    |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B1":
                            print("\n> I played A2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    | X | X     #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3    |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played A3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1    |   | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2  X | O | O     #\n"
                                    "#       -----------    #\n"
                                    "#     3  O |   | X     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A1) => ").upper()
                                if move == "A1":
                                    print("\n> I played B1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O |   | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B1":
                                    print("\n> I played A1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  O | X | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O |   | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B3":
                                    print("\n> I played A1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  O |   | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B1) => ").upper()
                                        if move == "B1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "A3":
                            print("\n> I played A2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played A2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3    | X | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                else:
                    print("Invalid move, try again")
        elif move == "A2":
            print("\n> I played B2")
            while True:
                print("\n## Turn 2, Your move: ##\n"
                    "#                      #\n"
                    "#        A   B   C     #\n"
                    "#     1    |   |       #\n"
                    "#       -----------    #\n"
                    "#     2  X | O |       #\n"
                    "#       -----------    #\n"
                    "#     3    |   |       #\n"
                    "#                      #\n"
                    "########################"
                )
                move = input("Please select a square (e.g. A1) => ").upper()
                if move == "A1":
                    print("\n> I played A3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1  X |   |       #\n"
                            "#       -----------    #\n"
                            "#     2  X | O |       #\n"
                            "#       -----------    #\n"
                            "#     3  O |   |       #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. B1) => ").upper()
                        if move == "B1":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X | X | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O |   |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C1":
                            print("\n> I played B1")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2  X | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3  O |   |       #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. C2) => ").upper()
                                if move == "C2":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | O |       #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "B3":
                                    print("\n> I played C3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C2) => ").upper()
                                        if move == "C2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "C3":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O |       #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | O | X     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "C2":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  O |   |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O | X |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C3":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "B1":
                    print("\n> I played C3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    | X |       #\n"
                            "#       -----------    #\n"
                            "#     2  X | O |       #\n"
                            "#       -----------    #\n"
                            "#     3    |   | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played A3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X | X |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  X | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3  O |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. C1) => ").upper()
                                if move == "C1":
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O |       #\n"
                                        "#       -----------    #\n"
                                        "#     3  O |   | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> You win, Congrats! <<<\n")
                                    return
                                elif move == "C2":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X |       #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "B3":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O |       #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "C1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X | X     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3    |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "C1":
                    print("\n> I played C3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   | X     #\n"
                            "#       -----------    #\n"
                            "#     2  X | O |       #\n"
                            "#       -----------    #\n"
                            "#     3    |   | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played A3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2  X | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3  O |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O |       #\n"
                                        "#       -----------    #\n"
                                        "#     3  O |   | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> You win, Congrats! <<<\n")
                                    return
                                elif move == "C2":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "B3":
                                    print("\n> I played B1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C2) => ").upper()
                                        if move == "C2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "B1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X | X     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3    |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "C2":
                    print("\n> I played C3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   |       #\n"
                            "#       -----------    #\n"
                            "#     2  X | O | X     #\n"
                            "#       -----------    #\n"
                            "#     3    |   | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played A3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  X | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3  O |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X |       #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C1":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "B3":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "B1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "A3":
                    print("\n> I played A1")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1  O |   |       #\n"
                            "#       -----------    #\n"
                            "#     2  X | O |       #\n"
                            "#       -----------    #\n"
                            "#     3  X |   |       #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. B1) => ").upper()
                        if move == "B1":
                            print("\n> I played C3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C1":
                            print("\n> I played C3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played C3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played C3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C3":
                            print("\n> I played B3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  O |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  X | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3  X | O | X     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played C1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  O | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | O | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C2) => ").upper()
                                        if move == "C2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  O | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | O | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "C1":
                                    print("\n> I played B1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  O | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O |       #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | O | X     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C2":
                                    print("\n> I played B1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  O | O |       #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | O | X     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        else:
                            print("Invalid move, try again")
                elif move == "B3":
                    print("\n> I played C3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   |       #\n"
                            "#       -----------    #\n"
                            "#     2  X | O |       #\n"
                            "#       -----------    #\n"
                            "#     3    | X | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played A3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  X | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3  O | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O |       #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C1":
                                    print("\n> I played B1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C2) => ").upper()
                                        if move == "C2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "C2":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "B1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "C3":
                    print("\n> I played A3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   |       #\n"
                            "#       -----------    #\n"
                            "#     2  X | O |       #\n"
                            "#       -----------    #\n"
                            "#     3  O |   | X     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B1":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    | X | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C1":
                            print("\n> I played C2")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1    |   | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2  X | O | O     #\n"
                                    "#       -----------    #\n"
                                    "#     3  O |   | X     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A1) => ").upper()
                                if move == "A1":
                                    print("\n> I played B1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O |   | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B1":
                                    print("\n> I played A1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  O | X | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O |   | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B3":
                                    print("\n> I played A1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  O |   | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B1) => ").upper()
                                        if move == "B1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "C2":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  O |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O | X | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                else:
                    print("Invalid move, try again")
        elif move == "B2":
            print("\n> I played C3")
            while True:
                print("\n## Turn 2, Your move: ##\n"
                    "#                      #\n"
                    "#        A   B   C     #\n"
                    "#     1    |   |       #\n"
                    "#       -----------    #\n"
                    "#     2    | X |       #\n"
                    "#       -----------    #\n"
                    "#     3    |   | O     #\n"
                    "#                      #\n"
                    "########################"
                )
                move = input("Please select a square (e.g. A1) => ").upper()
                if move == "A1":
                    print("\n> I played A3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1  X |   |       #\n"
                            "#       -----------    #\n"
                            "#     2    | X |       #\n"
                            "#       -----------    #\n"
                            "#     3  O |   | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. B1) => ").upper()
                        if move == "B1":
                            print("\n> I played B3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X | X |       #\n"
                                "#       -----------    #\n"
                                "#     2    | X |       #\n"
                                "#       -----------    #\n"
                                "#     3  O | O | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C1":
                            print("\n> I played B3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | X |       #\n"
                                "#       -----------    #\n"
                                "#     3  O | O | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played B3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | X |       #\n"
                                "#       -----------    #\n"
                                "#     3  O | O | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played B3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   |       #\n"
                                "#       -----------    #\n"
                                "#     2    | X | X     #\n"
                                "#       -----------    #\n"
                                "#     3  O | O | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played B1")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     2    | X |       #\n"
                                    "#       -----------    #\n"
                                    "#     3  O | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. C1) => ").upper()
                                if move == "C1":
                                    print("\n> I played C2")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2    | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A2) => ").upper()
                                        if move == "A2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "A2":
                                    print("\n> I played C2")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C1) => ").upper()
                                        if move == "C1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "C2":
                                    print("\n> I played A2")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | X | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C1) => ").upper()
                                        if move == "C1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        else:
                            print("Invalid move, try again")
                elif move == "B1":
                    print("\n> I played B3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    | X |       #\n"
                            "#       -----------    #\n"
                            "#     2    | X |       #\n"
                            "#       -----------    #\n"
                            "#     3    | O | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played A3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X | X |       #\n"
                                "#       -----------    #\n"
                                "#     2    | X |       #\n"
                                "#       -----------    #\n"
                                "#     3  O | O | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C1":
                            print("\n> I played A3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    | X | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | X |       #\n"
                                "#       -----------    #\n"
                                "#     3  O | O | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played A3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    | X |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | X |       #\n"
                                "#       -----------    #\n"
                                "#     3  O | O | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played A3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    | X |       #\n"
                                "#       -----------    #\n"
                                "#     2    | X | X     #\n"
                                "#       -----------    #\n"
                                "#     3  O | O | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A3":
                            print("\n> I played C1")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1    | X | O     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | X |       #\n"
                                    "#       -----------    #\n"
                                    "#     3  X | O | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A1) => ").upper()
                                if move == "A1":
                                    print("\n> I played C2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "A2":
                                    print("\n> I played C2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1    | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C2":
                                    print("\n> I played A2")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1    | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | X | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | O | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A1) => ").upper()
                                        if move == "A1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | O | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        else:
                            print("Invalid move, try again")
                elif move == "C1":
                    print("\n> I played A3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   | X     #\n"
                            "#       -----------    #\n"
                            "#     2    | X |       #\n"
                            "#       -----------    #\n"
                            "#     3  O |   | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played B3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | X |       #\n"
                                "#       -----------    #\n"
                                "#     3  O | O | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B1":
                            print("\n> I played B3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    | X | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | X |       #\n"
                                "#       -----------    #\n"
                                "#     3  O | O | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played B3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  X | X |       #\n"
                                "#       -----------    #\n"
                                "#     3  O | O | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played B3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | X | X     #\n"
                                "#       -----------    #\n"
                                "#     3  O | O | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played B1")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1    | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | X |       #\n"
                                    "#       -----------    #\n"
                                    "#     3  O | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A1) => ").upper()
                                if move == "A1":
                                    print("\n> I played C2")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2    | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A2) => ").upper()
                                        if move == "A2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "A2":
                                    print("\n> I played C2")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1    | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A1) => ").upper()
                                        if move == "A1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "C2":
                                    print("\n> I played A2")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1    | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | X | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A1) => ").upper()
                                        if move == "A1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        else:
                            print("Invalid move, try again")
                elif move == "A2":
                    print("\n> I played C2")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   |       #\n"
                            "#       -----------    #\n"
                            "#     2  X | X | O     #\n"
                            "#       -----------    #\n"
                            "#     3    |   | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | X | O     #\n"
                                "#       -----------    #\n"
                                "#     3    |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B1":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    | X | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | X | O     #\n"
                                "#       -----------    #\n"
                                "#     3    |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C1":
                            print("\n> I played A3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1    |   | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2  X | X | O     #\n"
                                    "#       -----------    #\n"
                                    "#     3  O |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A1) => ").upper()
                                if move == "A1":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "B1":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1    | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "B3":
                                    print("\n> I played B1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1    | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A1) => ").upper()
                                        if move == "A1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "A3":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | X | O     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | X | O     #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "C2":
                    print("\n> I played A2")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   |       #\n"
                            "#       -----------    #\n"
                            "#     2  O | X | X     #\n"
                            "#       -----------    #\n"
                            "#     3    |   | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played A3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  O | X | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3  O |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X |       #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C1":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "B3":
                                    print("\n> I played B1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | X | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C1) => ").upper()
                                        if move == "C1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "B1":
                            print("\n> I played B3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1    | X |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  O | X | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3    | O | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A1) => ").upper()
                                if move == "A1":
                                    print("\n> I played A3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X |       #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C1":
                                    print("\n> I played A3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1    | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "A3":
                                    print("\n> I played C1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1    | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | X | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | O | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A1) => ").upper()
                                        if move == "A1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | O | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "C1":
                            print("\n> I played A3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1    |   | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2  O | X | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3  O |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A1) => ").upper()
                                if move == "A1":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "B1":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1    | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "B3":
                                    print("\n> I played A1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  O |   | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "A3":
                            print("\n> I played C1")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1    |   | O     #\n"
                                    "#       -----------    #\n"
                                    "#     2  O | X | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3  X |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A1) => ").upper()
                                if move == "A1":
                                    print("\n> I played B3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X |   | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | X | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | O | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B1) => ").upper()
                                        if move == "B1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | O | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B1":
                                    print("\n> I played B3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1    | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | X | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | O | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A1) => ").upper()
                                        if move == "A1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | O | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B3":
                                    print("\n> I played B1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1    | O | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | X | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A1) => ").upper()
                                        if move == "A1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "B3":
                            print("\n> I played B1")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1    | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  O | X | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3    | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A1) => ").upper()
                                if move == "A1":
                                    print("\n> I played A3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | X | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C1) => ").upper()
                                        if move == "C1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "C1":
                                    print("\n> I played A3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1    | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | X | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A1) => ").upper()
                                        if move == "A1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "A3":
                                    print("\n> I played C1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1    | O | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | X | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A1) => ").upper()
                                        if move == "A1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        else:
                            print("Invalid move, try again")
                elif move == "A3":
                    print("\n> I played C1")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   | O     #\n"
                            "#       -----------    #\n"
                            "#     2    | X |       #\n"
                            "#       -----------    #\n"
                            "#     3  X |   | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played C2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2    | X | O     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B1":
                            print("\n> I played C2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    | X | O     #\n"
                                "#       -----------    #\n"
                                "#     2    | X | O     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played C2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | X | O     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played A2")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1    |   | O     #\n"
                                    "#       -----------    #\n"
                                    "#     2  O | X | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3  X |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A1) => ").upper()
                                if move == "A1":
                                    print("\n> I played B3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X |   | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | X | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | O | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B1) => ").upper()
                                        if move == "B1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | O | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B1":
                                    print("\n> I played B3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1    | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | X | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | O | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A1) => ").upper()
                                        if move == "A1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | O | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B3":
                                    print("\n> I played B1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1    | O | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | X | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A1) => ").upper()
                                        if move == "A1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "B3":
                            print("\n> I played C2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2    | X | O     #\n"
                                "#       -----------    #\n"
                                "#     3  X | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "B3":
                    print("\n> I played B1")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    | O |       #\n"
                            "#       -----------    #\n"
                            "#     2    | X |       #\n"
                            "#       -----------    #\n"
                            "#     3    | X | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played A3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     2    | X |       #\n"
                                    "#       -----------    #\n"
                                    "#     3  O | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. C1) => ").upper()
                                if move == "C1":
                                    print("\n> I played C2")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2    | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A2) => ").upper()
                                        if move == "A2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "A2":
                                    print("\n> I played C2")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C1) => ").upper()
                                        if move == "C1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "C2":
                                    print("\n> I played A2")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | X | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C1) => ").upper()
                                        if move == "C1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "C1":
                            print("\n> I played A3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1    | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | X |       #\n"
                                    "#       -----------    #\n"
                                    "#     3  O | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A1) => ").upper()
                                if move == "A1":
                                    print("\n> I played C2")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2    | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A2) => ").upper()
                                        if move == "A2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "A2":
                                    print("\n> I played C2")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1    | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A1) => ").upper()
                                        if move == "A1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "C2":
                                    print("\n> I played A2")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1    | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | X | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A1) => ").upper()
                                        if move == "A1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "A2":
                            print("\n> I played C2")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1    | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  X | X | O     #\n"
                                    "#       -----------    #\n"
                                    "#     3    | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A1) => ").upper()
                                if move == "A1":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3    | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C1":
                                    print("\n> I played A3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1    | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A1) => ").upper()
                                        if move == "A1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "A3":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1    | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "C2":
                            print("\n> I played A2")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1    | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  O | X | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3    | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A1) => ").upper()
                                if move == "A1":
                                    print("\n> I played A3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | X | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C1) => ").upper()
                                        if move == "C1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "C1":
                                    print("\n> I played A3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1    | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | X | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A1) => ").upper()
                                        if move == "A1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "A3":
                                    print("\n> I played C1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1    | O | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | X | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A1) => ").upper()
                                        if move == "A1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "A3":
                            print("\n> I played C1")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1    | O | O     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | X |       #\n"
                                    "#       -----------    #\n"
                                    "#     3  X | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A1) => ").upper()
                                if move == "A1":
                                    print("\n> I played C2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "A2":
                                    print("\n> I played A1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  O | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | X |       #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C2":
                                    print("\n> I played A1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  O | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        else:
                            print("Invalid move, try again")
                else:
                    print("Invalid move, try again")
        elif move == "C2":
            print("\n> I played B2")
            while True:
                print("\n## Turn 2, Your move: ##\n"
                    "#                      #\n"
                    "#        A   B   C     #\n"
                    "#     1    |   |       #\n"
                    "#       -----------    #\n"
                    "#     2    | O | X     #\n"
                    "#       -----------    #\n"
                    "#     3    |   |       #\n"
                    "#                      #\n"
                    "########################"
                )
                move = input("Please select a square (e.g. A1) => ").upper()
                if move == "A1":
                    print("\n> I played C3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1  X |   |       #\n"
                            "#       -----------    #\n"
                            "#     2    | O | X     #\n"
                            "#       -----------    #\n"
                            "#     3    |   | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. B1) => ").upper()
                        if move == "B1":
                            print("\n> I played C1")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X | X | O     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3    |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A2) => ").upper()
                                if move == "A2":
                                    print("\n> I played A3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O |   | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "A3":
                                    print("\n> I played A2")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X |   | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B3":
                                    print("\n> I played A3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "C1":
                            print("\n> I played B1")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3    |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A2) => ").upper()
                                if move == "A2":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3    | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "A3":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "B3":
                                    print("\n> I played A3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2    | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A2) => ").upper()
                                        if move == "A2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "A2":
                            print("\n> I played A3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  X | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3  O |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X |       #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C1":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "B3":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "A3":
                            print("\n> I played A2")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  O | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3  X |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played C1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X |   | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "C1":
                                    print("\n> I played B1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X |   | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B3":
                                    print("\n> I played C1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X |   | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B1) => ").upper()
                                        if move == "B1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "B3":
                            print("\n> I played A3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3  O | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C1":
                                    print("\n> I played B1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2    | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A2) => ").upper()
                                        if move == "A2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "A2":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        else:
                            print("Invalid move, try again")
                elif move == "B1":
                    print("\n> I played C3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    | X |       #\n"
                            "#       -----------    #\n"
                            "#     2    | O | X     #\n"
                            "#       -----------    #\n"
                            "#     3    |   | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played C1")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X | X | O     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3    |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A2) => ").upper()
                                if move == "A2":
                                    print("\n> I played A3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O |   | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "A3":
                                    print("\n> I played A2")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X |   | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B3":
                                    print("\n> I played A3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "C1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "C1":
                    print("\n> I played C3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   | X     #\n"
                            "#       -----------    #\n"
                            "#     2    | O | X     #\n"
                            "#       -----------    #\n"
                            "#     3    |   | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played B1")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3    |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A2) => ").upper()
                                if move == "A2":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3    | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "A3":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "B3":
                                    print("\n> I played A3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2    | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A2) => ").upper()
                                        if move == "A2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "B1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "A2":
                    print("\n> I played C3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   |       #\n"
                            "#       -----------    #\n"
                            "#     2  X | O | X     #\n"
                            "#       -----------    #\n"
                            "#     3    |   | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played A3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  X | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3  O |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X |       #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C1":
                                    print("\n> I played B3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | O | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "B3":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "B1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "A3":
                    print("\n> I played C3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   |       #\n"
                            "#       -----------    #\n"
                            "#     2    | O | X     #\n"
                            "#       -----------    #\n"
                            "#     3  X |   | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played A2")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  O | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3  X |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played C1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X |   | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "C1":
                                    print("\n> I played B1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X |   | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B3":
                                    print("\n> I played C1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X |   | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B1) => ").upper()
                                        if move == "B1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "B1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   |       #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  X | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "B3":
                    print("\n> I played C3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   |       #\n"
                            "#       -----------    #\n"
                            "#     2    | O | X     #\n"
                            "#       -----------    #\n"
                            "#     3    | X | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played A3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3  O | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C1":
                                    print("\n> I played B1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2    | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A2) => ").upper()
                                        if move == "A2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "A2":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "B1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   |       #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  X | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "C3":
                    print("\n> I played C1")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   | O     #\n"
                            "#       -----------    #\n"
                            "#     2    | O | X     #\n"
                            "#       -----------    #\n"
                            "#     3    |   | X     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played A3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  O |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B1":
                            print("\n> I played A3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    | X | O     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  O |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played A3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  O |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A3":
                            print("\n> I played B3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1    |   | O     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3  X | O | X     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A1) => ").upper()
                                if move == "A1":
                                    print("\n> I played B1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | O | X     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "B1":
                                    print("\n> I played A1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  O | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2    | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | O | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A2) => ").upper()
                                        if move == "A2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  O | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | O | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "A2":
                                    print("\n> I played B1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1    | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | O | X     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "B3":
                            print("\n> I played A3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  O | X | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                else:
                    print("Invalid move, try again")
        elif move == "A3":
            print("\n> I played B2")
            while True:
                print("\n## Turn 2, Your move: ##\n"
                    "#                      #\n"
                    "#        A   B   C     #\n"
                    "#     1    |   |       #\n"
                    "#       -----------    #\n"
                    "#     2    | O |       #\n"
                    "#       -----------    #\n"
                    "#     3  X |   |       #\n"
                    "#                      #\n"
                    "########################"
                )
                move = input("Please select a square (e.g. A1) => ").upper()
                if move == "A1":
                    print("\n> I played A2")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1  X |   |       #\n"
                            "#       -----------    #\n"
                            "#     2  O | O |       #\n"
                            "#       -----------    #\n"
                            "#     3  X |   |       #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. B1) => ").upper()
                        if move == "B1":
                            print("\n> I played C2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X | X |       #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C1":
                            print("\n> I played C2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played C3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  O | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3  X |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played C1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X |   | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "C1":
                                    print("\n> I played B1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X |   | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B3":
                                    print("\n> I played C1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X |   | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B1) => ").upper()
                                        if move == "B1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "B3":
                            print("\n> I played C2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   |       #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3  X | X |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C3":
                            print("\n> I played C2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   |       #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "B1":
                    print("\n> I played C3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    | X |       #\n"
                            "#       -----------    #\n"
                            "#     2    | O |       #\n"
                            "#       -----------    #\n"
                            "#     3  X |   | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played A2")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X | X |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  O | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3  X |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. C1) => ").upper()
                                if move == "C1":
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | O |       #\n"
                                        "#       -----------    #\n"
                                        "#     3  X |   | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> You win, Congrats! <<<\n")
                                    return
                                elif move == "C2":
                                    print("\n> I played C1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X |   | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B3":
                                    print("\n> I played C2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X |       #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "C1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "C1":
                    print("\n> I played C2")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   | X     #\n"
                            "#       -----------    #\n"
                            "#     2    | O | O     #\n"
                            "#       -----------    #\n"
                            "#     3  X |   |       #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played A2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B1":
                            print("\n> I played A2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    | X | X     #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played A1")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  O |   | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2  X | O | O     #\n"
                                    "#       -----------    #\n"
                                    "#     3  X |   |       #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played C3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  O | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X |   | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "B3":
                                    print("\n> I played C3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  O |   | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C3":
                                    print("\n> I played B3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  O |   | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | O | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B1) => ").upper()
                                        if move == "B1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | O | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "B3":
                            print("\n> I played A2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3  X | X |       #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C3":
                            print("\n> I played A2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "A2":
                    print("\n> I played A1")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1  O |   |       #\n"
                            "#       -----------    #\n"
                            "#     2  X | O |       #\n"
                            "#       -----------    #\n"
                            "#     3  X |   |       #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. B1) => ").upper()
                        if move == "B1":
                            print("\n> I played C3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C1":
                            print("\n> I played C3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played C3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played C3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C3":
                            print("\n> I played B3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  O |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  X | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3  X | O | X     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played C1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  O | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | O | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C2) => ").upper()
                                        if move == "C2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  O | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | O | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "C1":
                                    print("\n> I played B1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  O | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O |       #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | O | X     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C2":
                                    print("\n> I played B1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  O | O |       #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | O | X     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        else:
                            print("Invalid move, try again")
                elif move == "C2":
                    print("\n> I played C3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   |       #\n"
                            "#       -----------    #\n"
                            "#     2    | O | X     #\n"
                            "#       -----------    #\n"
                            "#     3  X |   | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played A2")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  O | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3  X |   | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played C1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X |   | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "C1":
                                    print("\n> I played B1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X |   | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B3":
                                    print("\n> I played C1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X |   | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B1) => ").upper()
                                        if move == "B1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "B1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   |       #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  X | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "B3":
                    print("\n> I played C3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   |       #\n"
                            "#       -----------    #\n"
                            "#     2    | O |       #\n"
                            "#       -----------    #\n"
                            "#     3  X | X | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played A2")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  O | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3  X | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played C2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X |       #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C1":
                                    print("\n> I played C2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C2":
                                    print("\n> I played C1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X |   | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B1) => ").upper()
                                        if move == "B1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "B1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   |       #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  X | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "C3":
                    print("\n> I played B3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   |       #\n"
                            "#       -----------    #\n"
                            "#     2    | O |       #\n"
                            "#       -----------    #\n"
                            "#     3  X | O | X     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played B1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X | O | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B1":
                            print("\n> I played C1")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1    | X | O     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3  X | O | X     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A1) => ").upper()
                                if move == "A1":
                                    print("\n> I played A2")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | O | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C2) => ").upper()
                                        if move == "C2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | O | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "A2":
                                    print("\n> I played A1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  O | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | O | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C2) => ").upper()
                                        if move == "C2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  O | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | O | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "C2":
                                    print("\n> I played A1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  O | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2    | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | O | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A2) => ").upper()
                                        if move == "A2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  O | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | O | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "C1":
                            print("\n> I played B1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X | O | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played B1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    | O |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X | O | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played B1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    | O |       #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  X | O | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                else:
                    print("Invalid move, try again")
        elif move == "B3":
            print("\n> I played B2")
            while True:
                print("\n## Turn 2, Your move: ##\n"
                    "#                      #\n"
                    "#        A   B   C     #\n"
                    "#     1    |   |       #\n"
                    "#       -----------    #\n"
                    "#     2    | O |       #\n"
                    "#       -----------    #\n"
                    "#     3    | X |       #\n"
                    "#                      #\n"
                    "########################"
                )
                move = input("Please select a square (e.g. A1) => ").upper()
                if move == "A1":
                    print("\n> I played C3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1  X |   |       #\n"
                            "#       -----------    #\n"
                            "#     2    | O |       #\n"
                            "#       -----------    #\n"
                            "#     3    | X | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. B1) => ").upper()
                        if move == "B1":
                            print("\n> I played C1")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X | X | O     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3    | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A2) => ").upper()
                                if move == "A2":
                                    print("\n> I played C2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3    | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C2":
                                    print("\n> I played A3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "A3":
                                    print("\n> I played C2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "C1":
                            print("\n> I played B1")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3    | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A2) => ").upper()
                                if move == "A2":
                                    print("\n> I played A3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C2) => ").upper()
                                        if move == "C2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "C2":
                                    print("\n> I played A3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2    | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A2) => ").upper()
                                        if move == "A2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "A3":
                                    print("\n> I played A2")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C2) => ").upper()
                                        if move == "C2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "A2":
                            print("\n> I played A3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  X | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3  O | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O |       #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C1":
                                    print("\n> I played B1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C2) => ").upper()
                                        if move == "C2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "C2":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "C2":
                            print("\n> I played A3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3  O | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C1":
                                    print("\n> I played B1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2    | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A2) => ").upper()
                                        if move == "A2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "A2":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "A3":
                            print("\n> I played A2")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  O | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3  X | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played C2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X |       #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C1":
                                    print("\n> I played C2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C2":
                                    print("\n> I played C1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X |   | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B1) => ").upper()
                                        if move == "B1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        else:
                            print("Invalid move, try again")
                elif move == "B1":
                    print("\n> I played C3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    | X |       #\n"
                            "#       -----------    #\n"
                            "#     2    | O |       #\n"
                            "#       -----------    #\n"
                            "#     3    | X | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played C1")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X | X | O     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3    | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A2) => ").upper()
                                if move == "A2":
                                    print("\n> I played C2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3    | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C2":
                                    print("\n> I played A3")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "A3":
                                    print("\n> I played C2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "C1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "C1":
                    print("\n> I played C3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   | X     #\n"
                            "#       -----------    #\n"
                            "#     2    | O |       #\n"
                            "#       -----------    #\n"
                            "#     3    | X | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played B1")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3    | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A2) => ").upper()
                                if move == "A2":
                                    print("\n> I played A3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C2) => ").upper()
                                        if move == "C2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "C2":
                                    print("\n> I played A3")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2    | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A2) => ").upper()
                                        if move == "A2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "A3":
                                    print("\n> I played A2")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C2) => ").upper()
                                        if move == "C2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "B1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "A2":
                    print("\n> I played C3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   |       #\n"
                            "#       -----------    #\n"
                            "#     2  X | O |       #\n"
                            "#       -----------    #\n"
                            "#     3    | X | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played A3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  X | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3  O | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O |       #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C1":
                                    print("\n> I played B1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C2) => ").upper()
                                        if move == "C2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "C2":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "B1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "C2":
                    print("\n> I played C3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   |       #\n"
                            "#       -----------    #\n"
                            "#     2    | O | X     #\n"
                            "#       -----------    #\n"
                            "#     3    | X | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played A3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3  O | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C1":
                                    print("\n> I played B1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2    | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A2) => ").upper()
                                        if move == "A2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "A2":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "B1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3    | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A3":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   |       #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  X | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "A3":
                    print("\n> I played C3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   |       #\n"
                            "#       -----------    #\n"
                            "#     2    | O |       #\n"
                            "#       -----------    #\n"
                            "#     3  X | X | O     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played A2")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  O | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3  X | X | O     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played C2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X |       #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C1":
                                    print("\n> I played C2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | X | O     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C2":
                                    print("\n> I played C1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X |   | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | X | O     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B1) => ").upper()
                                        if move == "B1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | X | O     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "B1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O | X |       #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C1":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played A1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  O |   |       #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  X | X | O     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "C3":
                    print("\n> I played A3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   |       #\n"
                            "#       -----------    #\n"
                            "#     2    | O |       #\n"
                            "#       -----------    #\n"
                            "#     3  O | X | X     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O | X | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B1":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    | X | O     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O | X | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C1":
                            print("\n> I played C2")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1    |   | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O | O     #\n"
                                    "#       -----------    #\n"
                                    "#     3  O | X | X     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A1) => ").upper()
                                if move == "A1":
                                    print("\n> I played A2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | X     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "B1":
                                    print("\n> I played A2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1    | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | X     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "A2":
                                    print("\n> I played A1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  O |   | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B1) => ").upper()
                                        if move == "B1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "A2":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O | X | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  O | X | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                else:
                    print("Invalid move, try again")
        elif move == "C3":
            print("\n> I played B2")
            while True:
                print("\n## Turn 2, Your move: ##\n"
                    "#                      #\n"
                    "#        A   B   C     #\n"
                    "#     1    |   |       #\n"
                    "#       -----------    #\n"
                    "#     2    | O |       #\n"
                    "#       -----------    #\n"
                    "#     3    |   | X     #\n"
                    "#                      #\n"
                    "########################"
                )
                move = input("Please select a square (e.g. A1) => ").upper()
                if move == "A1":
                    print("\n> I played C2")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1  X |   |       #\n"
                            "#       -----------    #\n"
                            "#     2    | O | O     #\n"
                            "#       -----------    #\n"
                            "#     3    |   | X     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. B1) => ").upper()
                        if move == "B1":
                            print("\n> I played A2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X | X |       #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3    |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C1":
                            print("\n> I played A2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3    |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played A3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1  X |   |       #\n"
                                    "#       -----------    #\n"
                                    "#     2  X | O | O     #\n"
                                    "#       -----------    #\n"
                                    "#     3  O |   | X     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. B1) => ").upper()
                                if move == "B1":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O |   | X     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "C1":
                                    print("\n> I played B1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O |   | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B3":
                                    print("\n> I played C1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | X     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "A3":
                            print("\n> I played A2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   |       #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played A2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   |       #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3    | X | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "B1":
                    print("\n> I played A3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    | X |       #\n"
                            "#       -----------    #\n"
                            "#     2    | O |       #\n"
                            "#       -----------    #\n"
                            "#     3  O |   | X     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X | X | O     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C1":
                            print("\n> I played C2")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1    | X | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O | O     #\n"
                                    "#       -----------    #\n"
                                    "#     3  O |   | X     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A1) => ").upper()
                                if move == "A1":
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O |   | X     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> You win, Congrats! <<<\n")
                                    return
                                elif move == "A2":
                                    print("\n> I played A1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  O | X | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O |   | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B3":
                                    print("\n> I played A2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1    | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | X     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "A2":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    | X | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    | X | O     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  O |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    | X | O     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O | X | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "C1":
                    print("\n> I played C2")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   | X     #\n"
                            "#       -----------    #\n"
                            "#     2    | O | O     #\n"
                            "#       -----------    #\n"
                            "#     3    |   | X     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played A2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3    |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B1":
                            print("\n> I played A2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    | X | X     #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3    |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played A3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1    |   | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2  X | O | O     #\n"
                                    "#       -----------    #\n"
                                    "#     3  O |   | X     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A1) => ").upper()
                                if move == "A1":
                                    print("\n> I played B1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O |   | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B1":
                                    print("\n> I played A1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  O | X | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O |   | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B3":
                                    print("\n> I played A1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  O |   | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B1) => ").upper()
                                        if move == "B1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "A3":
                            print("\n> I played A2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3  X |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played A2")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    |   | X     #\n"
                                "#       -----------    #\n"
                                "#     2  O | O | O     #\n"
                                "#       -----------    #\n"
                                "#     3    | X | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "A2":
                    print("\n> I played A3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   |       #\n"
                            "#       -----------    #\n"
                            "#     2  X | O |       #\n"
                            "#       -----------    #\n"
                            "#     3  O |   | X     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B1":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    | X | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C1":
                            print("\n> I played C2")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1    |   | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2  X | O | O     #\n"
                                    "#       -----------    #\n"
                                    "#     3  O |   | X     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A1) => ").upper()
                                if move == "A1":
                                    print("\n> I played B1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O |   | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B1":
                                    print("\n> I played A1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  O | X | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O |   | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B3) => ").upper()
                                        if move == "B3":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "B3":
                                    print("\n> I played A1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  O |   | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B1) => ").upper()
                                        if move == "B1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "C2":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  O |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B3":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O | X | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "C2":
                    print("\n> I played C1")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   | O     #\n"
                            "#       -----------    #\n"
                            "#     2    | O | X     #\n"
                            "#       -----------    #\n"
                            "#     3    |   | X     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played A3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  O |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B1":
                            print("\n> I played A3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    | X | O     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  O |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played A3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  O |   | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A3":
                            print("\n> I played B3")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1    |   | O     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O | X     #\n"
                                    "#       -----------    #\n"
                                    "#     3  X | O | X     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A1) => ").upper()
                                if move == "A1":
                                    print("\n> I played B1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2    | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | O | X     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "B1":
                                    print("\n> I played A1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  O | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2    | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | O | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A2) => ").upper()
                                        if move == "A2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  O | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | O | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "A2":
                                    print("\n> I played B1")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1    | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     2  X | O | X     #\n"
                                        "#       -----------    #\n"
                                        "#     3  X | O | X     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                else:
                                    print("Invalid move, try again")
                        elif move == "B3":
                            print("\n> I played A3")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  O | X | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "A3":
                    print("\n> I played B3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   |       #\n"
                            "#       -----------    #\n"
                            "#     2    | O |       #\n"
                            "#       -----------    #\n"
                            "#     3  X | O | X     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played B1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X | O | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B1":
                            print("\n> I played C1")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1    | X | O     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O |       #\n"
                                    "#       -----------    #\n"
                                    "#     3  X | O | X     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A1) => ").upper()
                                if move == "A1":
                                    print("\n> I played A2")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  X | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  O | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | O | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C2) => ").upper()
                                        if move == "C2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  X | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  O | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | O | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "A2":
                                    print("\n> I played A1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  O | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O |       #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | O | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. C2) => ").upper()
                                        if move == "C2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  O | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | O | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                elif move == "C2":
                                    print("\n> I played A1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  O | X | O     #\n"
                                            "#       -----------    #\n"
                                            "#     2    | O | X     #\n"
                                            "#       -----------    #\n"
                                            "#     3  X | O | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. A2) => ").upper()
                                        if move == "A2":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  O | X | O     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | X     #\n"
                                                "#       -----------    #\n"
                                                "#     3  X | O | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "C1":
                            print("\n> I played B1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X | O | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "A2":
                            print("\n> I played B1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    | O |       #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  X | O | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played B1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    | O |       #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  X | O | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                elif move == "B3":
                    print("\n> I played A3")
                    while True:
                        print("\n## Turn 3, Your move: ##\n"
                            "#                      #\n"
                            "#        A   B   C     #\n"
                            "#     1    |   |       #\n"
                            "#       -----------    #\n"
                            "#     2    | O |       #\n"
                            "#       -----------    #\n"
                            "#     3  O | X | X     #\n"
                            "#                      #\n"
                            "########################"
                        )
                        move = input("Please select a square (e.g. A1) => ").upper()
                        if move == "A1":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1  X |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O | X | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "B1":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    | X | O     #\n"
                                "#       -----------    #\n"
                                "#     2    | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O | X | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C1":
                            print("\n> I played C2")
                            while True:
                                print("\n## Turn 4, Your move: ##\n"
                                    "#                      #\n"
                                    "#        A   B   C     #\n"
                                    "#     1    |   | X     #\n"
                                    "#       -----------    #\n"
                                    "#     2    | O | O     #\n"
                                    "#       -----------    #\n"
                                    "#     3  O | X | X     #\n"
                                    "#                      #\n"
                                    "########################"
                                )
                                move = input("Please select a square (e.g. A1) => ").upper()
                                if move == "A1":
                                    print("\n> I played A2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1  X |   | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | X     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "B1":
                                    print("\n> I played A2")
                                    print("\n########################\n"
                                        "#                      #\n"
                                        "#        A   B   C     #\n"
                                        "#     1    | X | X     #\n"
                                        "#       -----------    #\n"
                                        "#     2  O | O | O     #\n"
                                        "#       -----------    #\n"
                                        "#     3  O | X | X     #\n"
                                        "#                      #\n"
                                        "########################"
                                    )
                                    print(">>> I win, Good game! <<<\n")
                                    return
                                elif move == "A2":
                                    print("\n> I played A1")
                                    while True:
                                        print("\n## Turn 5, Your move: ##\n"
                                            "#                      #\n"
                                            "#        A   B   C     #\n"
                                            "#     1  O |   | X     #\n"
                                            "#       -----------    #\n"
                                            "#     2  X | O | O     #\n"
                                            "#       -----------    #\n"
                                            "#     3  O | X | X     #\n"
                                            "#                      #\n"
                                            "########################"
                                        )
                                        move = input("Please select a square (e.g. B1) => ").upper()
                                        if move == "B1":
                                            print("\n########################\n"
                                                "#                      #\n"
                                                "#        A   B   C     #\n"
                                                "#     1  O | X | X     #\n"
                                                "#       -----------    #\n"
                                                "#     2  X | O | O     #\n"
                                                "#       -----------    #\n"
                                                "#     3  O | X | X     #\n"
                                                "#                      #\n"
                                                "########################"
                                            )
                                            print(">>> It's a tie! <<<\n")
                                            return
                                        else:
                                            print("Invalid move, try again")
                                else:
                                    print("Invalid move, try again")
                        elif move == "A2":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2  X | O |       #\n"
                                "#       -----------    #\n"
                                "#     3  O | X | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        elif move == "C2":
                            print("\n> I played C1")
                            print("\n########################\n"
                                "#                      #\n"
                                "#        A   B   C     #\n"
                                "#     1    |   | O     #\n"
                                "#       -----------    #\n"
                                "#     2    | O | X     #\n"
                                "#       -----------    #\n"
                                "#     3  O | X | X     #\n"
                                "#                      #\n"
                                "########################"
                            )
                            print(">>> I win, Good game! <<<\n")
                            return
                        else:
                            print("Invalid move, try again")
                else:
                    print("Invalid move, try again")
        else:
            print("Invalid move, try again")


if __name__ == "__main__":
    while True:
        game()
        again = input("Do you want to play again (y/n) => ")
        if again == "y":
            continue
        else:
            print("I hope you enjoyed my game, bye!\n")
            break

