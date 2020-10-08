class SumaDos: # un iterador que suma 2 a cada elemento de la lista pasada.
    def __init__(self, datos):
        self.datos = datos
        self.indice = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.indice == len(self.datos):
            raise StopIteration()
        elemento = self.datos[self.indice] + 2
        
        self.indice += 1
        
        return elemento
    
list(SumaDos([1,2,3,4,5])) # [1+2, 2+2, 3+2, 4+2, 5+2]