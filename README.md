# Symbolic Integer Arithmetic in Quadratic Integer Rings

```
>>> from quadratic_integer import QuadraticIntegerRing, QuadraticInteger
>>> zphi = QuadraticIntegerRing(1, -1, "phi")
>>> phi = QuadraticInteger(zphi, 0, 1)
>>> phi**2
1 + phi
>>> psi = QuadraticInteger(zphi, 1, -1)
>>> psi
1 - phi
>>> phi + psi == -1
False
>>> phi + psi == 1
True
>>> phi * psi
-1
>>> def fib(n):
...     return int(phi**(n+1))
...
>>> fib(5)
5
>>> def luc(n):
...     return phi**n + psi**n
...
>>> luc(5)
11
>>> fib(10) == fib(5) * luc(5)
True
```

Run `help("quadratic_integer")` for more information.
