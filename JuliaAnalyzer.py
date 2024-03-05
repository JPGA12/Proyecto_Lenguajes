from ply import lex

class JuliaAnalyzer:
    def __init__(self):
        # Crear el lexer
        self.lexer = lex.lex(module=self)

    # Lista de tokens
    tokens = (
        'IDENTIFIER',
        'NUMBER',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'LPAREN',
        'RPAREN',
        'NEWLINE',
        'HASHTAG',
        'EQUALS',   
        'QUOTE',    
        'COLON',    
        'DOLLAR',   
        'COMMA',  
        'POINTS',
    )

    # Definición de patrones para cada token
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_POINTS = r'.'

     # Nueva regla para reconocer '.'
    def t_POINTS(self, t):
        r'.'
        return t

    # Nueva regla para reconocer '#'
    def t_HASHTAG(self, t):
        r'\#'
        return t

    # Nueva regla para reconocer '='
    def t_EQUALS(self, t):
        r'='
        return t

    # Nueva regla para reconocer '"'
    def t_QUOTE(self, t):
        r'"'
        return t

    # Nueva regla para reconocer ':'
    def t_COLON(self, t):
        r':'
        return t

    # Nueva regla para reconocer '$'
    def t_DOLLAR(self, t):
        r'\$'
        return t

    # Nueva regla para reconocer ','
    def t_COMMA(self, t):
        r','
        return t

    # Ignorar espacios y tabulaciones
    t_ignore = ' \t'

    # Definir un token para identificadores (métodos y atributos)
    def t_IDENTIFIER(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        return t

    # Definir un token para números
    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    # Definir un token para saltos de línea
    def t_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        return t

    # Manejar errores de tokens no reconocidos
    def t_error(self, t):
        print(f"Error: Caracter no reconocido '{t.value[0]}' en la línea {t.lineno}")
        t.lexer.skip(1)

    # Método para analizar un código de Julia
    def analyze_code(self, julia_code):
        # Configurar el lexer
        self.lexer.input(julia_code)

        # Lista para almacenar los tokens reconocidos
        tokens = []

        # Obtener y almacenar los tokens
        for token in self.lexer:
            tokens.append(token)

        return tokens

