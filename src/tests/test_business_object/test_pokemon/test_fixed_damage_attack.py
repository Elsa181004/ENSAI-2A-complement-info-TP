from business_object.pokemon.fixed_damage_attack import FixedDamageAttack
class TestFixedDamageAttack:
     def test_compute_damage(self):
        # GIVEN
        attack = FixedDamageAttack(power=10)

        # WHEN
        

        # THEN
        assert attack.compute_damage() == 10


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])