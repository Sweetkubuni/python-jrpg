from enum import Enum
from dataclasses import dataclass
from typing import List, Callable
from .moves import BattleEventQueue

class Affinity(Enum):
    SPIRITUALITY=1
    FINANCE=2
    PERSAUSION=3

@dataclass
class Stats:
    moral: int
    attack: int
    reflex: int
    discernment: int
    healthPoints: int
    speed: int
    money: int
    affinity: Affinity

@dataclass
class Item:
    name: str
    description: str
    quantity: int

@dataclass
class Person:
    name: str
    stat: Stats
    moves: List[Callable[BattleEventQueue, Person, Person]]

@dataclass
class Party:
    people: List[Person]
    items: List[Item]
