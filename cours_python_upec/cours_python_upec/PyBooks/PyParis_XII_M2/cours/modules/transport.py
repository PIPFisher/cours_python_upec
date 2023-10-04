import datetime as dt

def liste_vols_vers_liste(liste_vols, separateur=';'):
    '''
    Transforme une liste de chaines de caractères en liste de liste de caractéristiques

    :param liste_vols: liste de données brutes (str), un élément par vol
    :param separateur: séparateur utilisé pour les caractéristiques du vol
    :return: liste de listes de caractéristiques de vols
    '''
    
    resultat = []
    
    for ligne in liste_vols:
        resultat.append(ligne.split(separateur))
        
    return resultat

def moyenne(liste):
    '''
    Calcule la moyenne des valeurs d'une liste
    '''
    
    somme = 0
    nombre_valeurs = 0
    
    for chiffre in liste:
        somme += chiffre
        nombre_valeurs += 1
    
    return somme/nombre_valeurs

def mappage(fonction, liste):
    '''
    Applique une même fonction à tous les éléments d'une liste

    :param data: liste de données brutes (str), un élément par vol
    :param sep: séparateur utilisé pour les caractéristiques du vol
    :return: liste de listes de caractéristiques de vols
    '''
    
    resultat = []
    
    for element in liste:
        resultat.append(fonction(element))
        
    return resultat


class Deplacement:
    '''
    Objet représentant un déplacement
    '''

    def __init__(self, origin, destination, date_dep, date_arr):
        '''
        Constructeur

        :param origin: nom d'origine du lieu (str)
        :param destination: nom de destination du déplacement (str)
        :param date_dep: date de départ (str, au format 2016-03-15T22:05:00)
        :param date_arr: date d'arrivée (str, au format 2016-03-15T22:05:00)
        '''
        # attributs publics
        self.origin = origin
        self.destination = destination
        # attributs privés
        self.__date_dep = date_dep
        self.__date_arr = date_arr
        self.__duree = 0

    def __str__(self):
        return f'OD : {self.origin} - {self.destination}'
        
    def fixer_duree(self):
        dep = dt.datetime.strptime(self.__date_dep, '%Y-%m-%dT%H:%M:%S')
        arr = dt.datetime.strptime(self.__date_arr, '%Y-%m-%dT%H:%M:%S')
        self.__duree = (arr - dep).seconds
    
    def dire_duree(self):
        self.fixer_duree()
        return '{:.2f}'.format(self.__duree/3600)