from Contexto import Contexto
from ID import ID
class TablaSimbolos(object):

    __instance= None 
    contextos=[]   
    

    def __new__(cls):
        if TablaSimbolos.__instance is None:
            TablaSimbolos.__instance = object.__new__(cls)
        return TablaSimbolos.__instance
    
    def __init__(self) :
        contextoGlobal= Contexto()
        self.contextos.append(contextoGlobal)

    def addContexto(self,contexto):
        self.contextos.append(contexto) 
        print("largo de la lista de contextos: "+str(len(self.contextos)))

    def delContexto(self):
        self.contextos.pop()

    def addIdentificador(self,nombre,tipoDato):
        contexto=self.contextos[-1]
        id = ID(nombre,tipoDato,1,1)
        contexto.tabla.update({nombre:id})
        print("SE ANADIO UN IDENTIFICADOR")

    def buscarLocal(self, nombre):

        if (self.contextos[-1].traerVariable(nombre))==None:
            print('"'+nombre+'"'+" como id de variable esta facha facha, segui asi!\n")

        else:
            print(nombre+" YA ESTA SIENDO USADO PA, BUSCATE OTRO!!!!\n")


    

    #def addIdentificador(self,tipo,nombreVariable):
