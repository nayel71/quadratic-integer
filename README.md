# Symbolic Integer Arithmetic in Quadratic Integer Rings

```
>>> from quadratic_integer import QuadraticIntegerRing, QuadraticInteger
>>> zphi = QuadraticIntegerRing(1, -1, "phi")
>>> phi = QuadraticInteger(zphi, 0, 1)
>>> phi**2
1 + phi
>>> psi = phi.conj()
>>> psi
1 - phi
>>> phi + psi == 1
True
>>> phi * psi
-1
>>> phi.norm()
-1
>>> def irr(z):
...     return (int(z)-z) * psi
...
>>> def fib(n):
...     return irr(phi**n)
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
