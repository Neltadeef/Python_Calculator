# Python calculator

import tkinter as tk

# Création des bouttons avec une liste sous forme (contenu, row, column)
buttons = [
    ('(', 1, 0), (')', 1, 1),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('+', 5, 2), ('=', 5, 3),
]

root = tk.Tk()
root.title("Calculatrice")
root.geometry("400x500")

# Champ d'affichage
display = tk.Entry(root, font=("Arial", 18), borderwidth=5, relief="ridge", justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def calculate():
    try:
        result = eval(display.get()) # Eval permet d'interprèter du code python. Ici il nous sert a faire des calculs
        display.delete(0, tk.END) # Réinitialise l'affichage
        display.insert(tk.END, result) # Affiche le résultat
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Erreur")

def append_text(text):
    display.insert(tk.END, text)

def clear_last():
    display.delete(display.index(tk.END)-1, tk.END)

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2, command=calculate)
    else:
        button = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2, command=lambda t=text: append_text(t)) # le mot clé lambda permet de passer des arguments lors de l'appel de la fonction
    button.grid(row=row, column=col, padx=5, pady=5)

# Bouton pour effacer
clear_button = tk.Button(root, text="<-", font=("Arial", 18), width=5, height=2, command=clear_last)
clear_button.grid(row=1, column=3, padx=5, pady=5)

root.mainloop()
