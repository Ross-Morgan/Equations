from typing import TypeVar

from . import Cubic, Quadratic

__all__ = [
    "test_operations",
    "test_properties",
]

T = TypeVar("T")


def assert_equal(a: T, b: T, desc: str = "No description"):
    assert (a == b), desc
    print(f"Test Passed: {a} == {b}")


def add(equation_1: Quadratic, equation_2: Quadratic) -> Quadratic:
    return equation_1 + equation_2


def sub(equation_1: Quadratic, equation_2: Quadratic) -> Quadratic:
    return equation_1 - equation_2


def test_operations():
    equation_1 = Quadratic(4, 12, 40)
    equation_2 = Quadratic(2, 6,  10)

    assert_equal(str(equation_1), "4x²+12x+40")
    assert_equal(str(equation_2), "2x²+6x+10")

    added = add(equation_1, equation_2)
    subbed = sub(equation_1, equation_2)

    assert_equal(added, Quadratic(6, 18, 50))
    assert_equal(subbed, Quadratic(2, 6, 30))

    assert_equal(str(added), "6x²+18x+50")
    assert_equal(str(subbed), "2x²+6x+30")


def test_properties():
    quad_equation_1 = Quadratic(4, 12, 40)
    quad_equation_2 = Quadratic(2, 6,  10)

    assert_equal(quad_equation_1.a, 4)
    assert_equal(quad_equation_1.b, 12)
    assert_equal(quad_equation_1.c, 40)

    assert_equal(quad_equation_2.a, 2)
    assert_equal(quad_equation_2.b, 6)
    assert_equal(quad_equation_2.c, 10)

    cube_equation_1 = Cubic(1, -7, 4, 12)
    cube_equation_2 = Cubic(2, 3, -11, -6)

    assert_equal(cube_equation_1.a, 1)
    assert_equal(cube_equation_1.b, -7)
    assert_equal(cube_equation_1.c, 4)
    assert_equal(cube_equation_1.d, 12)

    assert_equal(cube_equation_2.a, 2)
    assert_equal(cube_equation_2.b, 3)
    assert_equal(cube_equation_2.c, -11)
    assert_equal(cube_equation_2.d, -6)


def run_all_tests():
    test_operations()
    test_properties()


if __name__ == "__main__":
    test_operations()
