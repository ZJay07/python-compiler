import ply.yacc as yacc
os.cwd
from lexer import lexer

tokens = (
    'NAME', 'NUMBER', 'ASSIGN', 'COLON', 'LPAREN', 'RPAREN', 'COMMA',
    'ARROW', 'NEWLINE', 'DEF', 'TYPE'
)
# AST Node definitions
class Node:
    pass

class VarDecl(Node):
    def __init__(self, name, var_type):
        self.name = name
        self.var_type = var_type

    def __repr__(self):
        return f"VarDecl(name={self.name}, var_type={self.var_type})"

class FuncDef(Node):
    def __init__(self, name, params, return_type, body):
        self.name = name
        self.params = params
        self.return_type = return_type
        self.body = body

    def __repr__(self):
        return f"FuncDef(name={self.name}, params={self.params}, return_type={self.return_type}, body={self.body})"

class Param(Node):
    def __init__(self, name, param_type):
        self.name = name
        self.param_type = param_type

    def __repr__(self):
        return f"Param(name={self.name}, param_type={self.param_type})"

# Parsing rules
def p_program(p):
    '''program : statement_list'''
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : var_decl
                 | func_def'''
    p[0] = p[1]

def p_var_decl(p):
    '''var_decl : NAME COLON TYPE'''
    p[0] = VarDecl(p[1], p[3])

def p_func_def(p):
    '''func_def : DEF NAME LPAREN param_list RPAREN ARROW TYPE COLON statement_list'''
    p[0] = FuncDef(p[2], p[4], p[7], p[9])

def p_param_list(p):
    '''param_list : param_list COMMA param
                  | param
                  | empty'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 2:
        if p[1] is None:
            p[0] = []
        else:
            p[0] = [p[1]]

def p_param(p):
    '''param : NAME COLON TYPE'''
    p[0] = Param(p[1], p[3])

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()

if __name__ == "__main__":
    data = '''
    x: int
    y: float
    def add(a: int, b: int) -> int:
        return a + b
    '''
    result = parser.parse(data, lexer=lexer)
    for r in result:
        print(r)
