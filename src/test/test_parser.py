import unittest
from src.main.parser import parser, VarDecl, FuncDef, Param

class TestParser(unittest.TestCase):
    def test_var_decl(self):
        data = '''
        x: int
        y: float
        '''
        result = parser.parse(data)
        expected = [
            VarDecl(name='x', var_type='int'),
            VarDecl(name='y', var_type='float')
        ]
        self.assertEqual(result, expected)

    def test_func_def(self):
        data = '''
        def add(a: int, b: int) -> int:
            return a + b
        '''
        result = parser.parse(data)
        expected = [
            FuncDef(
                name='add',
                params=[
                    Param(name='a', param_type='int'),
                    Param(name='b', param_type='int')
                ],
                return_type='int',
                body=[]
            )
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
