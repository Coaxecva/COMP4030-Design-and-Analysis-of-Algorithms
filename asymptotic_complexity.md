Asymptotic complexity
Upper bound
If T(n) is in O(g(n)), then T(n) <= c*g(n), for all large values of n.

T(n) is a function of n.
g(n) is a function of n.
O(g(n)) is a set of functions.

Examples:
n^2 + 10 is in O(n^2)
because n^2 + 10 <= 11n^2 for all values of n > 1.
Explain:  n^2 + 10 <= n^2 + 10n^2 = 11n^2  (when n > 1)

n^2 + 10 is in O(n^2) because n^2+10 <= 11*n^2 when n>1.
T(n) = n^2 + 10
g(n) = n^2
c = 11

2n^2 + 5n  is in O(n^2) because 2n^2 + 5n <= 7n^2 when n>1
2n^2 + 5n <= 2n^2 + 5n^2 = 7n^2.

T(n) = 2n^2 + 5n
g(n) = n^2
c = 7


T(n) = 27n + 5 is in O(n^2)
27n + 5 <= 27n^2 + 5n^ = 32n^2 when n>1.

===============================
Lower bound

If T(n) is in Ω(g(n)), then T(n) >= c*g(n), for all large values of n.

Is 2n^2 + 10 in Omega(n^2)?  True because 2n^2 + 10 >= 1n^2, when n>1.
2n^2 + 10 is in Omega(n)
2n^2 + 10 is in O(n^2). 

Is 2n^2 + 5n is Omega(n)?
Is 2n^2 + 5n >= 1*n when n>1?


===============================
Order of complexity

If T(n) is in Theta(g(n)), then T(n) is both in O(g(n)) and Omega(g(n)).

2n^2 + 10 is in Theta(n^2).

===============================


T or F?  n^2 - 10n is in O(n) because n^2 - 10n <= 5*n when n=1.  FALSE.  Because
the inequality must be satisfied for all large values of n.

===============================


