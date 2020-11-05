import abc
from typing import Union


class ConnectionFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def requiresComPort(self) -> bool:
        return False

    @abc.abstractmethod
    def requiresBaudRate(self) -> bool:
        return False

    @abc.abstractmethod
    def construct(
        self,
        comPort: Union[int, str, None] = None,
        baudRate: Union[int, None] = None,
        rocket=None,
    ) -> None:
        pass