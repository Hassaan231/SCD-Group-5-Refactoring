from abc import ABC, abstractmethod
from enum import Enum


class ParrotType(Enum):
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3


BASE_SPEED = 12.0
LOAD_FACTOR = 9.0
MAX_SPEED = 24.0


class Parrot(ABC):

    def __init__(self, number_of_coconuts, voltage, nailed):
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed

    @abstractmethod
    def speed(self):
        ...

    @abstractmethod
    def cry(self):
        ...


class EuropeanParrot(Parrot):
    def speed(self):
        return BASE_SPEED

    def cry(self):
        return "Sqoork!"


class AfricanParrot(Parrot):
    def speed(self):
        return max(0, BASE_SPEED - LOAD_FACTOR * self._number_of_coconuts)

    def cry(self):
        return "Sqaark!"


class NorwegianBlueParrot(Parrot):
    def speed(self):
        if self._nailed:
            return 0
        return min(MAX_SPEED, self._voltage * BASE_SPEED)

    def cry(self):
        return "Bzzzzzz" if self._voltage > 0 else "..."


def create_parrot(parrot_type, number_of_coconuts=0, voltage=0.0, nailed=False):
    match parrot_type:
        case ParrotType.EUROPEAN:
            return EuropeanParrot(number_of_coconuts, voltage, nailed)
        case ParrotType.AFRICAN:
            return AfricanParrot(number_of_coconuts, voltage, nailed)
        case ParrotType.NORWEGIAN_BLUE:
            return NorwegianBlueParrot(number_of_coconuts, voltage, nailed)
        case _:
            raise ValueError(f"Unknown parrot type: {parrot_type}")