# Generated from /home/joaquincernik/Desktop/facultad/DHS/dhs/src/main/python/dhs/compiladores.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete generic visitor for a parse tree produced by compiladoresParser.

class compiladoresVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compiladoresParser#tipodato.
    def visitTipodato(self, ctx:compiladoresParser.TipodatoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#tipodatofunc.
    def visitTipodatofunc(self, ctx:compiladoresParser.TipodatofuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#programa.
    def visitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instrucciones.
    def visitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instruccion.
    def visitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#declaracion.
    def visitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#asignacion.
    def visitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#opal.
    def visitOpal(self, ctx:compiladoresParser.OpalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#or.
    def visitOr(self, ctx:compiladoresParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#o.
    def visitO(self, ctx:compiladoresParser.OContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#and.
    def visitAnd(self, ctx:compiladoresParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#a.
    def visitA(self, ctx:compiladoresParser.AContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#comp.
    def visitComp(self, ctx:compiladoresParser.CompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#c.
    def visitC(self, ctx:compiladoresParser.CContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#exp.
    def visitExp(self, ctx:compiladoresParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#term.
    def visitTerm(self, ctx:compiladoresParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#e.
    def visitE(self, ctx:compiladoresParser.EContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#t.
    def visitT(self, ctx:compiladoresParser.TContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#factor.
    def visitFactor(self, ctx:compiladoresParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#iwhile.
    def visitIwhile(self, ctx:compiladoresParser.IwhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque.
    def visitBloque(self, ctx:compiladoresParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#ifor.
    def visitIfor(self, ctx:compiladoresParser.IforContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#init.
    def visitInit(self, ctx:compiladoresParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#cond.
    def visitCond(self, ctx:compiladoresParser.CondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#iter.
    def visitIter(self, ctx:compiladoresParser.IterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#if.
    def visitIf(self, ctx:compiladoresParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#else.
    def visitElse(self, ctx:compiladoresParser.ElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#prototipo.
    def visitPrototipo(self, ctx:compiladoresParser.PrototipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#arg.
    def visitArg(self, ctx:compiladoresParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#funcion.
    def visitFuncion(self, ctx:compiladoresParser.FuncionContext):
        return self.visitChildren(ctx)



del compiladoresParser