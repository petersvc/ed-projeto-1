from node import Node
#from container import Container

class Ship: # QUEUE
    def __init__(self, top=None):
        self._top = top

    def queue_add(self, item):
        aux = Node(item)
        if self._top is None:
            self._top = aux
        else:
            aux = self._top
            while aux.get_next() != None:
                aux = aux.get_next()
            aux2 = Node()
            aux2.set_data(item)
            aux.set_next(aux2)
            aux2.set_next(None)        
    
    # Remove
    def queue_remove(self):
        if self._top is None:
            raise IndexError("Nao contem elemento.")
        self._top = self._top.get_next()
    
    # Stack size
    def queue_size(self):
        aux = self._top
        count = 0
        while aux is not None:
            aux = aux.get_next()
            count+=1
        return count
    
    # Is empty
    def queue_is_empty(self):
        return self._top is None
    
    # Top
    def get_top(self):
        return self._top