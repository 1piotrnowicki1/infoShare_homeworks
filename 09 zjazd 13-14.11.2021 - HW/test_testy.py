import pytest

from solution import trojkat


def test_trojkat_egipski():
    expected = 5
    result = trojkat(5, 4)
    assert expected == result


def test_trojkat__blad():
    with pytest.raises(TypeError):
        trojkat(3, 'tu_jest_string!')