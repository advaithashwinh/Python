while(1):
    user1 = input("Player1, do you want to choose rock, paper or scissors?")
    user2 = input("Player2, do you want to choose rock, paper or scissors?")
    def rcp(u1, u2):
        if u1 == u2:
            return("It's a tie!")
        elif u1 == 'r':
            if u2 == 's':
                return("Rock wins!")
            else:
                return("Paper wins!")
        elif u1 == 's':
            if u2 == 'p':
                return("Scissors win!")
            else:
                return("Rock wins!")
        elif u1 == 'p':
            if u2 == 'r':
                return("Paper wins!")
            else:
                return("Scissors win!")
        else:
                return("Invalid input! You have not entered rock, paper or scissors, try again.")

    print(rcp(user1,user2))

    r=input("Another round? y/n")
    if r == 'n':
        break
