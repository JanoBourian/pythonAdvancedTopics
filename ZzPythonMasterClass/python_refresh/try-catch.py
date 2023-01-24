def start():
    try:
      years = int(input("Insert your age: "))
      print(f"Yeah, your age is {years}")
    except Exception as err:
      print(f'An exception occurred: {err}')
    
if __name__ == '__main__':
    start()