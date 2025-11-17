# import pytest
from eco.core import EcoPlugin

def test_echo_returns_message():
    plugin = EcoPlugin("hola")
    assert plugin.echo() == "hola"

def test_shout_returns_uppercase():
    plugin = EcoPlugin("hola")
    assert plugin.shout() == "HOLA"