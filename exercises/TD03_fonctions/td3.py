"""temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes"""


def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    res = temps[0] * 86400 + temps[1]*(60*60) + temps[2]*60 + temps[3]
    return res


#temps = (3, 23, 1, 34)
#print(type(temps))
#print(tempsEnSeconde(temps))   


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jour = seconde // 86400
    heure = (seconde // 3600) % 24
    min = (seconde // 60) % 60
    sec = seconde % 60

    return (jour, heure, min, sec)


#temps = secondeEnTemps(100000)
#print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")


def afficheTemps(temps):
    """Affiche le temps, n'affiche pas les valeurs de temps égal à 0 et met les mots au pluriel si besoin"""
    l = ["jour", "heure", "minute", "seconde"]
    res = ""

    for i in range(len(temps)):
        if temps[i] == 0:
            continue
        elif (temps[i] > 1):
            res += str(temps[i]) + " " + l[i] + 's'
        else:
            res += str(temps[i]) + " " + l[i]
        res += " "
    print(res)


#afficheTemps((1,0,14,23))


def demandeTemps():
    """Renvoie le temps que l'utilisateur à rentré"""
    l = ["jour", "heure", "minute", "seconde"]
    res = []
    for i in range(4):
        isCorrect = False
        while not isCorrect:
            n = int(input("Entrez le nombre de " + l[i] + " :"))
            if n is None or n < 0:
                print("Merci d'entrer une valeur correcte")
            elif i ==  1 and  n >= 24 :
                print("Merci d'entrer une valeur correcte")
            elif (i == 2 or i == 3) and n >= 60:
                print("Merci d'entrer une valeur correcte")
            else:
                res.append(n)
                isCorrect = True
    return (res[0], res[1], res[2], res[3])
     

#afficheTemps(demandeTemps())

def sommeTemps(temps1,temps2):
    """La somme de deux temps"""
    res = secondeEnTemps(tempsEnSeconde(temps1) + tempsEnSeconde(temps2))
    afficheTemps(res)

#sommeTemps((2,3,4,25),(5,22,57,1))

def proportionTemps(temps,proportion):
    if type(temps) != tuple:
        temps, proportion = proportion, temps
    secondes = tempsEnSeconde(temps)
    secondes *= proportion
    res = secondeEnTemps(int(secondes))
    return res
    

#afficheTemps(proportionTemps(0.2, (2,0,36,0)))


def tempsEnDate(temps):
    année = 1970 + temps[0] // 365
    jour = temps[0] % 31
    heure = temps[1]
    minute = temps[2]
    sec = temps[3]
    return(année, jour, heure, minute, sec)
    
    


def afficheDate(date = -1):
    mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]

    print(date)
    

temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDate(temps))
#afficheDate()