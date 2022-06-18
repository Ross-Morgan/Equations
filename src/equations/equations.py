from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypeVar, overload

import solvers
from terms import (cubic_coefficients, linear_coefficients,
                   quadratic_coefficients, quartic_coefficients,
                   sign_cube_terms, sign_linear_terms, sign_quad_terms,
                   sign_quart_terms)

__all__ = [
    # constants
    "real",

    # classes
    "Cubic",
    "Quadratic",
    "Equation",
]

real = int | float
number = real | complex

T_co = TypeVar("T_co", "Linear", "Quadratic", "Cubic", "Quartic",
               covariant=True)


class Equation(ABC):
    """Abstract base class for equation sub-classes"""
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{str(self)}')"

    @abstractmethod
    def __str__(self) -> str: ...

    @abstractmethod
    def __eq__(self: T_co, other: T_co) -> bool: ...
    @abstractmethod
    def __add__(self: T_co, other: T_co) -> T_co: ...
    @abstractmethod
    def __sub__(self: T_co, other: T_co) -> T_co: ...
    @abstractmethod
    def __mul__(self: T_co, other: T_co) -> T_co: ...
    @abstractmethod
    def __div__(self: T_co, other: T_co) -> T_co: ...

    @abstractmethod
    def solve(self) -> number:
        """
        solve equation
        """


class Linear(Equation):
    """
    Linear equation in form `ax + b`
    where coefficients are real or complex
    ---
    - @param a: number - [coefficient for x¹]
    - @param b: number - [coefficient for x⁰]
    ---
    - @param equation: str - [equation in string form]
    """
    @overload
    def __init__(self, a: real, b: real, c: real) -> None: ...
    @overload
    def __init__(self, equation: str) -> None: ...

    def __init__(self, *args: real) -> None:
        if len(args) == 1:
            self._a, self._b = linear_coefficients(*args)
        else:
            self._a, self._b = args

    def __str__(self: T_co) -> str:
        a, b = sign_linear_terms(self.a, self.b)

        if a.startswith("+"):
            a = a[1:]

        return f"{a}{b}"

    def __eq__(self: T_co, other: T_co) -> bool:
        return [self.a, self.b] == [other.a, other.b]

    def __add__(self: T_co, other: T_co) -> T_co:
        return self.__class__(
            self.a + other.a,
            self.b + other.b,
        )

    def __sub__(self: T_co, other: T_co) -> T_co:
        return self.__class__(
            self.a - other.a,
            self.b - other.b,
        )

    def __mul__(self: T_co, other: real) -> T_co:
        return self.__class__(
            self.a * other,
            self.b * other,
        )

    def __div__(self: T_co, other: real) -> T_co:
        return self.__class__(
            self.a / other,
            self.b / other,
        )

    @property
    def a(self) -> T_co:
        return self._a

    @property
    def b(self) -> T_co:
        return self._b

    def solve(self: T_co) -> number:
        return solvers.solve(self.a, self.b)


class Quadratic(Equation):
    """
    Quadratic equation in form `ax² + bx + c`
    where all coefficients are real
    ---
    - @param a: real - [coeffient for x²]
    - @param b: real - [coeffient for x¹]
    - @param c: real - [coeffient for x⁰]
    ---
    - @param equation: str - [equation in string form]
    """
    @overload
    def __init__(self, a: real, b: real, c: real) -> None: ...
    @overload
    def __init__(self, equation: str) -> None: ...

    def __init__(self, *args: real) -> None:
        if len(args) == 1:
            self._a, self._b, self._c = quadratic_coefficients(*args)
        else:
            self._a, self._b, self._c = args

    def __str__(self):
        a, b, c = sign_quad_terms(self.a, self.b, self.c)

        if a.startswith("+"):
            a = a[1:]

        return f"{a}{b}{c}"

    def __eq__(self: T_co, other: T_co) -> bool:
        return [self.a, self.b, self.c] == [other.a, other.b, other.c]

    def __add__(self: T_co, other: T_co) -> T_co:
        return self.__class__(
            self.a + other.a,
            self.b + other.b,
            self.c + other.c
        )

    def __sub__(self: T_co, other: T_co) -> T_co:
        return self.__class__(
            self.a - other.a,
            self.b - other.b,
            self.c - other.c,
        )

    def __mul__(self: T_co, other: real) -> T_co:
        return self.__class__(
            self.a * other,
            self.b * other,
            self.c * other,
        )

    def __div__(self: T_co, other: real) -> T_co:
        return self.__class__(
            self.a / other,
            self.b / other,
            self.c / other,
        )

    @property
    def a(self) -> real:
        return self._a

    @property
    def b(self) -> real:
        return self._b

    @property
    def c(self) -> real:
        return self._c

    def solve(self) -> tuple[real, real]:
        return solvers.solve(self.a, self.b, as_list=True)


class Cubic(Equation):
    """
    Quadratic equation in form `ax³ + bx² + cx + d`
    where all coefficients are real
    ---
    - @param a: real - [coeffient for x³]
    - @param b: real - [coeffient for x²]
    - @param c: real - [coeffient for x¹]
    - @param d: real - [coeffient for x⁰]
    ---
    - @param equation: str - [equation in string form]
    """
    @overload
    def __init__(self, a: real, b: real, c: real, d: real) -> None: ...
    @overload
    def __init__(self, equation: str) -> None: ...

    def __init__(self, *args: real) -> None:
        if len(args) == 1:
            self._a, self._b, self._c, self._d = cubic_coefficients(*args)
        else:
            self._a, self._b, self._c, self._d = args
            self._a: real
            self._b: real
            self._c: real
            self._d: real

    def __str__(self) -> str:
        a, b, c, d = sign_cube_terms(self.a, self.b, self.c, self.d)

        if a.startswith("+"):
            a = a[1:]

        return f"{a}{b}{c}{d}"

    def __eq__(self: T_co, other: T_co) -> bool:
        return [self.a, self.b, self.c, self.d] == [other.a, other.b, other.c, self.d]  # noqa

    def __add__(self: T_co, other: T_co) -> T_co:
        return self.__class__(
            self.a + other.a,
            self.b + other.b,
            self.c + other.c,
            self.d + other.d,
        )

    def __sub__(self: T_co, other: T_co) -> T_co:
        return self.__class__(
            self.a - other.a,
            self.b - other.b,
            self.c - other.c,
            self.d - other.d,
        )

    def __mul__(self: T_co, other: real) -> T_co:
        return self.__class__(
            self.a * other,
            self.b * other,
            self.c * other,
            self.d * other,
        )

    def __div__(self: T_co, other: real) -> T_co:
        return self.__class__(
            self.a / other,
            self.b / other,
            self.c / other,
            self.d / other,
        )

    @property
    def a(self) -> real:
        return self._a

    @property
    def b(self) -> real:
        return self._b

    @property
    def c(self) -> real:
        return self._c

    @property
    def d(self) -> real:
        return self._d

    def solve(self):
        return solvers.solve(self.a, self.b, self.c, as_list=True)


class Quartic(Equation):
    """
    Quadratic equation in form `ax⁴ + bx³ + cx² + dx + e`
    where all coefficients are real
    ---
    - @param a: real - [coeffient for x⁴]
    - @param b: real - [coeffient for x³]
    - @param c: real - [coeffient for x²]
    - @param d: real - [coeffient for x¹]
    - @param e: real - [coeffient for x⁰]
    ---
    - @param equation: str - [equation in string form]
    """
    @overload
    def __init__(self,
                 a: real, b: real, c: real, d: real, e: real) -> None: ...

    @overload
    def __init__(self, equation: str) -> None: ...

    def __init__(self, *args: real) -> None:
        if len(args) == 1:
            (self._a, self._b,
             self._c, self._d, self._e) = quartic_coefficients(*args)
        else:
            self._a, self._b, self._c, self._d, self._e = args
            self._a: real
            self._b: real
            self._c: real
            self._d: real
            self._e: real

    def __str__(self) -> str:
        a, b, c, d, e = sign_quart_terms(
            self.a, self.b, self.c, self.d, self.e
        )

        if a.startswith("+"):
            a = a[1:]

        return f"{a}{b}{c}{d}{e}"

    def __eq__(self: T_co, other: T_co) -> bool:
        return [self.a, self.b, self.c, self.d, self.e] == [other.a, other.b, other.c, self.d, self.e]  # noqa

    def __add__(self: T_co, other: T_co) -> T_co:
        return self.__class__(
            self.a + other.a,
            self.b + other.b,
            self.c + other.c,
            self.d + other.d,
            self.e + other.e,
        )

    def __sub__(self: T_co, other: T_co) -> T_co:
        return self.__class__(
            self.a - other.a,
            self.b - other.b,
            self.c - other.c,
            self.d - other.d,
            self.e - other.e,
        )

    def __mul__(self: T_co, other: real) -> T_co:
        return self.__class__(
            self.a * other,
            self.b * other,
            self.c * other,
            self.d * other,
            self.e * other,
        )

    def __div__(self: T_co, other: real) -> T_co:
        return self.__class__(
            self.a / other,
            self.b / other,
            self.c / other,
            self.d / other,
            self.e / other,
        )

    @property
    def a(self) -> real:
        return self._a

    @property
    def b(self) -> real:
        return self._b

    @property
    def c(self) -> real:
        return self._c

    @property
    def d(self) -> real:
        return self._d

    @property
    def e(self) -> real:
        return self._e

    def solve(self):
        return solvers.solve(self.a, self.b, self.c, self.d, self.e,
                             as_list=True)
