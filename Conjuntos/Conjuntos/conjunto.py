class Conjunto():
    def __init__(self, nome):
        self.lista = []
        self.nome = nome
        
    def inserir(self, dados):
        if not dados in self.lista: 
            self.lista.append(dados)
        else:
            print(dados + ', já existente no conjunto')


    def tamanho(self,):
        return len(self.lista)


    def pertence(self,dado):
        return dado in self.lista


    def contem(self,conj):
        for elemento in conj:
            if elemento not in self.lista:
                return False
        return True
            
            
                 
    def show(self):
        if len(self.lista) == 0:
            print (' Conjunto Vazio: ' + self.nome + ' ={ }')
        else:
            aux = ', '.join(self.lista)
            print(self.nome + '={ ' + aux + ' }')
 
