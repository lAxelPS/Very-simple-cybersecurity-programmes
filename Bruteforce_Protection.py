import getpass
import os
import random
def bruteforce():
    mdp='password'
    n=1
    x=getpass.getpass()
    while x!=mdp and n!=3:
        x=getpass.getpass()
        n+=1
    if n==3 and x==mdp:
        desktop_path=os.path.join(os.path.expanduser('~'),'Desktop')
        code=random.randint(1000, 9999)
        file_path = os.path.join(desktop_path,'double authentification code.txt')
        with open(file_path, 'w') as file:
            file.write(str(code))
        c=int(input('Enter the code that is in the txt file name double authentification:'))
        if c!=code:
            print('This is a bruteforce attack')
            return True
        else:
            print('Thank you for getting authentificated')
            return False
    elif x==mdp and n!=3:
        print('Thank you for getting authentificated')
        return False

print(bruteforce())