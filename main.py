import ply.lex as lex
import tkinter as tk
from tkinter import scrolledtext, filedialog
from JuliaAnalyzer import JuliaAnalyzer

class JuliaLexer:
    tokens = ['LPAREN', 'RPAREN', 'ARGUMENT','EQUAL', 'NOT_EQUAL', 'LESS_THAN', 'LESS_THAN_EQUAL', 'GREATER_THAN', 'GREATER_THAN_EQUAL', 'EQUALS']

    # Reglas de expresiones regulares para tokens
    t_EQUAL = r'=='
    t_EQUALS = r'='
    t_NOT_EQUAL = r'!='
    t_LESS_THAN = r'<'
    t_LESS_THAN_EQUAL = r'<='
    t_GREATER_THAN = r'>'
    t_GREATER_THAN_EQUAL = r'>='
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_ARGUMENT = r'[a-zA-Z_][a-zA-Z_0-9]*'

    t_ignore = ' \t'

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        print(f"Caracter no reconocido: '{t.value[0]}'")
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def analyze_julia_code(self, code):
        self.lexer.input(code)
        result = "Análisis léxico para Julia:\n"

        while True:
            tok = self.lexer.token()
            if not tok:
                break
            result += f"Token: {tok.type}\n"

        # Verificar si hay mensajes de error en la cadena de resultados
        if "Caracter no reconocido" in result:
            result += "Error léxico en el código de Julia."

        result += "Análisis léxico exitoso para Julia."
        return result

class CodeInputApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Código")
        self.root.geometry("730x400")

        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.file_menu.add_command(label="Abrir Julia", command=self.open_file_julia)
        self.file_menu.add_command(label="Abrir Ruby", command=self.open_file_ruby)
        self.file_menu.add_command(label="Guardar Como", command=self.save_as)

        self.code_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=20)
        self.code_input.grid(row=0, column=0, padx=10, pady=10)

        self.run_button = tk.Button(root, text="Ejecutar Código", command=self.execute_code)
        self.run_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W + tk.E)

        self.console_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=20)
        self.console_output.grid(row=0, column=1, padx=10, pady=10)
        self.console_output.config(state=tk.DISABLED)

        # Inicializar el analizador léxico de Julia
        self.julia_lexer = JuliaLexer()
        self.julia_lexer.build()

    def execute_code(self):
        self.console_output.config(state=tk.NORMAL)
        self.console_output.delete("1.0", tk.END)

        code = self.code_input.get("1.0", tk.END)
        language = self.identify_language(code)

        if language == "julia":
<<<<<<< HEAD
            # Crear una instancia de JuliaAnalyzer y analizar el código
            julia_analyzer = JuliaAnalyzer()
            analyzed_tokens = julia_analyzer.analyze_code(code)

            # Mostrar los resultados en la consola
            result = f"Tokens reconocidos:\n{analyzed_tokens}"
=======
            result = self.julia_lexer.analyze_julia_code(code)
>>>>>>> f9fe885f1dcc008b387f6fe6c45a0896246538be
        elif language == "ruby":
            result = self.analyze_ruby_code(code)
        else:
            result = "Lenguaje no identificado."

        self.console_output.insert(tk.END, result)
        self.console_output.config(state=tk.DISABLED)

    def identify_language(self, code):
        if "println" in code:
            return "julia"
        elif "puts" in code:
            return "ruby"
        else:
            return "unknown"

    def open_file_julia(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos Julia", "*.jl")])
        if file_path:
            with open(file_path, "r") as file:
                code = file.read()
                self.code_input.delete("1.0", tk.END)
                self.code_input.insert(tk.END, code)
                
    def open_file_ruby(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos Ruby", "*.rb")])
        if file_path:
            with open(file_path, "r") as file:
                code = file.read()
                self.code_input.delete("1.0", tk.END)
                self.code_input.insert(tk.END, code)

    def save_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de Texto", "*.txt"),
                                                                                      ("Archivos Julia", "*.jl"),
                                                                                      ("Archivos Ruby", "*.rb")])
        if file_path:
            with open(file_path, "w") as file:
                code = self.code_input.get("1.0", tk.END)
                file.write(code)

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeInputApp(root)
    root.mainloop()