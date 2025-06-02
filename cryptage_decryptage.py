def cryptage_mdp(mdp):
    x=[]
    for i in mdp:
        z=ord(i)
        x.append(bin(z))
    return x

def decryptage_mdp(mdp):
    x=''
    for i in mdp:
        z=int(i,2)
        x+=chr(z)
    return x