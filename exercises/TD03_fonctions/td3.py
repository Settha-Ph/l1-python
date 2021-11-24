import time

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

def isBissextile(annee):
    """Fonction qui vérifie si une année est bissextile"""
    l = [annee]
    if ((annee%4 == 0 and annee%100 != 0) or annee%400 == 0):
        return True
    else:
        return False

#Prend un tuple en argument et renvoie un tuple  (tempsEnDate : (int*int*int*int) -> (int*int*int*int*int*int))
def tempsEnDate(temps):
    """Donne la date sous la forme (année, mois, jour, heure, minute, seconde) en prenant en compte le nombre de jour dans le mois et les années bissextiles"""
    totalJour = temps[0]
    #Vérifie si l'année est bissextile pour soustraire le bon nombre de jour
    annee = 1970
    while totalJour >= 365 :
        annee += 1
        if isBissextile(annee):
            totalJour -= 366
        else:
            totalJour -= 365

    #Vérifie le nombre de jour dans un mois
    listeMoisAvecPlusDeJour = [1, 3, 5, 7, 8, 10, 12]
    mois = 1
    while totalJour >= 30:
        mois += 1
        if mois == 2 and isBissextile(annee):
            totalJour -= 29
        elif mois == 2 and not isBissextile(annee):
            totalJour -= 28
        elif mois in listeMoisAvecPlusDeJour:
            totalJour -= 31
        else:
            totalJour -= 30

    
    jour = totalJour
    heure = temps[1]
    minute = temps[2]
    sec = temps[3]
    return(annee, mois, jour, heure, minute, sec)
    
    


def afficheDate(date = -1):
    if date == -1:
        print(time.gmtime)
    else:
        listeMois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
        res = str(date[2]) + " " + str(listeMois[date[1] - 1]) + " " + str(date[0]) + " " + str(date[3]) + ":" + str(date[4]) + ":" + str(date[5])
        print(res)
    
    

#temps = secondeEnTemps(1000000000)
#afficheTemps(temps)
#afficheDate(tempsEnDate(temps))
#afficheDate()


#nombreBisextile prend un int en argument et renvoie un int (nombreBisextile : int -> int)
def nombreBisextile(jour):
    """Renvoie le nombre d'années bissextiles pour un nombre de jour donnée"""
    annee = 1970
    res = 0
    while jour >= 365 :
        annee += 1
        if isBissextile(annee):
            jour -= 366
            res += 1
        else:
            jour -= 365
    return res


def tempsEnDateBisextile(temps):
    """Voir la fonction tempsEnDate"""
    pass

#bisextile(20000)


def verifie(liste_temps):
    """Vérifie si la charge horaire donnée par une liste ne dépasse pas 48h par semaine et 140h par mois, renvoie un booleean"""
    isAbove = False
    res = []
    listeSommeMois = []
    for i in range(len(liste_temps)):
        sommeMois = 0
        for j in range(len(liste_temps[i])):
            if liste_temps[i][j] > 48:
                res.append((i+1, j+1, liste_temps[i][j]))
                isAbove = True
            sommeMois += liste_temps[i][j]

        if sommeMois > 140:
            isAbove = True
            listeSommeMois.append((i+1, sommeMois))

    if res:
        for e in res:
            print("Mois : {0}, Semaine : {1}, {2}h de travail !".format(e[0], e[1], e[2]))
        print("\n")

    if listeSommeMois:
        for e in listeSommeMois:
            print("Le mois {0} comptabilise {1} de travail !".format(e[0], e[1]))

    return isAbove


#liste_temps = [[1,2,39,34],[0,1,9,4],[0,29,39,51],[0,31,13,46]]
#verifie(liste_temps)



def calculs(b,c):
    a = 2
    c = a * 2
    a = 1
    return a + b
    
def dernierExo():
    c = 1
    b = calculs(3,4)
    print(a,b,c)