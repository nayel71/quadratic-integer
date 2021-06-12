"""Symbolic integer arithmetic in quadratic integer rings"""

class QuadraticIntegerRing:
    """Base class for symbolic integer arithmetic in \mathbb Z[x],
    where x^2 - P*x + Q = 0
    """

    def __init__(self, P, Q, sym="x"):
        """Return a symbolic representation of \mathbb Z[x]."""
        for _ in (P, Q):
            if not isinstance(_, int):
                raise ValueError(f"{_} (coefficients must be integers)")
        # require P to be odd for the discriminant to be square-free
        if P & 1 == 0:
            raise ValueError(f"{P} (P must be odd)")
        self._P = P  # negative linear coefficient
        self._Q = Q  # constant coefficient
        self._SYM = sym

    def __eq__(self, other):
        """Return self == other."""
        if isinstance(other, QuadraticIntegerRing):
            return self._P == other._P and\
                   self._Q == other._Q and\
                   self._SYM == other._SYM
        return NotImplemented

    def __req__(self, other):
        """Return other == self."""
        return self == other


class QuadraticInteger:
    """Class representing an element in a QuadraticIntegerRing"""

    def __init__(self, base_ring, a, b):
        """Return a new QuadraticInteger in base_ring with
        rational/real part a and irrational/imaginary part b.
        """
        for _ in (a, b):
            if not isinstance(_, int):
                raise ValueError(f"{_} (coefficients must be integers)")
        if not isinstance(base_ring, QuadraticIntegerRing):
            raise ValueError(
                f"{base_ring} (base_ring must be a QuadraticIntegerRing)"
            )
        self._parent = base_ring
        self._r = a  # rational/real part
        self._i = b  # irrational/imaginary part

    def __int__(self):
        """Return the rational/real part of self."""
        return self._r

    def __neg__(self):
        """Return -self."""
        return QuadraticInteger(self._parent, -self._r, -self._i)

    def __same_base(self, other):
        """Check if self and other belong to the same base ring."""
        return isinstance(other, QuadraticInteger) and\
               self._parent == other._parent

    def __add__(self, other):
        """Return self + other."""
        if isinstance(other, int):
            return QuadraticInteger(self._parent, self._r + other, self._i)
        if self.__same_base(other):
            return QuadraticInteger(
                self._parent,
                self._r + other._r,
                self._i + other._i
            )
        return NotImplemented

    def __sub__(self, other):
        """Return self - other."""
        return self + -other

    def __mul__(self, other):
        """Return self * other."""
        if isinstance(other, int):
            return QuadraticInteger(
                self._parent,
                self._r * other,
                self._i * other
            )
        if self.__same_base(other):
            # (a + bx)(c + dx) = (ac - bdQ) + (ad + bc + bdP)x
            return QuadraticInteger(
                self._parent,
                self._r*other._r - self._i*other._i*self._parent._Q,
                self._r*other._i + self._i*other._r + self._i*other._i*self._parent._P
            )
        return NotImplemented

    def __eq__(self, other):
        """Return self == other."""
        if isinstance(other, int):
            return self._r == other and self._i == 0
        if self.__same_base(other):
            return self._r == other._r and self._i == other._i
        return NotImplemented

    def __radd__(self, other):
        """Return other + self."""
        return self + other

    def __rsub__(self, other):
        """Return other - self."""
        return -self + other

    def __rmul__(self, other):
        """Return other * self."""
        return self * other

    def __req__(self, other):
        """Return other == self."""
        return self == other

    def __pow__(self, other):
        """Return self**other."""
        if isinstance(other, int) and other >= 0:
            if other == 0:
                return 1
            if other % 2 == 0:
                sqrt = self**(other//2)
                return sqrt * sqrt
            return self * self**(other-1)
        raise ValueError(f"{other} (exponent must be a positive integer)")

    def __repr__(self):
        rat = self._r
        irr = f"{abs(self._i)}*{self._parent._SYM}"
        sgn = "+" if self._i > 0 else "-"

        if self._i == 0:
            return f"{rat}"
        if abs(self._i) == 1:
            irr = self._parent._SYM

        if rat == 0:
            return f"{irr}" if sgn == "+" else f"{sgn}{irr}"
        return f"{rat} {sgn} {irr}"
