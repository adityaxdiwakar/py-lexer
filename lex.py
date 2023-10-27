from sys import stdin

def get_char():
    for line in stdin:
        for char in line:
            yield char

gen = get_char()

# tokens
INT_WORD    = "INT_WORD"
FLOAT_WORD  = "FLOAT_WORD"
INT         = "INT"
FLOAT       = "FLOAT"
STR         = "STR"
IDENT       = "IDENT"
WHILE       = "WHILE"
NEQ         = "NEQ"
MINEQ       = "MINEQ"
PLUSEQ      = "PLUSEQ"
LBRACK      = "LBRACK"
RBRACK      = "RBRACK"
LPAREN      = "LPAREN"
RPAREN      = "RPAREN"
RETURN      = "RETURN"
SEMI        = "SEMI"
IF          = "IF"
PLUS        = "PLUS"
SUB         = "SUB"
MINUS       = "MINUS"
MULT        = "MULT"
DIV         = "DIV"
EQUALS      = "EQUALS"
NOT         = "NOT"
COMMA       = "COMMA"
GT          = "GT"
LT          = "LT"
DIRECTIVE   = "DIRECTIVE"
ANDREF      = "ANDREF"

LANG_NUMBERS = list(map(str, range(0, 10)))
LANG_NUMBERS_FLOAT = LANG_NUMBERS + ["."]

LANG_FIRST_LETTER_IDENT = [chr(a) for a in list(range(65, 91)) + list(range(97, 123))] + ["#"]
LANG_IDENT = LANG_FIRST_LETTER_IDENT + ["_"] + LANG_NUMBERS
LANG_RESERVED = ["int", "float", "while", "if", "return"]
LANG_PAIRS = ["(", ")", "{", "}"]
LANG_OPERATORS = ["&", "!", "-", "+", "=", "/", "*", ">", "<"]

class Token():
    def __init__(self, t_type, value=None):
        self.t_type = t_type
        self.value = value

    def __str__(self):
        if self.value:
            return f"{self.t_type}({self.value})"
        return self.t_type

# if first character is a letter, keep consuming until illegal
buffer = ""
tokens = []
ident_flag = False 
numerical_flag = False
str_flag = False
for character in gen:
    # start string consuming procedure
    if not str_flag and character == '"':
        str_flag = True
    elif str_flag:
        if character != '"':
            buffer += character
        else:
            str_flag = False
            tokens.append(Token(STR, buffer))
            buffer = ""

    if not str_flag:
        if not ident_flag and character in LANG_FIRST_LETTER_IDENT:
            ident_flag = True
            buffer += character
        elif ident_flag and character in LANG_IDENT:
            buffer += character
        elif ident_flag:
            if "#" in buffer:
                tokens.append(Token(DIRECTIVE, buffer[1:]))
            elif buffer not in LANG_RESERVED:
                tokens.append(Token(IDENT, buffer))
            else:
                if buffer == "int": tokens.append(Token(INT_WORD))
                elif buffer == "float": tokens.append(Token(FLOAT_WORD))
                elif buffer == "while": tokens.append(Token(WHILE))
                elif buffer == "if": tokens.append(Token(IF))
                elif buffer == "return": tokens.append(Token(RETURN))
            ident_flag = False
            buffer = ""

    if not str_flag and not ident_flag:
        if not numerical_flag and character in LANG_NUMBERS:
            buffer += character
            numerical_flag = True
        elif numerical_flag:
            if character in LANG_NUMBERS_FLOAT:
                buffer += character
            else:
                if "." in buffer: tokens.append(Token(FLOAT, buffer))
                else: tokens.append(Token(INT, buffer))
                numerical_flag = False
                buffer = ""


    if not str_flag:
        if character == ";": tokens.append(Token(SEMI))
        if character == ",": tokens.append(Token(COMMA))

        if character in LANG_OPERATORS:
            if character == "+": tokens.append(Token(PLUS))
            if character == "-": tokens.append(Token(SUB))
            if character == "*": tokens.append(Token(MULT))
            if character == "/": tokens.append(Token(DIV))
            if character == "!": tokens.append(Token(NOT))
            if character == "=": tokens.append(Token(EQUALS))
            if character == ">": tokens.append(Token(GT))
            if character == "<": tokens.append(Token(LT))
            if character == "&": tokens.append(Token(ANDREF))

        if character in LANG_PAIRS: 
            if character == "(": tokens.append(Token(LPAREN))
            if character == ")": tokens.append(Token(RPAREN))
            if character == "{": tokens.append(Token(LBRACK))
            if character == "}": tokens.append(Token(RBRACK))
            ident_flag = False
            buffer = ""


for token in tokens: print(token)
