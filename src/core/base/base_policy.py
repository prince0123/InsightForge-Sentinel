from abc import ABC
from abc import abstractmethod


class BasePolicy(ABC):

    @abstractmethod
    def apply(
        self,
        *args,
        **kwargs
    ):
        raise NotImplementedError