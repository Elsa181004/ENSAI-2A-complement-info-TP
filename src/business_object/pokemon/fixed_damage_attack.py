from business_object.pokemon.abstract_attack import AbstractAttack

class FixedDamageAttack(AbstractAttack):
    def __init__(self):
        super().__init__()

    def compute_damage(self, pok_1, pok_2):
        return self._power 