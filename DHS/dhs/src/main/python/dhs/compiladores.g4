grammar compiladores;

fragment LETRA : [A-Za-z] ;
fragment DIGITO : [0-9] ;

//INST : (LETRA | DIGITO | [- ,;{}()+=>] )+ '\n'; es una letra, un digito .. no quiero que exceda el guion 
PA: '(';
PC: ')';
LLA: '{';
LLC: '}';
PYC: ';';
SUMA : '+';
RESTA : '-';
MULT : '*';
DIV : '/';
MOD : '%';  

MAYOR : '>';
MAYOREQ : '>=';
MENOREQ : '<=';
MENOR : '<';
IGUAL : '==';
AND : '&&';
OR : '||';

WHILE :'while';
NUMERO : DIGITO+ ;

INT:'int';
CHAR:'char';
FLOAT:'float';
BOOLEAN:'bool';
DOUBLE:'double';



FOR: 'for';
ASIG: '=';

WS : [ \t\n\r] -> skip;
ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;
/*OTRO : . ;


s : ID     {print("ID ->" + $ID.text + "<--") }         s
  | NUMERO {print("NUMERO ->" + $NUMERO.text + "<--") } s
  | OTRO   {print("Otro ->" + $OTRO.text + "<--") }     s
  | EOF
  ;
  */

//si : s EOF; que comience en un nodo, que sea solo la razi del arbol
//s: PA s PC s  s permite la anidacion, se cierra un parentesis y se puede abrirotro parentesis. Verifica balance de parentesis
  //|
//;

programa : instrucciones EOF ; //secuencia de instrucciones hasta el final del archivo

instrucciones : instruccion instrucciones //es una instruccion con mas instrucciones 
                |
                ;
instruccion: declaracion
            | iwhile
            //| ifor
            | bloque
            | asignacion PYC
            ;

declaracion: INT ID PYC
            | CHAR ID PYC
            | DOUBLE ID PYC
            | BOOLEAN ID PYC
            | FLOAT ID PYC ;

asignacion: ID ASIG opal ;

opal: comp;  //completar una operacion aridmeticas, buscar en cppreference, agregamoss operaciones relacionales
    
comp: exp c;

c : MAYOR exp c
  | MENOR exp c
  | MENOREQ exp c
  | MAYOREQ exp c
  | IGUAL exp c
  |
  ;
  
exp : term e ; //e es una expresion prima

term : factor t; //t es termino prima, es una multiplicacion y viene un factor

e : SUMA term e // a partir del segundo termino
  | RESTA term e
  | //regla vacia 
  ;


t :   MULT factor t  //esto aplica jerarquia, multipliaciones se hacen antes, hacen que este por debajo en el arbol
    | DIV factor t
    | MOD factor t
    |
    ;
factor : NUMERO  //parentesis se convierte en factor
      | ID
      | PA exp PC
      ;

iwhile : WHILE PA ID PC instruccion ;//llave representa una instruccion compuesta, despues del while viene siempre una instruccion

bloque : LLA instrucciones LLC; 

//ifor : FOR PA init PYC cond PYC iter PC instruccion;

