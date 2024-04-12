import queue
from .jprg import Party, Affinity
from typing import List
import random

class BattleEventQueue:
    def __init__(self):
        self.events = queue.SimpleQueue()
    def signal_stats_change(self, targets: List[str], stats: str, modifiers: int):
        """ updates simple queue """
        self.events.put(("stat", targets, stats, modifiers))
    def signal_item_event(self, source : str, item):
        """ updates simple queue """
        self.events.put(("item", source))

def process_event_queue(battleEvents: BattleEventQueue, party: Party):
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


def Payoff(event: BattleEventQueue, person: str, target: str, payment: int, demoralize: int):
    """ you pay off person to lower their moral and prevent an attack """
    event.signal_stats_change([person], "money", -1 * payment)
    event.signal_stats_change([target], "moral", demoralize)

def MassPayoff(event: BattleEventQueue, person: str, targets: List[str], payment: int, demoralize: int):
    """ you pay off person to lower their moral and prevent an attack """
    event.signal_stats_change([person], "money", -1 * payment)
    event.signal_stats_change(targets, "moral", demoralize)

def BamBoozle(event: BattleEventQueue, person, target):
    """ confuse enemy and waste their turn """
    pass

def PreachFinancialFreedom(event: BattleEventQueue, person: Person, target: Person):
    """ lowers enemy moral and atk by amount of money you have """
    pass

def DispelEvil(event, person, target):
    """ does light damage, contact hit is based on atk and affinity"""
    landsHit=random.randint(10, target.stat.reflex * 10)
    hit = 0
    if person.stat.affinity == Affinity.SPIRITUALITY:
        hit = person.stat.attack * 2
    else:
        hit = person.stat.attacks
    pass


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

def useItem(event, person):
    pass

