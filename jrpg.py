from enum import Enum
from dataclasses import dataclass
from typing import List, Callable

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
class Move:
    func: Callable[[str], List[str]]
    name: str
    description: str

@dataclass
class Person:
    stat: Stats
    name: str
    moves: List[Move]

@dataclass
class Party:
    people: List[Person]
    items: List[Item]
