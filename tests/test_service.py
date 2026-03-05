import pytest
from app.service import calculate_total, process_payment

def test_calculate_total_ok():
    assert calculate_total("coffee", 2) == 360

def test_calculate_total_zero():
    assert calculate_total("tea", 0) == 0

def test_invalid_product():
    with pytest.raises(KeyError):
        calculate_total("cofee", 0)

def test_calculate_total_minus_one():
    with pytest.raises(ValueError):
        calculate_total("coffee", -1)

def test_process_payment():
    assert not process_payment(-100)