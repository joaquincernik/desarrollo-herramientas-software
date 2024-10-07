from antlr4 import ErrorNode, TerminalNode
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser

class Escucha (compiladoresListener) :
    numTokens = 0
    numNodos = 0

    # Enter a parse tree produced by compiladoresParser#iwhile.
    def enterIwhile(self, ctx:compiladoresParser.IwhileContext):
        print('Encontre WHILE')
        print('\tCantidad de hijos: '+ str(ctx.getChildCount()))
        print('\tTOQUENS: '+ ctx.getText())

    # Exit a parse tree produced by compiladoresParser#iwhile.
    def exitIwhile(self, ctx:compiladoresParser.IwhileContext):
        print('Fin de WHILE')
        print('\tCantidad de hijos: '+ str(ctx.getChildCount()))
        print('\tTOQUENS: '+ str(ctx.getText()))


    
    # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print('Comienza compilacion')

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print('Fin compilacion')
        print('Se encontraron: ')
        print('\Nodos: '+ str(self.numNodos))
        #tokens son las hojas
        print('\tTokens: '+ str(self.numTokens))

    
    # Enter a parse tree produced by compiladoresParser#declaracion.
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        print(' ### Declaracion')

    # Exit a parse tree produced by compiladoresParser#declaracion.
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        print('Nombre variable: '+ ctx.getChild(1).getText())


#para saber si estoy en una hoja
    def visitTerminal(self, node: TerminalNode):
        self.numTokens+=1 

    def visitErrorNode(self, node: ErrorNode):
        print('----> ERROR')  
    
    #cada vez que entro en una regla aumento el contador
    def enterEveryRule(self, ctx):
        self.numNodos +=1





