import pytest
from parrot import create_parrot, ParrotType


def build(type_, coconuts=0, voltage=0.0, nailed=False):
    return create_parrot(type_, coconuts, voltage, nailed)


# ---------- speed ----------
def test_european_speed():
    assert build(ParrotType.EUROPEAN).speed() == 12.0


@pytest.mark.parametrize("coconuts, expected", [(0, 12.0), (1, 3.0), (2, 0), (5, 0)])
def test_african_speed(coconuts, expected):
    assert build(ParrotType.AFRICAN, coconuts=coconuts).speed() == expected


@pytest.mark.parametrize("voltage, expected", [(0, 0), (1.5, 18.0), (2, 24.0), (4, 24.0)])
def test_norwegian_blue_speed(voltage, expected):
    assert build(ParrotType.NORWEGIAN_BLUE, voltage=voltage).speed() == expected


def test_nailed_norwegian_blue_speed_is_zero():
    assert build(ParrotType.NORWEGIAN_BLUE, voltage=4, nailed=True).speed() == 0


# ---------- cry ----------
def test_european_cry():
    assert build(ParrotType.EUROPEAN).cry() == "Sqoork!"


def test_african_cry():
    assert build(ParrotType.AFRICAN).cry() == "Sqaark!"


def test_norwegian_blue_cry_with_voltage():
    assert build(ParrotType.NORWEGIAN_BLUE, voltage=4).cry() == "Bzzzzzz"


def test_norwegian_blue_cry_without_voltage():
    assert build(ParrotType.NORWEGIAN_BLUE, voltage=0).cry() == "..."