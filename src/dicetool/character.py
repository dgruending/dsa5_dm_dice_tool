class Character:

    # Dictionary keys as constants
    MUT = "MU"
    KLUGHEIT = "KL"
    INTUITION = "IN"
    CHARISMA = "CH"
    FINGERFERTIGKEIT = "FF"
    GEWANDHEIT = "GE"
    KONSTITUTION = "KO"
    KOERPERKRAFT = "KK"
    INITIATIVE = "INI"

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
