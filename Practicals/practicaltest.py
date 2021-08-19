from heroenemy import heroenemy
from errors import MismatchError,CharacterError

i=0
list=[]

while(1):
    e1 = input("Enter energies of enemies (Use space to separate energies):")
    h1 = input("Enter strengths of heroes \n(Use space to separate energies) \n(Number of entries should be equal to that of enemies):")
    list.append(heroenemy(e1, h1))
    [e,h] = list[i].split(e1,h1)

    try:
        print(list[i].game(e, h))
    except MismatchError:
        print("Inequal number of elements for heroes and enemies")
    except CharacterError:
        print("Wrong delimeter used/Non-numeric character used")

    i=i+1
    if input("Another game?y/n:") == 'n':
        break














