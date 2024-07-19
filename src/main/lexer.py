import ply.lex as lex

# List of token names
tokens = (
    'NAME', 'NUMBER', 'ASSIGN', 'COLON', 'LPAREN', 'RPAREN', 'COMMA',
    'ARROW', 'NEWLINE', 'DEF', 'TYPE'
)

# Regular expression rules for simple tokens
t_ASSIGN = r'='
t_COLON = r':'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_ARROW = r'->'

# Keyword mapping
keywords = {
    'def': 'DEF'
}

# Token definitions
def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = keywords.get(t.value, 'NAME')
    return t

def t_TYPE(t):
    r'int|float|str|bool'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.type = 'NEWLINE'
    return t

# Ignored characters
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

if __name__ == "__main__":
    data = '''
    x: int
    y: float
    def add(a: int, b: int) -> int:
        return a + b
    '''
    lexer.input(data)
    for tok in lexer:
        print(tok)
