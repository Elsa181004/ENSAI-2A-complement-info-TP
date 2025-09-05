from abc import ABC, abstractmethod
from business_object.pokemon.abstract_pokemon import AbstractPokemon

class AbstractAttack(ABC):
    def __init__(self, power, name, description):
        self._power = power
        self._name = name
        self._description = description

    @abstractmethod
    def compute_damage(self, pok_1:AbstractPokemon , pok_2:AbstractPokemon) -> int:
        pass

