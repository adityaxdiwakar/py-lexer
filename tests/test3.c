#include "stdio.h"

int main() {
    int x;
    int y;
    int max;
    scanf("%d %d",&x,&y);
    if (x > y) {
        max = x;
    } else {
        max = y;
    }
    printf("%d",max);
}

/*
DIRECTIVE
STR
INT_WORD
IDENT(main)
LBRACK

INT_WORD
IDENT(x)
SEMI
INT_WORD
IDENT(y)
SEMI
INT_WORD
IDENT(max)
SEMI

IDENT(scanf)
LPAREN
STR
COMMA
IDENT(x)
COMMA
IDENT(y)
RPAREN
SEMI

IF
LPAREN
IDENT(x)
GT
IDENT(y)
RBRACK
IDENT(max)
EQUALS
IDENT(x)
SEMI
RBRACK

ELSE
LBRACK
IDENT(max)
EQUALS
IDENT(y)
SEMI
RBRACK

IDENT(printf)
STR
COMMA
IDENT(max)
SEMI

RBRACK
*/