# Generated from /home/joaquincernik/Desktop/facultad/DHS/dhs/src/main/python/dhs/compiladores.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete listener for a parse tree produced by compiladoresParser.
class compiladoresListener(ParseTreeListener):

    # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass


    # Enter a parse tree produced by compiladoresParser#instrucciones.
    def enterInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instrucciones.
    def exitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        pass


    # Enter a parse tree produced by compiladoresParser#instruccion.
    def enterInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instruccion.
    def exitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#declaracion.
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#declaracion.
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#asignacion.
    def enterAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#asignacion.
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#opal.
    def enterOpal(self, ctx:compiladoresParser.OpalContext):
        pass

    # Exit a parse tree produced by compiladoresParser#opal.
    def exitOpal(self, ctx:compiladoresParser.OpalContext):
        pass


    # Enter a parse tree produced by compiladoresParser#or.
    def enterOr(self, ctx:compiladoresParser.OrContext):
        pass

    # Exit a parse tree produced by compiladoresParser#or.
    def exitOr(self, ctx:compiladoresParser.OrContext):
        pass


    # Enter a parse tree produced by compiladoresParser#o.
    def enterO(self, ctx:compiladoresParser.OContext):
        pass

    # Exit a parse tree produced by compiladoresParser#o.
    def exitO(self, ctx:compiladoresParser.OContext):
        pass


    # Enter a parse tree produced by compiladoresParser#and.
    def enterAnd(self, ctx:compiladoresParser.AndContext):
        pass

    # Exit a parse tree produced by compiladoresParser#and.
    def exitAnd(self, ctx:compiladoresParser.AndContext):
        pass


    # Enter a parse tree produced by compiladoresParser#a.
    def enterA(self, ctx:compiladoresParser.AContext):
        pass

    # Exit a parse tree produced by compiladoresParser#a.
    def exitA(self, ctx:compiladoresParser.AContext):
        pass


    # Enter a parse tree produced by compiladoresParser#comp.
    def enterComp(self, ctx:compiladoresParser.CompContext):
        pass

    # Exit a parse tree produced by compiladoresParser#comp.
    def exitComp(self, ctx:compiladoresParser.CompContext):
        pass


    # Enter a parse tree produced by compiladoresParser#c.
    def enterC(self, ctx:compiladoresParser.CContext):
        pass

    # Exit a parse tree produced by compiladoresParser#c.
    def exitC(self, ctx:compiladoresParser.CContext):
        pass


    # Enter a parse tree produced by compiladoresParser#exp.
    def enterExp(self, ctx:compiladoresParser.ExpContext):
        pass

    # Exit a parse tree produced by compiladoresParser#exp.
    def exitExp(self, ctx:compiladoresParser.ExpContext):
        pass


    # Enter a parse tree produced by compiladoresParser#term.
    def enterTerm(self, ctx:compiladoresParser.TermContext):
        pass

    # Exit a parse tree produced by compiladoresParser#term.
    def exitTerm(self, ctx:compiladoresParser.TermContext):
        pass


    # Enter a parse tree produced by compiladoresParser#e.
    def enterE(self, ctx:compiladoresParser.EContext):
        pass

    # Exit a parse tree produced by compiladoresParser#e.
    def exitE(self, ctx:compiladoresParser.EContext):
        pass


    # Enter a parse tree produced by compiladoresParser#t.
    def enterT(self, ctx:compiladoresParser.TContext):
        pass

    # Exit a parse tree produced by compiladoresParser#t.
    def exitT(self, ctx:compiladoresParser.TContext):
        pass


    # Enter a parse tree produced by compiladoresParser#factor.
    def enterFactor(self, ctx:compiladoresParser.FactorContext):
        pass

    # Exit a parse tree produced by compiladoresParser#factor.
    def exitFactor(self, ctx:compiladoresParser.FactorContext):
        pass


    # Enter a parse tree produced by compiladoresParser#iwhile.
    def enterIwhile(self, ctx:compiladoresParser.IwhileContext):
        pass

    # Exit a parse tree produced by compiladoresParser#iwhile.
    def exitIwhile(self, ctx:compiladoresParser.IwhileContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloque.
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloque.
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        pass


    # Enter a parse tree produced by compiladoresParser#ifor.
    def enterIfor(self, ctx:compiladoresParser.IforContext):
        pass

    # Exit a parse tree produced by compiladoresParser#ifor.
    def exitIfor(self, ctx:compiladoresParser.IforContext):
        pass


    # Enter a parse tree produced by compiladoresParser#init.
    def enterInit(self, ctx:compiladoresParser.InitContext):
        pass

    # Exit a parse tree produced by compiladoresParser#init.
    def exitInit(self, ctx:compiladoresParser.InitContext):
        pass


    # Enter a parse tree produced by compiladoresParser#cond.
    def enterCond(self, ctx:compiladoresParser.CondContext):
        pass

    # Exit a parse tree produced by compiladoresParser#cond.
    def exitCond(self, ctx:compiladoresParser.CondContext):
        pass


    # Enter a parse tree produced by compiladoresParser#iter.
    def enterIter(self, ctx:compiladoresParser.IterContext):
        pass

    # Exit a parse tree produced by compiladoresParser#iter.
    def exitIter(self, ctx:compiladoresParser.IterContext):
        pass


    # Enter a parse tree produced by compiladoresParser#incremento.
    def enterIncremento(self, ctx:compiladoresParser.IncrementoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#incremento.
    def exitIncremento(self, ctx:compiladoresParser.IncrementoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#decremento.
    def enterDecremento(self, ctx:compiladoresParser.DecrementoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#decremento.
    def exitDecremento(self, ctx:compiladoresParser.DecrementoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#preincremento.
    def enterPreincremento(self, ctx:compiladoresParser.PreincrementoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#preincremento.
    def exitPreincremento(self, ctx:compiladoresParser.PreincrementoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#predecremento.
    def enterPredecremento(self, ctx:compiladoresParser.PredecrementoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#predecremento.
    def exitPredecremento(self, ctx:compiladoresParser.PredecrementoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#if.
    def enterIf(self, ctx:compiladoresParser.IfContext):
        pass

    # Exit a parse tree produced by compiladoresParser#if.
    def exitIf(self, ctx:compiladoresParser.IfContext):
        pass


    # Enter a parse tree produced by compiladoresParser#else.
    def enterElse(self, ctx:compiladoresParser.ElseContext):
        pass

    # Exit a parse tree produced by compiladoresParser#else.
    def exitElse(self, ctx:compiladoresParser.ElseContext):
        pass



del compiladoresParser