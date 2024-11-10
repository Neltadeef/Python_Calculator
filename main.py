# Python calculator

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Calculatrice")
root.geometry("300x400")

num1_var = tk.StringVar()
num2_var = tk.StringVar()
operator_var = tk.StringVar()

def calculate():
    try:
        num1 = float(num1_var.get())
        num2 = float(num2_var.get())
        operator = operator_var.get()

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2
        else:
            messagebox.showerror("Erreur", "Opérateur invalide")
            return

        result_label.config(text=f"Résultat: {round(result, 3)}")

    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des nombres valides")

tk.Label(root, text="Premier nombre :").pack()
tk.Entry(root, textvariable=num1_var).pack()

tk.Label(root, text="Opérateur (+, -, *, /) :").pack()
tk.Entry(root, textvariable=operator_var).pack()

tk.Label(root, text="Deuxième nombre :").pack()
tk.Entry(root, textvariable=num2_var).pack()

tk.Button(root, text="Calculer", command=calculate).pack()

result_label = tk.Label(root, text="Résultat : ")
result_label.pack()

root.mainloop()
