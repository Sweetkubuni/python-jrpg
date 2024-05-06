from .jprg import Person, Affinity
from .moves import Payoff
from functools import partial
# we use the Person DataClass from jrpg.py to create example NPCS and PCS


payOff = partial(Payoff, payment=10, demoralize=-2)

adam = Person("adam", Stats(10, 2, 1, 4, 20, 5, 20, Affinity.FINANCE), [payOff])

everyone = [
    adam
]
