import itertools
import math
import sys

import pytest

from app.quadratic_equation import QuadraticEquationError, solve


def assert_roots(calculated: list[float], expected: list[float]) -> None:
    for calculated_root, expected_root in zip(sorted(calculated), sorted(expected), strict=True):
        assert math.isclose(calculated_root, expected_root, abs_tol=1.0e-07)


# 3) Для уравнения x^2+1 = 0 корней нет (возвращается пустой массив)
def test_no_roots() -> None:
    assert solve(1.0, 0.0, 1.0) == []


# 5) Для уравнения x^2-1 = 0 есть два корня кратности 1 (x1=1, x2=-1)
def test_2_roots() -> None:
    assert_roots(solve(1.0, 0.0, -1.0), [-1.0, 1.0])


# 7) Для уравнения x^2+2x+1 = 0 есть один корень кратности 2 (x1= x2 = -1).
def test_1_root() -> None:
    assert_roots(solve(1.0, 2.0, 1.0), [-1.0])


# 11) Дискриминант отличный от нуля, но меньше заданного эпсилон
def test_1_root_tolerance() -> None:
    assert_roots(solve(1.0, 0.2, 0.01), [-0.1])


# 9) Коэффициент a не может быть равен 0
def test_negative_a() -> None:
    with pytest.raises(QuadraticEquationError):
        solve(0.0, 2.0, 1.0)

    with pytest.raises(QuadraticEquationError):
        solve(0.0 + sys.float_info.epsilon, 2.0, 1.0)


# 13) solve не может принимать значения, отличные от чиcел
def test_non_numbers() -> None:
    values = [1.0, math.nan, math.inf, -math.inf]

    for coeficients in itertools.product(values, repeat=3):
        if set(coeficients) == {1.0}:
            continue
        with pytest.raises(QuadraticEquationError):
            solve(*coeficients)
