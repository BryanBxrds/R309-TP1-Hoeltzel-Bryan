import tkinter as tk

# Création de la fenêtre principale
root = tk.Tk()
root.title("Compteur")

compteur = tk.IntVar(value=0) #tk.IntVar est une variable pour les entiers

label = tk.Label(root, textvariable=compteur, font=("Arial", 20)) # Les labels sont des sortes de fenetres
label.pack(pady=100) # pack pour afficher et pady pour la taille (padding)

# Fonction pour incrémenter
def incrementer():
    compteur.set(compteur.get() + 1)

# Fonction pour décrémenter
def decrementer():
    compteur.set(compteur.get() - 1)

# Bouton "+"
btn_plus = tk.Button(root, text="+", command=incrementer, width=10)
btn_plus.pack(pady=5)

# Bouton "-"
btn_moins = tk.Button(root, text="-", command=decrementer, width=10)
btn_moins.pack(pady=5)

# Boucle principale
root.mainloop()
