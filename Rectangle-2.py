import copy

class Rectangle2:
    def __init__(self, _largeur, _langeur, _Nbrrectangle):
        self._largeur = _largeur
        self._langeur = _langeur
        self._Nbrrectangle = _Nbrrectangle

    def getlargeur(self):
        return self._largeur

    def getlangeur(self):
        return self._langeur

    def setlargeur(self, newlargeur):
        self._largeur = newlargeur

    def setlangeur(self, newlangeur):
        self._langeur = newlangeur

    def getNbrrectangle(self):
        return self._Nbrrectangle

    def info(self):
        print("le rectangle 1, a une largeur de {} et une longueur de {} et un nombre de rectangle {}".
              format(self._largeur, self._langeur, self._Nbrrectangle))

    def perimetre(self):
        return (self._langeur + self._largeur) * 2

    def surface(self):
        return (self._langeur * self._largeur)


class Parallélépipéde(Rectangle2):
    def __init__(self, _largeur, _langeur, _Nbrrectangle, _Hauteur, _NbrParrallélépides):
        super().__init__(_largeur, _langeur, _Nbrrectangle)
        self._Hauteur = _Hauteur
        self._NbrParrallélépides = _NbrParrallélépides

    def gethauteur(self):
        return self._Hauteur

    def sethauteur(self, newHauteur):
        self._Hauteur = newHauteur

    def getNbrParrallélépides(self):
        return self._NbrParrallélépides

    def Equal(self):
        pass

    def surface(self):
        return (self._langeur * self._largeur)

    def Tostring(self):
        print(f'Le rectangle')

    def Volume(self):
        return (self._langeur * self._largeur * self._Hauteur)


# Example of creating instances:
rec1 = Rectangle2(5, 10, 1)
rec2 = copy.deepcopy(rec1)

rec1.info()
print("Surface de rectangle 1:", rec1.surface())

# Example of creating instances for Parallélépipéde:
par1 = Parallélépipéde(5, 10, 1, 3, 2)
print("Surface de parrallélépides 1 :", par1.surface())
print("Volume de parrallélépides 1 :", par1.Volume())
