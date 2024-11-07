class Element:
    def __init__(self, valeur, suivant = None) :
        self.valeur = valeur
        self.suivant = suivant

class Liste:
    def __init__(self) :
        self.premier_element = None
        self.dernier_element = None

    def ajout(self, valeur_element):

        nouvel_element = Element(valeur_element)

        if self.premier_element == None :
            self.premier_element = nouvel_element
        else :
            self.dernier_element.suivant = nouvel_element
        
        self.dernier_element = nouvel_element

    def afficher_tout(self) :

        element_actuel = self.premier_element

        while element_actuel is not None:
            print(element_actuel.valeur)
            element_actuel = element_actuel.suivant

    def supprimer_dernier(self) :

        element_actuel = self.premier_element

        while element_actuel.suivant != self.dernier_element :
            element_actuel = element_actuel.suivant

        #en sortant de la boucle, element_actuel contient l'élément précédant l'élément à supprimer
        # cad l'avant dernier élément de ma liste
        self.dernier_element = element_actuel
        self.dernier_element.suivant = None

    def remplacer_element(self, valeur_element_a_remplacer, nouvelle_valeur) :    

        element_actuel = self.premier_element

        while element_actuel != None :

            if element_actuel.valeur == valeur_element_a_remplacer :
                element_actuel.valeur = nouvelle_valeur
    
            element_actuel = element_actuel.suivant


    def sous_liste(self, index_debut, index_fin) :    
        
        nouvelle_liste = Liste()
        index_actuel = 0

        element_actuel = self.premier_element

        while index_actuel <= index_fin  and element_actuel != None :
            
            if index_actuel >= index_debut :
                nouvelle_liste.ajout(element_actuel.valeur)

            element_actuel = element_actuel.suivant
            index_actuel += 1

        return nouvelle_liste
    
    def sous_liste_for(self, index_debut, index_fin) :    
        
        nouvelle_liste = Liste()
        element_actuel = self.premier_element

        for index_actuel in range(index_fin + 1) :
            
            if index_actuel >= index_debut :
                nouvelle_liste.ajout(element_actuel.valeur)

            element_actuel = element_actuel.suivant

            if element_actuel == None :
                return nouvelle_liste
        
        return nouvelle_liste

    def donne_inverse(self) :

        liste_inverse = Liste()

        element_actuel = self.premier_element

        while element_actuel is not None:
            liste_inverse.ajout_debut(element_actuel)
            element_actuel = element_actuel.suivant


        return liste_inverse

    
    def ajout_debut(self, valeur_element):

        nouvel_element = Element(valeur_element)

        nouvel_element.suivant = self.premier_element

        self.premier_element = nouvel_element

        if self.dernier_element == None :
            self.dernier_element = nouvel_element

    def afficher_inverse(self) :
        affichage = ""

        while element_actuel is not None:
            affichage = element_actuel.valeur + "\n" + affichage
            element_actuel = element_actuel.suivant

        print(affichage)

    #--- exo 3 ----
    def inverse(self):
        """Méthode qui inverse les éléments de la liste elle-même"""
        previous_element = None
        current_element = self.premier_element
        self.dernier_element = self.premier_element  # Le premier élément deviendra le dernier après inversion

        while current_element is not None:
            next_element = current_element.suivant   # Sauvegarde l'élément suivant avant de changer le lien

            current_element.suivant = previous_element

            previous_element = current_element
            current_element = next_element

        self.premier_element = previous_element



alphabet = Liste()

alphabet.ajout("b") #0
alphabet.ajout("a") #1
alphabet.ajout("e") #2
alphabet.ajout("i") #3
alphabet.ajout_debut("c") #4

