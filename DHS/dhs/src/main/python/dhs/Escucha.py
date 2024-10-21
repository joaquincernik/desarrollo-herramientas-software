from antlr4 import ErrorNode, TerminalNode
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from TablaSimbolos import TablaSimbolos
from Contexto import Contexto
from ID import ID

class Escucha (compiladoresListener) :
    tablaDeSimbolos=TablaSimbolos()

    #para el contador total del programa
    numTokensTotal = 0
    numNodosTotal = 0

    #para cada bloque
    numTokens=0
    numNodos=0


    
    # COMIENZO DE PROGRAMA
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print('Comienza compilacion\n')


    # Enter a parse tree produced by compiladoresParser#iwhile.
    def enterIwhile(self, ctx:compiladoresParser.IwhileContext):
        print('***Se entra a un WHILE***\n')
        #print('\tCantidad de hijos: '+ str(ctx.getChildCount()))
        #print('\tTOQUENS: '+ ctx.getText())

    # Exit a parse tree produced by compiladoresParser#iwhile.
    def exitIwhile(self, ctx:compiladoresParser.IwhileContext):
        print('Fin de WHILE')
        print('Cantidad de hijos: '+ str(ctx.getChildCount()))
        print('TOQUENS: '+ str(ctx.getText())+"\n")


    # Enter a parse tree produced by compiladoresParser#declaracion.
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        print(' ### Declaracion ###')

    # Exit a parse tree produced by compiladoresParser#declaracion.
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        tipoDeDato= ctx.getChild(0).getText()
        nombreVariable= ctx.getChild(1).getText()
        
        #Las busquedas si devuelven 1 es porque encontraron algo
        busquedaGlobal = self.tablaDeSimbolos.buscarGlobal(nombreVariable)
        busquedaLocal = self.tablaDeSimbolos.buscarLocal(nombreVariable)
       
        if busquedaGlobal == 1 and busquedaLocal == 1 :
            print('"'+nombreVariable+'"'+" como id de variable esta facha facha, segui asi!\n")
            self.tablaDeSimbolos.addIdentificador(nombreVariable,tipoDeDato)
        
        else : 
            if busquedaGlobal != 1 :
                print('ERROR: "' + nombreVariable +'" YA ESTA USADO GLOBALMENTE PA! BUSCATE OTRO \n')

            else:
                print('ERROR: "' + nombreVariable +'" YA ESTA USADO LOCALENTE PA! BUSCATE OTRO \n')


            



    def enterAsignacion(self, ctx: compiladoresParser.AsignacionContext):
        print(" ### ASIGNACION ###")

    def exitAsignacion(self, ctx: compiladoresParser.AsignacionContext):
        nombreVariable= ctx.getChild(0).getText()
        busquedaGlobal = self.tablaDeSimbolos.buscarGlobal(nombreVariable)

        
        #buscamos si la variable fue declarada globalmente
        if busquedaGlobal == 1 :

            #no la encontro entonces la busco localmente
            busquedaLocal = self.tablaDeSimbolos.buscarLocal(nombreVariable)

            if busquedaLocal == 1 :
                #entonces no la encontro en ningun lado
                print("ERROR: Loco no se que es " + nombreVariable + " tenes que declararla primero !\n")
            else :
                busquedaLocal.inicializado = 1

        else :
            #la encontro en el contexto global 
            busquedaGlobal.inicializado = 1
        


#para saber si estoy en una hoja
    def visitTerminal(self, node: TerminalNode):
        self.numTokensTotal+=1 
        self.numTokens +=1 


    def visitErrorNode(self, node: ErrorNode):
        print('----> ERROR')  
    
    #cada vez que entro en una regla aumento el contador
    def enterEveryRule(self, ctx):
        self.numNodosTotal +=1
        self.numNodos +=1

    #contexto:
    # Enter a parse tree produced by compiladoresParser#bloque.
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        print('***Entre a un CONTEXTO***\n')
        contexto= Contexto()
        self.tablaDeSimbolos.addContexto(contexto)
        



    # Exit a parse tree produced by compiladoresParser#bloque.
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        print('***Sali de un CONTEXTO***')
        #print('Cantidad de hijos: '+ str(ctx.getChildCount()))
        #print('TOQUENS: '+ ctx.getText())

        print("En este contexto se encontro lo siguiente:")
        self.tablaDeSimbolos.contextos[-1].imprimirTabla()
        print("********************************************\n")
        self.tablaDeSimbolos.delContexto()

    
    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        #
        print('Fin compilacion\n')
        print("En el contexto global se encontro lo siguiente:")
        self.tablaDeSimbolos.contextos[-1].imprimirTabla()
        print("********************************************\n")
        
        #print('Se encontraron: ')
        #print('Nodos: '+ str(self.numNodosTotal))
        #tokens son las hojas
        #print('\tTokens: '+ str(self.numTokensTotal))
        #print("Cantidad de contextos encontrados en esta tabla de simbolos: "+self.tablaDeSimbolos.nombre)






