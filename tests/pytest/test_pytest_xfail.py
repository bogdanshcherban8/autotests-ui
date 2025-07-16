import pytest

@pytest.mark.xfail(reason="один не равно два")
def test_with_bug():
    assert 1==2
@pytest.mark.xfail(reason='баг исправлен')
def test_without_bug():
    ...