from node import Node

class Container: # STACK

    # Start
    def __init__(self, top = None):
        self._top = top

    # Add
    def add(self, new_data):
        aux = Node()
        aux.set_data(new_data)
        aux.set_next(self._top)
        self._top = aux
        return self._top
    
    # Remove
    def remove(self):
        if self._top == None:
            print('Pilha vazia')
        else: 
            self._top = self._top.get_next()

    # Is empty
    def is_empty(self):
        return self._top == None
    
    # Stack size
    def size(self):
        aux = self._top
        count = 0
        while aux != None:
            aux = aux.get_next()
            count+=1
        return count

    # Top
    def get_top(self):
        return self._top