import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        # On initialise le cercle soit par son rayon, soit par son diamètre
        if radius is not None:
            self._radius = radius
        elif diameter is not None:
            self._radius = diameter / 2
        else:
            raise ValueError("You must specify either a radius or a diameter.")

    # --- Gestion du rayon (Getter et Setter) ---
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

    # --- Gestion du diamètre via un Décorateur ---
    @property
    def diameter(self):
        # Le diamètre est automatiquement calculé à partir du rayon
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        # Si l'utilisateur modifie le diamètre, cela modifie le rayon en arrière-plan
        if value < 0:
            raise ValueError("Diameter cannot be negative.")
        self._radius = value / 2

    # --- ✅ Capacité 1 : Calculer l'aire ---
    @property
    def area(self):
        # Formule : Pi * R²
        return math.pi * (self._radius ** 2)

    # --- ✅ Capacité 2 : Afficher les attributs (Dunder method) ---
    def __repr__(self):
        # Représentation officielle de l'objet (idéal pour l'affichage dans une liste)
        return f"Circle(radius={self._radius})"

    def __str__(self):
        # Version lisible pour l'utilisateur lors d'un 'print()'
        return f"Circle with Radius: {self.radius:.2f}, Diameter: {self.diameter:.2f}, Area: {self.area:.2f}"

    # --- ✅ Capacité 3 : Additionner deux cercles (Dunder method) ---
    def __add__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        # Retourne un NOUVEAU cercle avec la somme des deux rayons
        return Circle(radius=self.radius + other.radius)

    # --- ✅ Capacité 5 : Vérifier l'égalité (Dunder method) ---
    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius

    # --- ✅ Capacité 6 : Permettre le tri automatique (Dunder method) ---
    def __lt__(self, other):
        # __lt__ signifie "Less Than" (<). Python l'utilise pour la fonction sort()
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius

    # --- ✅ Capacité 4 : Comparer quel cercle est plus grand (Dunder method) ---
    def __gt__(self, other):
        # __gt__ signifie "Greater Than" (>)
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius > other.radius