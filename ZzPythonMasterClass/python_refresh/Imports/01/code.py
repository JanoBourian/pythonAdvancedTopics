from mymodule import (divide,)
import sys
result = divide(10, 20)
print(f'code __name__: {__name__}')
print(f'result: {result}')
print(f'sys.path: {sys.path}')
print(f'sys.modules: {sys.modules}')