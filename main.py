from node import Node
from container import Container
from ship import Ship
opt = 0
container = Container()
ship = Ship()

while opt != 6:
    print('op1 = Adicionar container')
    print('op2 = Remover container')
    print('op3 = Ver se está vazia')
    print('op4 = Ver o tamanho da pilha')
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
        print(container.get_top())'''

