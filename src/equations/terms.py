import re

__all__ = [
    "sign_x3",
    "sign_x2",
    "sign_x",
    "sign_n",

    "sign_quad_terms",
    "sign_cube_terms",
]

number = int | float

linear_root = tuple[number]
quad_roots =  tuple[number, number]                                   # noqa
cube_roots =  tuple[number, number, number]                           # noqa
quart_roots = tuple[number, number, number, number]
quint_roots = tuple[number, number, number, number, number]

linear_terms = tuple[number, number]
quad_terms =   tuple[number, number, number]                          # noqa
cube_terms =   tuple[number, number, number, number]                  # noqa
quart_terms =  tuple[number, number, number, number, number]          # noqa
quint_terms =  tuple[number, number, number, number, number, number]  # noqa


patterns: dict[str, dict[str, re.Pattern] | re.Pattern] = {
    "coeff": re.compile(r"[+-]?\d*"),
    "Linear": {
        "equation": re.compile(),
        "terms": re.compile()
    },
    "Quadratic": {
        "equation": re.compile(r"(-?\d*)x(²)([+-]\d+)x([+-]\d+)"),
        "terms": re.compile(r"([+-]?\d*(x?)(²?))"),
    },
    "Cubic": {
        "equation": re.compile(r"(-?\d*)x³([+-]?\d*)x²([+-]\d+)x([+-]\d+)"),
        "terms": re.compile(r"([+-]?\d*(x?)([²³]?))"),
    },
    "Quartic": {
        "equation": re.compile("(-?\d*)x⁴([+-]?\d*)x³([+-]?\d*)x²([+-]\d+)x([+-]\d+)"), # noqa
        "terms": re.compile(r"([+-]?\d*(x?)([²³⁴]?))"),
    }
}


def numify(num: str) -> number:
    if num == "-":
        return -1
    if num == "":
        return 1

    if float(num) % 1 == 0:
        f = int
    else:
        f = float

    return f(num)


def sign_x3(c: number) -> str:
    """
    @param c: number [Coefficient signed for x²]
    """
    if c not in [0, 1] and c > 0:
        c = f"{c}x³"
    elif c == 1:
        c = "x³"
    elif c == 0:
        c = ""
    elif c not in [0, -1] and c < 0:
        c = f"-{c}x³"
    elif c == -1:
        c = "-x³"

    return c


def sign_x2(c) -> str:
    """
    @param c: number [Coefficient signed for x²]
    """
    return sign_x3(c).replace("³", "²")


def sign_x(c) -> str:
    """
    @param c: number [Coefficient signed for x]
    """
    return sign_x3(c).replace("³", "")


def sign_n(c) -> str:
    """
    @param c: number [Coefficient signed for n]
    """
    if c >= 0:
        return f"+{c}"
    else:
        return f"-{c}"


def sign_linear_terms(a: number, b: number) -> linear_terms:
    """
    Add positive/negative signs to terms and/or remove appropriately

    ---
    - @param a: number [ax term]
    - @param b: number [b term]
    """
    a = sign_x(a)
    b = sign_n(b)

    return a, b


def sign_quad_terms(a: number, b: number, c: number) -> quad_terms:
    """
    Add positive/negative signs to terms and/or remove appropriately

    ---

    - @param a: number [ax² term]
    - @param b: number [bx term]
    - @param c: number [c term]
    """
    a = sign_x2(a)
    b = sign_x(b)
    c = sign_n(c)

    return a, b, c


def sign_cube_terms(a: number, b: number, c: number, d: number) -> cube_terms:
    """
    Add positive/negative signs to terms and/or remove appropriately

    ---

    - @param a: number [ax³ term]
    - @param b: number [bx² term]
    - @param c: number [cx term]
    - @param d: number [d term]
    """
    a = sign_x3(a)
    b = sign_x2(b)
    c = sign_x(c)
    d = sign_n(d)


def linear_coefficients(equation: str) -> linear_terms:
    """
    Return coefficients from linear equation
    ---
    - @param equation: str - [linear equation in form ax + b]
    """


def quadratic_coefficients(equation: str) -> quad_terms:
    """
    Return coefficients from cubic equation
    ---
    - @param equation: str - [quadratic equation in form ax² + bx + c]
    """
    # Remove all whitespace for regularity
    equation.replace(" ", "")

    # Find terms
    a, b, c, *d = patterns["Quadratic"]["terms"].findall(equation)

    a = a[0]
    b = b[0]
    c = c[0]

    # Extract coefficients
    a = numify(patterns["coeff"].findall(a)[0])
    b = numify(patterns["coeff"].findall(b)[0])
    c = numify(patterns["coeff"].findall(c)[0])

    return a, b, c


def cubic_coefficients(equation: str) -> cube_terms:
    """
    Return coefficients from cubic equation
    ---
    - @param equation: str [cubic equation in form ax³ + bx² + cx + d]
    """
    # Remove all whitespace for regularity
    equation.replace(" ", "")

    # Find terms
    a, b, c, d, *e = patterns["Cubic"]["terms"].findall(equation)

    # Get first from each group
    a = a[0]
    b = b[0]
    c = c[0]
    d = d[0]

    # Extract coefficients
    a = numify(patterns["coeff"].findall(a)[0])
    b = numify(patterns["coeff"].findall(b)[0])
    c = numify(patterns["coeff"].findall(c)[0])
    d = numify(patterns["coeff"].findall(d)[0])

    return a, b, c, d


def quartic_coefficients(equation: str) -> quart_terms:
    """
    Return coefficients from cubic equation
    ---
    - @param equation: str [cubic equation in form ax³ + bx² + cx + d]
    """
    # Remove all whitespace for regularity
    equation.replace(" ", "")

    # Find terms
    a, b, c, d, e, *f = patterns["Quartic"]["terms"].findall(equation)

    # Get first from each group
    a = a[0]
    b = b[0]
    c = c[0]
    d = d[0]
    e = e[0]

    # Extract coefficients
    a = numify(patterns["coeff"].findall(a)[0])
    b = numify(patterns["coeff"].findall(b)[0])
    c = numify(patterns["coeff"].findall(c)[0])
    d = numify(patterns["coeff"].findall(d)[0])
    e = numify(patterns["coeff"].findall(e)[0])

    return a, b, c, d, e
