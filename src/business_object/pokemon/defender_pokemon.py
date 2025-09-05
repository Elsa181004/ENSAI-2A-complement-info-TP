from abstract_pokemon import AbstractPokemon

class DefenderPokemon(AbstractPokemon):
    def __init__(self):
        super().__init__(type_pk="Defender")
       
    def get_pokemon_attack_coef(self) -> float:
        return(1 + (self.attack_current + self.defense_current) / 200)
