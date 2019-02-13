def hangman(word):
    wrong = 0

    stages = ["",
              "_____________",
              "|     |      ",
              "|     o      ",
              "|   / | \    ",
              "|    / \     ",
              "|            "
              ]

    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to hangman!")

    while wrong < len(stages) - 2:
        char = input("guess a character.:")
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
            print("Collect!")
        else:
            print ("False!")
            wrong +=1

        print(board)
        print("\n".join(stages[0:wrong+2]))

        if "_" not in board:
            print("You win the game!")
            win = True
            break

    if  win != True:
        print("You lose... the word is {}.".format(word))

hangman("apple")
