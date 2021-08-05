import pytest
from src.television_program import TelevisionProgram

def test_exercise():
    doctor_who = TelevisionProgram("Doctor Who",1)

    assert doctor_who.get_name() == "Doctor Who"
    assert doctor_who.get_duration() == 1
