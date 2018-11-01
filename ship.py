from node import Node
#from container import Container

class Ship: # QUEUE

    # Start
    def __init__(self, top = None):
        self._top = top

    # Add
    def queue_add(self, new_data):
        aux = Node(new_data)
        if self._top == None:
            self._top = aux
        else:
            aux = self._top
            while aux.get_next() != None:
                aux = aux.get_next()
            aux2 = Node()
            aux2.set_data(new_data)
            aux.set_next(aux2)
            aux2.set_next(None)        
    
    # Remove
    def queue_remove(self):
        if self._top == None:
            print('Fila vazia')
        else:
            self._top = self._top.get_next()
    
    # Stack size
    def queue_size(self):
        aux = self._top
        count = 0
        while aux != None:
            aux = aux.get_next()
            count+=1
        return count
    
    # Is empty
    def queue_is_empty(self):
        return self._top == None
    
    # Top
    def get_top(self):
        return self._top