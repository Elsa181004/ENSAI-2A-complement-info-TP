from business_object.pokemon.abstract_attack import AbstractAttack

class FixedDamageAttack(AbstractAttack):

    def compute_damage(self, pok_1, pok_2):
        return self._power 