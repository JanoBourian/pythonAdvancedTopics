def do_stuff(num: float) -> float:
    try:
        if num:
            return int(num) + 5
        else:
            return 'please enter number'
    except ValueError as err:
        return err
