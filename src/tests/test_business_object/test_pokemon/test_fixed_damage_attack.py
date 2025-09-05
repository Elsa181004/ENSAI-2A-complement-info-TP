from business_object.pokemon.fixed_damage_attack import FixedDamageAttack

class TestFixedDamageAttack:
     def test_compute_damage(self):
        # GIVEN
        attack = FixedDamageAttack(power=10, "")


        # THEN
        assert attack.compute_damage() == 10
