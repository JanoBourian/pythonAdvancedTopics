from Classes.Device import (Device,)
from Classes.Lector import (Lector,)
from Classes.Printer import (Printer,)

def start() -> None: 
    cd1 = Lector('CD1', 'Lector 1', 'DVD')
    print(f'cd1: {cd1}')
    cd1.play()
    cd1.disconnect()
    press1 = Printer("Epson 4L150", "USB", 100)
    print(f'press1: {press1}')
    press1.print(150)
    press1.disconnect()
    help(Lector)

if __name__ == '__main__':
    start()