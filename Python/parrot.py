from enum import Enum


class ParrotType(Enum):
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3


BASE_SPEED = 12.0
LOAD_FACTOR = 9.0
MAX_SPEED = 24.0


class Parrot:

    def __init__(self, parrot_type, number_of_coconuts, voltage, nailed):
        self._type = parrot_type
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed

    def _speed_for_voltage(self, voltage):
        return min(MAX_SPEED, voltage * self._base_speed())

    def _load_factor(self):
        return LOAD_FACTOR

    def _base_speed(self):
        return BASE_SPEED


class EuropeanParrot(Parrot):
    def speed(self):
        return self._base_speed()

    def cry(self):
        return "Sqoork!"


class AfricanParrot(Parrot):
    def speed(self):
        return max(0, self._base_speed() - self._load_factor() * self._number_of_coconuts)

    def cry(self):
        return "Sqaark!"


class NorwegianBlueParrot(Parrot):
    def speed(self):
        return 0 if self._nailed else self._speed_for_voltage(self._voltage)

    def cry(self):
        return "Bzzzzzz" if self._voltage > 0 else "..."


def create_parrot(parrot_type, number_of_coconuts=0, voltage=0.0, nailed=False):
    match parrot_type:
        case ParrotType.EUROPEAN:
            return EuropeanParrot(parrot_type, number_of_coconuts, voltage, nailed)
        case ParrotType.AFRICAN:
            return AfricanParrot(parrot_type, number_of_coconuts, voltage, nailed)
        case ParrotType.NORWEGIAN_BLUE:
            return NorwegianBlueParrot(parrot_type, number_of_coconuts, voltage, nailed)
        case _:
            raise ValueError(f"Unknown parrot type: {parrot_type}")