result = (lambda x: [str(x), x] ) (5)
print(result)

def double(x):
    return x*2

sequence = [x for x in range(10)]
print(f'sequence: {sequence}')

doubled = map(lambda x: x*2, sequence)
print(f'doubled: {doubled}')

doubled = list(map(double, sequence))
print(f'doubled: {doubled}')

double_wc = [ (lambda x: x*2)(x) for x in sequence]
print(f'double_wc: {double_wc}')

print(f'sequence: {sequence}')