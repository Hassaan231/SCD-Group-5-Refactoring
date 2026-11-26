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

    def speed(self):
        match self._type:
            case ParrotType.EUROPEAN:
                return self._base_speed()
            case ParrotType.AFRICAN:
                return max(0, self._base_speed() - self._load_factor() * self._number_of_coconuts)
            case ParrotType.NORWEGIAN_BLUE:
                return 0 if self._nailed else self._compute_base_speed_for_voltage(self._voltage)

    def cry(self):
        match self._type:
            case ParrotType.EUROPEAN:
                return "Sqoork!"
            case ParrotType.AFRICAN:
                return "Sqaark!"
            case ParrotType.NORWEGIAN_BLUE:
                return "Bzzzzzz" if self._voltage > 0 else "..."

        def _compute_base_speed_for_voltage(self, voltage):
        return min([MAX_SPEED, voltage * self._base_speed()])

    def _load_factor(self):
        return LOAD_FACTOR

    def _base_speed(self):
        return BASE_SPEED