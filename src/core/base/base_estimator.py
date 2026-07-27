from abc import ABC
from abc import abstractmethod


class BaseEstimator(ABC):

    @abstractmethod
    def estimate(
        self,
        *args,
        **kwargs
    ):
        raise NotImplementedError