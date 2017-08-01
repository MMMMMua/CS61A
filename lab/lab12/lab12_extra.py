from stream import *
# Extra Questions

def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    >>> list(s)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    for ele in s:
        yield ele * k

def remainders_generator(m):
    """
    Takes in an integer m, and yields m different remainder groups
    of m.

    >>> remainders_mod_four = remainders_generator(4)
    >>> for rem_group in remainders_mod_four:
    ...     for _ in range(3):
    ...         print(next(rem_group))
    0
    4
    8
    1
    5
    9
    2
    6
    10
    3
    7
    11
    """
    def remainder_group(k):
        cur = k
        while True:
            yield cur
            cur += m

    for i in range(m):
        yield remainder_group(i)

# the naturals generator is used for testing the scale function
def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1

def zip(*iterables):
    """
    Takes in any number of iterables and zips them together.
    Returns a generator that outputs a series of lists, each
    containing the nth items of each iterable.
    >>> z = zip([1, 2, 3], [4, 5, 6], [7, 8])
    >>> for i in z:
    ...     print(i)
    ...
    [1, 4, 7]
    [2, 5, 8]
    """
    itr_lst = []
    for lst in iterables:
        itr_lst.append(iter(lst))
    while True:
        res = []
        for itr in itr_lst:
            res.append(next(itr))
        yield res
        

def convolve_streams(a, b):
    """
    >>> zeros = Stream(0, lambda: zeros)
    >>> a = Stream(2, lambda: Stream(3, lambda: Stream(1, lambda: zeros)))
    >>> b = Stream(6, lambda: Stream(-1, lambda: zeros))
    >>> c = convolve_streams(a, b)
    >>> _ = c.rest.rest.rest.rest
    >>> c
    Stream(12, Stream(16, Stream(3, Stream(-1, Stream(0, <Stream>)))))
    """
    def get_list(lst, sz):
        res = []
        for i in range(sz+1):
            res.append(lst.first)
            lst = lst.rest
        return res

    def get_nxt():
        expn = 0
        while True:
            lst_a = get_list(a, expn)
            lst_b = get_list(b, expn)

            lst_b.reverse()
            
            res = 0
            for i in range(expn+1):
                res += lst_a[i] * lst_b[i]

            expn += 1
            yield res

    genr =  get_nxt()
    f = lambda : Stream(next(genr), f)
    return  f()