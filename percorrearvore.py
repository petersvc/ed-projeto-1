from arv import Tree
'''def pecorre_pre+(arvore):
    if(arvore!=None):
        print(arvore)
        percorre_pre(arvore.get_esq())
        pecorre_pre(arvore.get_dir())
 '''   

def pecorre_ordem(arvore):
    if(arvore!=None):
        percorre_pre(arvore.get_esq())
        print(arvore)
        pecorre_pre(arvore.get_dir())  

def percorre_posordem(arvore):
    if(arvore!=None):
        percorre_pre(arvore.get_esq())
        pecorre_pre(arvore.get_dir())                                                                      
        print(arvore)
    
#digamos que o primeiro esteja o valor none
def cria_arvore(valor):
    p=Tree()
    p.set_dado(valor)
    primeiro=p
    if primeiro:
        primeiro.set_esq=p
        p.set_pai(primeiro)