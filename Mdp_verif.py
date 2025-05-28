import getpass

def verif_mdp():
    alphabet1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphabet2=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    signs=['@','&','_','-','.','!','(',')','/','%','$','£','€']
    numbers=['0','1','2','3','4','5','6','7','8','9']
    c=[0,0,0,0]
    mdp=getpass.getpass()
    if len(mdp)<12:
        print('mot de passe faible, veuillez recommencer')
        return(verif_mdp())
    for i in mdp:
        if i in alphabet1:
            c[0]=1
        elif i in alphabet2:
            c[1]=1
        elif i in signs:
            c[2]=1
        elif i in numbers:
            c[3]=1
    x=0
    for i in range(len(c)):
        x+=c[i]
    if x<=1:
        print('mot de passe faible, veuillez recommencer')
        return(verif_mdp())
    elif x==2:
        print('mot de passe moyen, veuillez recommencer')
        return(verif_mdp())
    else:
        print('mot de passe fort, mot de passe accepter')
        return True

verif_mdp()
