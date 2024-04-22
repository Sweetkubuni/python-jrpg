from enum import Enum
from dataclasses import dataclass
from typing import List, Callable, Union
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
    finesse: int
    luck: int
    allegiance: int
    affinity: Affinity

@dataclass
class Item:
    name: str
    description: str
    quantity: int

class TargetType(Enum):
    Self=1
    Ally=2
    Enemy=3

class MoveType(Enum):
    Single=1
    Multi=2

@dataclass
class Move:
    targetType: TargetType
    moveType: MoveType
    multi: Union[Callable[BattleEventQueue, Person, List[Person]], None]
    single: Union[Callable[BattleEventQueue, Person, Person], None]

@dataclass
class Person:
    name: str
    stat: Stats
    moves: Move

@dataclass
class Party:
    people: List[Person]
    items: List[Item]
