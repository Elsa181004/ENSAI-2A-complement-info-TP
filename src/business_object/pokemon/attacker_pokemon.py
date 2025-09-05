from abstract_pokemon import AbstractPokemon

class AttackerPokemon(AbstractPokemon):
    def __init__(self):
        super().__init__(type_pk="Attacker")
       
    def get_pokemon_attack_coef(self) -> float:
        return(1 + (self.speed_current + self.attack_current) / 200)
