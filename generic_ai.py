from .jprg import Party

class DecisionTreeNode:
    @abstractmethod
    def makeDecision(self):
        """ returns DecisionTreeNode """

class Action(DecisionTreeNode):
    @abstractmethod
    def perform_action(self, name: str, targets: Party):
        pass
    def makeDecision(self):
        """ return new state of the world"""


class Decision(DecisionTreeNode):
    @abstractmethod
    def testValue(self, us: Party):
        """ perform the test """
    @abstractmethod
    def getBranch(self):
        """ perform the test """

    def makeDecision(self):
        branch = self.getBranch()
        return branch.makeDecision()
