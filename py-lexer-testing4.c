void someFunction() {
    int x;
    if (x > 0) {
        int y = 10;
    } else {
       int y = -10;
    }
}
/*
IDENT(someFunction)
LPAREN
RPAREN
LBRACK
IF
LPAREN
IDENT(x)
GT
INT
RPAREN
LBRACK
IDENT(y)
EQUALS
INT
SEMI
RBRACK
ELSE
LBRACK
IDENT(y)
EQUALS
SUB
INT
SEMI
RBRACK
*/