def get_pair_quotient_remainder(dividend, *, divisor):
    """The pair: an integer part of division, and its remainder.

    Function divides `dividend` by `divisor` and
    returns a pair (quotient, remainder), according to

    DIVIDEND = QUOTIENT * DIVISOR + REMAINDER

    Parameters
    ----------
    dividend : int
        Dividend
    divisor : int
        Divisor

    Returns
    -------
    (int, int)
        Pair (quotient, remainder)

    """
    return dividend // divisor, dividend % divisor


seconds = int(input('Input a time in seconds: '))

minutes, seconds = get_pair_quotient_remainder(seconds, divisor=60)
hours, minutes = get_pair_quotient_remainder(minutes, divisor=60)

print(f'{hours:02}:{minutes:02}:{seconds:02}')

