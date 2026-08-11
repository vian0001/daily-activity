from scripts.metrics_collector import collect

def test_metrics():
    assert collect()['status'] == 'active'
