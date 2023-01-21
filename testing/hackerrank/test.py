import doctest

def evaluate_process(n:int) -> str:
    """Return a string based on a rule

    Args:
        n (int): Integer to evaluate

    Returns:
        str: Message 
        
    >>> evaluate_process(1)
    'Weird'
    """
    if (n%2 != 0) or n in range(6,21):
        return "Weird"
    else:
        return "Not Weird"

if __name__ == '__main__':
    doctest.testmod()