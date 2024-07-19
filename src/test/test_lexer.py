import unittest
from src.main.lexer import lexer

class TestLexer(unittest.TestCase):
    def test_tokens(self):
        data = '''
        x: int
        y: float
        def add(a: int, b: int) -> int:
            return a + b
        '''
        lexer.input(data)
        tokens = [(tok.type, tok.value) for tok in lexer]
        expected_tokens = [
            ('NAME', 'x'), ('COLON', ':'), ('TYPE', 'int'), ('NEWLINE', '\n'),
            ('NAME', 'y'), ('COLON', ':'), ('TYPE', 'float'), ('NEWLINE', '\n'),
            ('DEF', 'def'), ('NAME', 'add'), ('LPAREN', '('), ('NAME', 'a'), ('COLON', ':'),
            ('TYPE', 'int'), ('COMMA', ','), ('NAME', 'b'), ('COLON', ':'), ('TYPE', 'int'),
            ('RPAREN', ')'), ('ARROW', '->'), ('TYPE', 'int'), ('COLON', ':'), ('NEWLINE', '\n')
        ]
        self.assertEqual(tokens[:20], expected_tokens)

if __name__ == "__main__":
    unittest.main()
