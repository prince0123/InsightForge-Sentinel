from abc import ABC
from abc import abstractmethod


class BaseCalculator(ABC):

    @abstractmethod
    def calculate(
        self,
        *args,
        **kwargs
    ):
        raise NotImplementedError