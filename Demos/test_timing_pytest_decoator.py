from timing_pytest import timing

@timing
def test_passing():
    assert 1==1

@timing
def test_failing():
    assert 1==2