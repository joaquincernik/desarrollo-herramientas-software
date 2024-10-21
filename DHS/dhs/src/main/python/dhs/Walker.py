from compiladoresParser import compiladoresParser
from compiladoresVisitor import compiladoresVisitor

class Walker (compiladoresVisitor) :
    def visitPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print('=.'* 20)
        print("-- Comienzo a caminar --")
        temp = super().visitPrograma(ctx)
        print('=.'* 20)
        print("-- Fin de la caminata --")
        return temp
    
    def visitBloque(self, ctx: compiladoresParser.BloqueContext):
        print("-- Nuevo contexto --")

        #te muestra todo el texto del bloque por ejemplo :
        print(ctx.getText())
        # no quiero visitar las llaves quiero ver solo las instrucciones
        return super().visitInstrucciones(ctx.getChild(1))
    

    def visitDeclaracion(self, ctx: compiladoresParser.DeclaracionContext):
        #esto funciona solo co nuna variable
        print(ctx.getChild(0).getText() + '-' +
              ctx.getChild(1).getText())
        return None
    

    def visitTerminal(self, node):
        print("-- Toquen : " + node.getText() + "--")
        return super().visitTerminal(node)