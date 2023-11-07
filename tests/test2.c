#include "stdio.h"

int main() {
    float a = 10.0;
    float b = 4.0;
    return a / b;
}

/*
DIRECTIVE
STR(stdio.h)
INT_WORD
IDENT(main)
LBRACK

FLOAT_WORD
IDENT(a)
EQUALS
FLOAT
SEMI

FLOAT_WORD
IDENT(b)
EQUALS
FLOAT
SEMI

RETURN
IDENT(a)
DIV
IDENT(b)
SEMI
RBRACK
*/