import queue
from .jprg import Party, Person, Alignment


class BattleEventQueue:
    def __init__(self):
        self.events = queue.SimpleQueue()
    def signal_stats_change(self, target:Person, stats: str, modifiers: int):
        """ add status change to queue """
        self.events.put(("stat", targets, stats, modifiers))

    def signal_item_event(self, source : Party, item : Item):
        """ add item change to queue """
        self.events.put(("item", source))

    def signal_status_effect_event(self, target: Person,  ailment: Alignment):
        """ updates simple queue """
        self.events.put(("ailment", target, ailment))

    def signal_miss_event(self, target:Person):
        self.events.put(("miss", target))


# we need to seperate out process event functions to handle specific events
# we need one overall process_event_queue that takes as params
#battleEvents, enemies: Party, allies: Party
def process_stat_event(event):
    person = event[1]
    status_attrib = event[2]
    mod = event[3]
    print(f"{person.name}  {status_attrib}  {mod}")
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


def process_miss_event(event):
    person = event[1]
    print(f"miss {person.name}")


def process_ailment_event(event):
    person = event[1]
    person.ailment = event[2]
    ailment = ["anxiety", "depression", "mania", "addict"]
    print(f" {person.name} has gain ailment: {ailment[person.ailment - 1]}")


def process_item_event(event):
    for item in party.items:
        if item.name == event[1]:
            item.quantity -= 1


def process_event_queue(battleEvents: BattleEventQueue):
    while not battleEvents.events.empty():
        event = battleEvents.events.get()
        if event[0] == "stat":
            process_stat_event(event)
        elif event[0] == "item":
             process_item_event(event)
        elif event[0] == "miss":
            process_miss_event(event)
        elif event[0] == "ailment":
            process_ailment_event(event)
        else:
            print(f"unknown event {event[0]}")