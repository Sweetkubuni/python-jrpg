from .types import Decision, DecisionTreeNode


class HealCheck(Decision):
    def __init__(self, defaultOption):
        pass

class HealOthersCheck(Decision):
    def __init__(self, defaultOption):
        pass

class ChooseAttack(DecisionTreeNode):
    def __init__(self, defaultOption):
        pass
    def getBranch(self):
        """ perform the test """
    def testValue(self, us: Party):
        pass