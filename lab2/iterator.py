
def count_to(count):
    """Считает по количеству слов, максимум до пяти"""
    numbers = ["one", "two", "three", "four", "five"]
    yield from numbers[:count]


# Тест генератора
count_to_two = lambda: count_to(2)
count_to_five = lambda: count_to(5)


def main():
    """
    # Считая до двух...
    >>> for number in count_to_two():
    ...     print(number)
    one
    two
    # Считая до пяти...
    >>> for number in count_to_five():
    ...     print(number)
    one
    two
    three
    four
    five
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
