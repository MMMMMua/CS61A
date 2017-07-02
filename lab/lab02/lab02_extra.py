"""Optional program for lab02 """

from lab02 import *
import sys
# Higher Order Functions

def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function CONDITION.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    "*** YOUR CODE HERE ***"
    def count(n):
        tot = 0
        for i in range(n):
            tot += 1 if condition(n, i+1) == True else 0
        return tot

    return count

def add1(x):
    return x + 1
def times2(x):
    return x * 2
def add3(x):
    return x + 3

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    def proc(n):
        # def attr(x):
        #     for i in range(n):
        #         x = f1(x)
        #         f1, f2, f3 = f2, f3, f1

        # def attr(x):
        #     nonlocal f1, f2, f3
        #     for i in range(n):
        #         x = f1(x)
        #         f1, f2, f3 = f2, f3, f1
        #     return x
                
        def attr(x):
            g1, g2, g3 = f1, f2, f3
            for i in range(n):
                x = g1(x)
                g1, g2, g3 = g2, g3, g1
            return x
        return attr
    return proc

