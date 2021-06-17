# Symbolic Integer Arithmetic in Quadratic Integer Rings

Example usage (run `help("quadratic_integer")` for details):

## Arithmetic in <img src="https://render.githubusercontent.com/render/math?math=\mathbb Z[\phi]" width=45>
```
>>> from quadratic_integer import QuadraticIntegerRing, QuadraticInteger
>>> Zphi = QuadraticIntegerRing(1, -1, "phi")
>>> phi = QuadraticInteger(Zphi, 0, 1)
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

## Finding Units in Quadratic Integer Rings
```
>>> from quadratic_integer import QuadraticIntegerRing, QuadraticInteger
>>> Zi = QuadraticIntegerRing(0, 1, "i")
>>> for x in range(-100, 100):
...     for y in range(-100, 100):
...         z = QuadraticInteger(Zi, x, y)
...         if abs(z.norm() == 1):
...             print(z)
...
-1
-i
i
1
>>> Zomega = QuadraticIntegerRing(-1, 1, "omega")
>>> for x in range(-100, 100):
...     for y in range(-100, 100):
...         z = QuadraticInteger(Zomega, x, y)
...         if abs(z.norm()) == 1:
...             print(z)
...
-1 - omega
-1
-omega
omega
1
1 + omega
```
