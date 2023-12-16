import random
EULER = 2.718281828459045

def compute_e(num_int: int = 1) -> float:
    total_iter = 0
    for _ in range(num_int):
        suma_val = 0
        while (suma_val <= 1):
            suma_val += random.uniform(0, 1)
            total_iter += 1
    return total_iter / num_int

def get_e(tol:float = 0.001) -> float:
    total_iter = 0
    max_iter = 1
    while( abs((total_iter/max_iter) - EULER) > tol ):
        suma_val = 0
        while (suma_val <= 1):
            suma_val += random.uniform(0, 1)
            total_iter += 1
        max_iter += 1
    print((total_iter/max_iter))
    return total_iter 

if __name__ == "__main__":
    aprox_e = compute_e(510116704)
    print(aprox_e)
    aprox_e = get_e(0.00000000001)
    print(aprox_e)