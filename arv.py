class Tree:
    def __init__(self,dado=None,pai=None,esq=None,dire=None):
        self._dado=dado
        self._pai=pai
        self._f_esq=esq
        self._f_dir=dire

    def get_dado(self):
        return self._dado
    def get_pai(self):
        return self._pai
    def get_esq(self):
        return self._f_esq
    def get_dir(self):
        return self._f_dir
    def set_dado(self,novo):
        self._dado=novo
    def set_pai(self,novo):
        self._pai=novo
    def set_esq(self,valor):
        self._f_esq=valor
    def set_dir(self,valor):
        self._f_dir=valor
