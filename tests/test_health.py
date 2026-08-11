from scripts.health_check import check

def test_health():
    assert check() is True
