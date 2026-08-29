from eos_readiness.status import Status, worst_of


def test_worst_of_fail_beats_warning_and_pass():
    assert worst_of([Status.PASS, Status.WARNING, Status.FAIL]) == Status.FAIL


def test_worst_of_warning_beats_pass():
    assert worst_of([Status.PASS, Status.WARNING]) == Status.WARNING


def test_worst_of_all_pass():
    assert worst_of([Status.PASS, Status.PASS]) == Status.PASS


def test_worst_of_excludes_not_applicable():
    assert worst_of([Status.PASS, Status.NOT_APPLICABLE, Status.NOT_APPLICABLE]) == Status.PASS
    assert worst_of([Status.NOT_APPLICABLE, Status.FAIL]) == Status.FAIL


def test_worst_of_all_not_applicable_defaults_to_pass():
    assert worst_of([Status.NOT_APPLICABLE, Status.NOT_APPLICABLE]) == Status.PASS


def test_worst_of_empty_defaults_to_pass():
    assert worst_of([]) == Status.PASS
