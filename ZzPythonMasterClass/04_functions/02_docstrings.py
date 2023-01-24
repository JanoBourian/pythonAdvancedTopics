def test(a) -> None:
    '''
    Info: this function tests and prints param a
    '''

    print(a)


test("hihi")

# help(test)

print(test.__doc__)


def is_even(num) -> bool:
    return num % 2 == 0


print(is_even(5))
