class Node:
    # Start
    def __init__(self, data=None, next=None):
        self._data = data
        self._next = next
    
    # Getters
    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    # Setters
    def set_data(self, valor):
        self._data = valor
    
    def set_next(self, valor):
        self._next = valor

    # Print
    def __str__(self):
        return str(self._data)