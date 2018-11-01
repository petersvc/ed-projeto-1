from node import Node

class LinkedList:

    # Start
    def __init__(self, head = None, tail = None):
        self._head = head
        self._tail = tail
        self.total = 1
    
    # Add head
    def add_head(self, new_data):
        aux = Node(new_data)
        if self._head == None:
            self._tail = self._head = aux
            self.count()
            print('Adicionado')
        else:
            aux.set_next(self._head)
            self._head = aux
            self.count()
            print('Adicionado')
    
    # Add middle
    def add_middle(self, new_data):
        aux = Node(new_data)        
        if self._head == None:
            self._tail = self._head = aux
            self.count()
        else:
            pos = int(input('Digite a posicao para inserir: '))
            # adicionar any place but head or tail
            if pos >= self.total-1 or pos <= 0:
                print('Impossivel inserir na posicao ',pos,'!')
            else:
                print('Total:', self.total)
                p = q = self._head
                for i in range(pos-1):
                    p = p.get_next()
                for i in range(pos):
                    q = q.get_next()
                aux.set_next(q)
                p.set_next(aux)
                self.count()

    # Add tail               
    def add_tail(self, new_data):
        aux = Node(new_data)
        p = self._head
        if self._head == None:
            self._tail = self._head = aux
            self.count()
            print('Adicionado')
        else:
            while p.get_next() != None:
                p = p.get_next()
            p.set_next(aux)
            self._tail = aux
            self.count()
            print('Adicionado')

    def remove_head(self):
        if self._head != None:
            self._head = self._head.get_next()
            self.countn()
            print('Removido')
        else:
            print('Falha,',self.vazia())

    def remove_middle(self):
        pos = int(input('> Digite a posicao para remover:'))
        if pos <= 0 or pos >= self.total-1:
            print('>> Não foi possivel remover da posicao',pos,'!')
        else:
            p = q = self._head
            for i in range(pos-1):
                p = p.get_next()
            for i in range(pos):
                q = q.get_next()
            if q.get_next() == None:
                print('>> Não foi possivel remover da posicao',pos,'!')
            else:
                p.set_next(q.get_next())
                print('Removido!')
            self.countn()

    def remove_tail(self):
        if self._head != None:
            p = self._head
            q = self._tail
            if self._head == self._tail:
                self._head = self._tail = None
                print('Removido!')
                self.countn()
            elif p.get_next() == q:
                p.set_next(None)
                self._tail = p
                print('Removido!')
                self.countn()
            else:
                while p.get_next() != q:
                    p = p.get_next()
                p.set_next(None)
                self._tail = p
                self.countn()
                print('Removido!')
        else:
            print('Erro, {}'.format(self.vazia()))

    
    #verificar se esta vazia
    def vazia(self):
        if self._head == None:
            return 'Lista vazia!' 
        return 'Lista não vazia!'

    #verificar o tamanho
    def tamanho(self):
        tam = 1
        aux = self._head
        if aux == None:
            return self.vazia()
        else:
            while aux.get_next() != None:
                tam+=1
                aux = aux.get_next()
        return tam

#visualizar o dado de uma posicao
    def visualizar(self):
        pos = int(input('> Digite o numero da posicao para visualizar:'))
        if pos < 0 or pos > self.total-2:
            return '>> Não foi possivel visualizar a posicao [{}], dado nulo.'.format(pos)
        else:
            aux = self._head
            teste = 0
            while aux.get_next() != None:
                if teste == pos:
                    return aux.get_data()
                teste+=1
                aux = aux.get_next()
            return aux.get_data()

    #str da lista
    def __str__(self):
        if self._head != None:
            res = ''
            aux = self._head
            res+= aux.get_dado()+' '
            while aux.get_next() != None:
                aux = aux.get_next()
                res+= aux.get_dado()+' '
            return '{}'.format(res)
        else:
            return 'Lista vazia!'

    def count(self):
        self.total+=1
        
    def countn(self):
        self.total-=1
