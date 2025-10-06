import tkinter as tk


root = tk.Tk()
root.title("Email")

tk.Label(root, text="Entrez votre adresse email :", font=("Arial", 14)).pack(pady=10)

# Fonction pour verifier la conformatié du mail 
def email_validation(email):
    return (
        "@" in email
        and "." in email
        and " " not in email
    )

def valide(*args):  #Fonction pour gerer le bouton validé 
    email = email_var.get()
    if email_validation(email):
        bouton_valide.config(state="normal")
        info_label.config(fg="green", text="Adresse valide")
    else:
        bouton_valide.config(state="disabled")
        info_label.config(fg="red", text="Adresse invalide")

def fermeture():  #Fonction pour fermer la fenetre et afficher le mail dans la console
    print(email_var.get())
    root.destroy()


email_var = tk.StringVar() #tk.stringvar est une variable pour le texte (chaine de caractere)
email_var.trace_add('write', valide) #trace_add pour surveiller les changements de la variable (afin de gerer le bouton validé)

entry = tk.Entry(root, textvariable=email_var, font=("Arial", 14), width=30)  #tk.Entry pour creer un formulaire dont le contenue est identifié par la variable email_var
entry.pack(pady=5)
entry.focus() #focus pour que le curseur soit dans le formulaire

info_label = tk.Label(root, text="Adresse invalide", fg="red", font=("Arial", 12))  #Message par default invalide)
info_label.pack(pady=5)

bouton_valide = tk.Button(root, text="Valider", font=("Arial", 14), state="disabled", command=fermeture) #Bouton validé desactivé par default et appelle la fonction fermeture
bouton_valide.pack(pady=20)

root.mainloop()