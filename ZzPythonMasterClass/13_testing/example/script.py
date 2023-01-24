from random import randint


def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print('hey bozo, I said 1~10!')
        return False


def guess_input():
    guess = int(input("guess a number 1~10: "))
    return guess


if __name__ == '__main__':
    answer = randint(1, 10)
    while True:
        try:
            guess = guess_input()
            if run_guess(guess, answer):
                break
        except ValueError:
            print("Enter a number")
            continue
