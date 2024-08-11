import math

from loguru import logger


class QuadraticEquationError(Exception): ...


def solve(a: float, b: float, c: float, abs_tolerance: float = 1.0e-07) -> list[float]:
    logger.debug(f"Solving for coefficients: a={a}, b={b}, c={c}")

    for value, name in [(a, "A"), (b, "B"), (c, "C")]:
        if math.isnan(value):
            raise QuadraticEquationError(f"Coefficient {name} is NaN")
        if math.isinf(value):
            raise QuadraticEquationError(f"Coefficient {name} is infinity")

    if math.isclose(a, 0, abs_tol=abs_tolerance):
        raise QuadraticEquationError("Coefficient  A is (close to) zero")

    d = pow(b, 2) - 4 * a * c

    logger.debug(f"D = {d}")

    if math.isclose(d, 0, abs_tol=abs_tolerance):
        return [-b / (2 * a)]

    if d < 0:
        return []

    return [(-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a)]
