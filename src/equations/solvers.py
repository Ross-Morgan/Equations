import numpy as np

import fqs

__all__ = [
    "number",
    "real",
    "solve",
    "solve_linear",
]

number = int | float | complex
real = int | float


def _assert_real(*args: number) -> None:
    assert all(isinstance(x, real) for x in args), "All Arguments must be real"


def solve_linear(a0: list[real]):
    return (-a0[1]) / a0[0]


def solve(a: real, b: real, c: real = 0, d: real = 0, e: real = 0,
          *, as_list: bool = False) -> number:
    """
    Solves equation for ≥ 2 real coefficients passed
    where `a = b ≠ 0`
    ---
    - @param a: number - [coefficient for x ≤ ⁴]
    - @param b: number - [coefficient for x ≤ ³]
    - @param c: number - [coefficient for x ≤ ²]
    - @param d: number - [coefficient for x ≤ ¹]
    - @param e: number - [coefficient for x ≤ ⁰]
    """

    list_type = np.array

    if as_list:
        list_type = list

    _assert_real(a, b, c, d, e)

    if e != 0:
        roots = fqs.quartic_roots([a, b, c, d, e])
    elif d != 0:
        roots = fqs.cubic_roots([a, b, c, d])
    elif c != 0:
        roots = fqs.single_quadratic([a, b, c])
    elif b != 0:
        roots = [solve_linear([a, b])]
    else:
        roots = [a]  # should never run
    return list_type(roots)
