import random as rd

print("Welcome to the game:")

c = 0
p = 0
a = 1
while True:
    if a == 4:
        if p > c:
            print("----------*Player won*----------")
        elif p == c:
            print("----------*It's a draw*----------")
        else:
            print("----------*Computer won*-----------")
        break
    else:
        x = input('''Please type one of the given below:
stone
paper
scissors
quit
Type here: ''')
        action = ['stone','paper','scissors']
        y = rd.choice(action)
        if x == y:
            print("Computer: ",y)
            print('''Draw.
Player = {}
Computer = {}'''.format(p,c))
        elif x == "stone" and y == "paper":
            print("Computer: ",y)
            c = c+1
            print('''Computer won.
Player = {}
Computer = {}'''.format(p,c))
        elif x == "stone" and y == "scissors":
            print("Computer: ",y)
            p = p+1
            print('''You won.
Player = {}
Computer = {}'''.format(p,c))
        elif x == "paper" and y == "stone":
            print("Computer: ",y)
            p = p+1
            print('''You won.
Player = {}
Computer = {}'''.format(p,c))
        elif x == "paper" and y == "scissors":
            print("Computer: ",y)
            c = c+1
            print('''Computer won.
Player = {}
Computer = {}'''.format(p,c))
        elif x == "scissors" and y == "stone":
            print("Computer: ",y)
            c = c+1
            print('''Computer won.
Player = {}
Computer = {}'''.format(p,c))
        elif x == "scissors" and y == "paper":
            print("Computer: ",y)
            p = p+1
            print('''You won.
Player = {}
Computer = {}'''.format(p,c))
        else:
            print("Please enter correct value.")

    a = a+1
