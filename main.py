from node import Node
from container import Container
from ship import Ship
from linked_list import LinkedList
opt = 0
container = Container()
ship = Ship()
linked_list = LinkedList()

while opt != 6:
    print('op1 = Adicionar navio')
    print('op2 = Remover navio')
    print('op3 = Ver se está vazia')
    print('op4 = Ver o tamanho da fila')
    print('op5 = Ver o topo')
    print('op6 = Sair')
    opt = int(input('Digite a opção:'))
    if opt == 1:
        ship.queue_add(input('Bora:'))
    elif opt == 2:
        ship.queue_remove()
    elif opt == 3:
        print(ship.queue_is_empty())
    elif opt == 4:
        print(ship.queue_size())
    elif opt == 5:
        print(ship.get_top())
       
'''
while opt != 6:
    print('op1 = Adicionar container')
    print('op2 = Remover container')
    print('op3 = Ver se está vazia')
    print('op4 = Ver o tamanho da pilha')
    print('op5 = Ver o topo')
    print('op6 = Sair')
    opt = int(input('Digite a opção:'))
    if opt == 1:
        container.add(int(input('Bora:')))
    elif opt == 2:
        container.remove()
    elif opt == 3:
        print(container.is_empty())
    elif opt == 4:
        print(container.size())
    elif opt == 5:
        print(container.get_top())
'''

'''
while opt != 10:
    print('op1 = Adicionar terminal')
    print('op2 = Remover terminal')
    print('op3 = Ver se está vazia')
    print('op4 = Ver o tamanho da lista')
    print('op5 = Ver o topo')
    print('op6 = Sair')
    opt = int(input('Digite a opção:'))
    if opt == 1:
        linked_list.add_head(input('Bora:'))
    elif opt == 2:
        linked_list.add_middle(input('Bora:'))
    elif opt == 3:
        linked_list.add_tail(input('Bora'))
    elif opt == 4:
        linked_list.remove_head()
    elif opt == 5:
        linked_list.remove_middle()
    elif opt == 6:
        linked_list.remove_tail()
    elif opt == 7:
        print(linked_list.tamanho())
    elif opt == 8:
        print(linked_list.vazia())
    elif opt == 9:
        print(linked_list.visualizar())
'''