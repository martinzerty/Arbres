class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.enfant_droit = None
        self.enfant_gauche = None
    def insert(self, valeur):
        arbre = self
        while arbre:
            x = arbre
            if valeur == x.valeur:
                break
            elif valeur < x.valeur:
                arbre = arbre.enfant_gauche
            elif valeur > x.valeur:
                arbre = arbre.enfant_droit
        if valeur < x.valeur:
            x.enfant_gauche = Noeud(valeur)
        else:
            x.enfant_droit = Noeud(valeur)
