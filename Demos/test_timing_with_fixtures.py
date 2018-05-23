from timing_with_fixtures import timing


def test_passing(timing):
    # testname = request.node.name
    # assert testname == 'test_name1'
    assert 1==1


def test_failing(timing):
    assert 1==2