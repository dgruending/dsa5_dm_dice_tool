class Character:

    MUT = 0
    KLUGHEIT = 1
    INTUITION = 2
    CHARISMA = 3
    FINGERFERTIGKEIT = 4
    GEWANDHEIT = 5
    KONSTITUTION = 6
    KOERPERKRAFT = 7
    INITIATIVE = 8

    def __init__(self):
        self._eigenschaften = {Character.MUT: 0, Character.KLUGHEIT: 0, Character.INTUITION: 0, Character.CHARISMA: 0,
                               Character.FINGERFERTIGKEIT: 0, Character.GEWANDHEIT: 0, Character.KONSTITUTION: 0,
                               Character.KOERPERKRAFT: 0, Character.INITIATIVE: 0}
        self.talente = list()

    def get_eigenschaft(self, eigenschaft):
        return self._eigenschaften.get(eigenschaft)

    def set_eigenschaft(self, eigenschaft, new_value):
        if new_value >= 0:
            self._eigenschaften[eigenschaft] = new_value
