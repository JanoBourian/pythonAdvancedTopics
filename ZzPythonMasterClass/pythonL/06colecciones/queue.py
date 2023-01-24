### Las colas sólo permiten añadir un elemento a la cola y sacar un elementos de la cola
from collections import deque
cola = deque(['Juan', 'Miguel', 'Bryan', 'Roberto'])
cola
cola.append('Milton')
cola
cola.popleft()
cola