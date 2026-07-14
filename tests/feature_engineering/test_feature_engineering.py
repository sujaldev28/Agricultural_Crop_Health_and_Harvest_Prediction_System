"""
Tests for agricultural feature calculators.
"""
import pytest
from src.feature_engineering.gdd import GDDCalculator
from src.feature_engineering.dli import DLICalculator

def test_gdd_calculation() -> None:
    gdd = GDDCalculator()
    val = gdd.calculate(max_temp=28.0, min_temp=12.0, base_temp=10.0)
    assert val == 10.0

def test_dli_calculation() -> None:
    dli = DLICalculator()
    val = dli.calculate(avg_lux=5000.0, photoperiod_hours=14.0)
    assert val > 0
