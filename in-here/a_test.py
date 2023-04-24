"""make pylint happy"""
import pytest


@pytest.mark.skip(reason="something")
def test_a():
    """make pylint happy"""
    pass
