from abc import ABC
from abc import abstractmethod


class BaseRenderer(ABC):

    @abstractmethod
    def render(
        self,
        model
    ):
        raise NotImplementedError