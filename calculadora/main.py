import tkinter as tk
from tkinter import ttk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")

        # Ajustando a geometria da janela
        self.root.geometry("200x300")

        # Frame para a entrada e resultado
        self.entry_frame = ttk.Frame(self.root)
        self.entry_frame.pack(fill="both", expand=True)

        # Entrada
        self.entry_var = tk.StringVar()
        self.entry = ttk.Entry(self.entry_frame, textvariable=self.entry_var, font=('Arial', 20), justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
        
        # Frame para os botões
        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(fill="both", expand=True)

        # Lista de rótulos e comandos para os botões
        buttons = [
            ("C", self.clear_all),
            ("CE", self.clear_entry),
            ("%", lambda: self.add_to_expression("%")),
            ("/", lambda: self.add_to_expression("/")),
            ("7", lambda: self.add_to_expression("7")),
            ("8", lambda: self.add_to_expression("8")),
            ("9", lambda: self.add_to_expression("9")),
            ("*", lambda: self.add_to_expression("*")),
            ("4", lambda: self.add_to_expression("4")),
            ("5", lambda: self.add_to_expression("5")),
            ("6", lambda: self.add_to_expression("6")),
            ("-", lambda: self.add_to_expression("-")),
            ("1", lambda: self.add_to_expression("1")),
            ("2", lambda: self.add_to_expression("2")),
            ("3", lambda: self.add_to_expression("3")),
            ("+", lambda: self.add_to_expression("+")),
            ("0", lambda: self.add_to_expression("0")),
            (".", lambda: self.add_to_expression(".")),
            ("=", self.calculate),
        ]

        # Criar e posicionar botões
        row = 1
        col = 0
        for (text, command) in buttons:
            button = ttk.Button(self.button_frame, text=text, command=command)
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Configurar estilo para os botões de operação
        style = ttk.Style()
        style.configure('TButton', foreground='black', background='#3CB8EA', font=('Ivy', 12))

        # Ajustando o peso das linhas e colunas para o gerenciamento de geometria grid
        self.button_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.button_frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

    def add_to_expression(self, value):
        current_expression = self.entry_var.get()
        new_expression = current_expression + value
        self.entry_var.set(new_expression)

    def calculate(self):
        try:
            result = eval(self.entry_var.get())
            self.entry_var.set(str(result))
        except Exception as e:
            self.entry_var.set("Erro")

    def clear_all(self):
        self.entry_var.set("")

    def clear_entry(self):
        current_expression = self.entry_var.get()
        new_expression = current_expression[:-1]
        self.entry_var.set(new_expression)

root = tk.Tk()
app = Calculadora(root)
root.mainloop()
