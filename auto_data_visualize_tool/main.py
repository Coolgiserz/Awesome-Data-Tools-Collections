import ast

def print_ast(node, level=0):
    indent = '  ' * level
    print(f'{indent}{node.__class__.__name__}')

    for field, value in ast.iter_fields(node):
        if isinstance(value, list):
            for item in value:
                if isinstance(item, ast.AST):
                    print_ast(item, level + 1)
        elif isinstance(value, ast.AST):
            print(f'{indent}  {field}:')
            print_ast(value, level + 2)
        else:
            print(f'{indent}  {field}: {value}')

code = """
def greet(name):
    message = f'Hello, {name}!'
    print(message)

greet('Alice')
"""

tree = ast.parse(code)
print_ast(tree)