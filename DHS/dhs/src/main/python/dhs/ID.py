class ID():
    
    def __init__(self,nombre,tipoDato,inicializado,usado):
        self.nombre=nombre
        self.tipoDato=tipoDato
        self.inicializado=inicializado
        self.usado=usado

    def __str__(self):
        return("ID: \t"+self.nombre+"\t"+self.tipoDato)

     
class Variable(ID):
    def __init__(nombre,tipoDato,inicializado,usado):
        super.__init__(nombre,tipoDato,inicializado,usado)


class Funcion(ID):
    def __init__(self,nombre,tipoDato,inicializado,usado,args):
        super.__init__(nombre,tipoDato,inicializado,usado)
        self.args=args
