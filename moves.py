import queue
from .jprg import Affinity, Party, Person
from typing import List
import random
import functools

class BattleEventQueue:
    def __init__(self):
        self.events = queue.SimpleQueue()
    def signal_stats_change(self, target:Person, stats: str, modifiers: int):
        """ updates simple queue """
        self.events.put(("stat", targets, stats, modifiers))
    def signal_item_event(self, source : Person, item):
        """ updates simple queue """
        self.events.put(("item", source))
    def signal_status_effect_event(self, target: Person,  ailment: str):
        """ updates simple queue """
        self.events.put(("status", target, ailment))
    def signal_miss_event(self, target:Person):
        self.events.put(("miss", target))

def process_stat_changes(event, everyone: Party):
    pass

def process_event_queue(battleEvents: BattleEventQueue, everyone: Party):
    while not battleEvents.events.empty():
        event = battleEvents.events.get()
        if event[0] == "stat":
            for person in party.people:
                if person.name in event[1]:
                    status_attrib = event[2]
                    mod = event[3]
                    if status_attrib == "moral":
                        person.stat.moral += mod
                    elif status_attrib == "attack":
                        person.stat.attack += mod;
                    elif status_attrib == "reflex":
                        person.stat.reflex += mod;
                    elif status_attrib == "discernment":
                        person.stat.discernment += mod;
                    elif status_attrib == "healthPoints":
                        person.stat.healthPoints += mod;
                    elif status_attrib == "speed":
                        person.stat.speed += mod;
                    elif status_attrib == "money":
                        person.stat.money += mod;
                    else:
                        print(f"unknown stats {status_attrib}")
        elif event[0] == "item":
            for item in party.items:
                if item.name == event[1]:
                    item.quantity -= 1
        else:
            print(f"unknown event {event[0]}")

def checkIfSpiritualAttackHits(func, affinityMod, maxDifficulty):
    @functools.wrap(func)
    def wrapper_timer(*args, **kwargs):
        event = args[0]
        person = args[1]
        target = args[2]
        difficulty=random.randint(target.stat.reflex,  maxDifficulty)
        if person.stat.affinity == Affinity.SPIRITUALITY:
            hit = person.stat.attack * affinityMod
        else:
            hit = person.stat.attacks
        if hit > difficulty:
            func(*args, **kwargs)
        else:
            event.signal_miss_event(target)
    return wrapper_timer

def checkIfPersuasiveAttackHits(func, affinityMod, maxDifficulty):
    @functools.wrap(func)
    def wrapper_timer(*args, **kwargs):
        event = args[0]
        person = args[1]
        target = args[2]
        difficulty=random.randint(target.stat.discernment,  maxDifficulty)
        if person.stat.affinity == Affinity.PERSAUSION:
            hit = person.stat.attack * affinityMod
        else:
            hit = person.stat.attacks
        if hit > difficulty:
            func(*args, **kwargs)
        else:
            event.signal_miss_event(target)
    return wrapper_timer

def checkIfFinancialAttackHits(func):
    @functools.wrap(func)
    def wrapper_timer(*args, **kwargs):
        event = args[0]
        person = args[1]
        target = args[2]
        if person.stat.money > target.stat.money:
            func(*args, **kwargs)
        else:
            event.signal_miss_event(target)
    return wrapper_timer


@checkIfFinancialAttackHits
def Payoff(event: BattleEventQueue, caster: Person, enemy: Person, payment: int, demoralize: int):
    """ you pay off person to lower their moral and prevent an attack """
    event.signal_stats_change(caster, "money", payment)
    event.signal_stats_change(enemy, "moral", demoralize)

def MassPayoff(event: BattleEventQueue, caster: Person, enemies: List[Person], payment: int, demoralize: int):
    for enemy in enemies:
        Payoff(event, caster, enemy, payment, demoralize)

#TODO: create status effect enum instead of string
def BamBoozle(event: BattleEventQueue, person: Person, target: Person):
    """ confuse enemy and waste their turn """
    event.signal_status_effect_event(target, "confusion")
    pass

def PreachFinancialFreedom(event: BattleEventQueue, person: Person, allies: List[Person], loss, gain):
    """ increase ally's moral but pay with money """
    if person.stat.money >= loss * len(allies):
        event.signal_stats_change(person, "money", loss)
        for ally in allies:
            event.signal_stats_change(ally, "moral", gain)
    else:
        event.signal_miss_event(person)

checkIfSpiritualAttackHits(affinityMod=1.5, maxDifficulty=20)
def DispelEvil(event, person, target, loss):
    """ does light damage, contact hit is based on atk and affinity"""
    event.signal_stats_change(target, "healthPoints", loss)


def EchoingEndorsement (event, person: Person, allies: List[Person], gain):
    """ increase attack stat for all ally party members"""

#multi target moves
def MassDispelEvil(event, person, targets):
    """ does same number of damage to all targets, but they all need to be within low discernment
    in total """
    pass

def WereAFamily(event, people):
    """ Increases protagonist def and moral in sacrifice of party members stats"""
    pass

def PromiseLove(event, person, target):
    """ heals a small portion of enemy and allies, but increases their alignness (moral) to you"""
    pass

def PromiseWeath(event, person, target):
    """ increase a small portion of everyones wealth, but their aligness (moral) to you """
    pass
def PromisePeace(event, person, target):
    """pacificy everyone for a turn"""
def PromiseFairness(event, person, target):
    """"""

def SectarianSurge():
    """Channels the fervor of a devoted following into a powerful energy blast, 
    dealing damage based on the number of allies in the party."""
    pass

def PolicyParalyze():
    """Inflicts paralysis on enemies by overwhelming them with conflicting ideologies and policies, 
    rendering them unable to act."""
    pass

def PyramidPummel():
    pass

def InfluenceIncantation():
    pass

def KarmaCascade():
    pass

def AuraOfAbundance():
    pass

def TranscendentTornado():
    pass

def MeditativeMirage():
    pass

def ApocalypticAnnihilation():
    pass

def ConformityCrush():
    pass

def PowerPlay():
    pass


def useItem(event, itemName, caster, targets, func):
    """ signal the item the caster used """
    event.signal_item_event(caster, itemName)
    func(event, caster, targets)

@useItem
def usePotion(event, caster, targets, healthPoints=10):
    event.signal_stats_change([caster], "healthPoints", healthPoints)