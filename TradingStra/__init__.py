from abc import ABC, abstractmethod
from backtesting import Strategy

class Context():

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

class Strategy(ABC):
    @abstractmethod
    def trade(self):
        pass