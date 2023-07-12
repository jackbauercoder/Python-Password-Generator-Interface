import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gerador de Senhas")

        self.length_label = tk.Label(self.root, text="Comprimento:")
        self.length_label.pack(pady=5)
        self.length_entry = tk.Entry(self.root)
        self.length_entry.pack(pady=5)

        self.password_label = tk.Label(self.root, text="Senha Gerada:")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.root, width=50)
        self.password_entry.pack(pady=5)

        self.generate_button = tk.Button(self.root, text="Gerar Senha", command=self.generate_password)
        self.generate_button.pack(pady=5)

    def generate_password(self):
        length = int(self.length_entry.get())
        if length <= 0:
            messagebox.showerror("Erro", "O comprimento da senha deve ser maior que zero.")
            return

        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(tk.END, password)

if __name__ == "__main__":
    password_generator = PasswordGenerator()
    password_generator.root.mainloop()
