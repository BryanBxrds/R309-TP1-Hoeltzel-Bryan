from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title("Échiquier")

taille = 8 # echequier 8x8
case = 60  # taille d'une case en pixels



def dessiner_echiquier(canvas):
	for i in range(taille):
		for j in range(taille):
			# La case (i, j) est blanche si (i+j)%2 == 0, donc si i et j sont tous les deux pairs ou tous les deux impairs, sinon noire
			couleur = "white" if (i+j)%2 == 0 else "black"
			x1 = j * case
			y1 = i * case
			x2 = x1 + case
			y2 = y1 + case
			canvas.create_rectangle(x1, y1, x2, y2, fill=couleur)


canvas = tk.Canvas(root, width=taille*case, height=taille*case)
canvas.pack()

dessiner_echiquier(canvas)


############## Insertion de la reine ################


img_pil = Image.open("reine.png").resize((case, case), Image.LANCZOS)
img_reine = ImageTk.PhotoImage(img_pil)
canvas.img_reine = img_reine  # éviter probleme de dimension et permet d'interagir avec l'image

reine_id = canvas.create_image(3 * case + case//2, 0 * case + case//2, image=img_reine) # Place la reine a la postion [3,0]

selection = [False]

def coordonnees_case(event):
    return event.y // case, event.x // case

def deplacement(event):
	ligne, col = coordonnees_case(event)
	# Vérifie que la case cliquée est dans les limites de l'échiquier
	if 0 <= ligne < taille and 0 <= col < taille:
		canvas.coords(reine_id, col * case + case//2, ligne * case + case//2)

canvas.bind("<Button-1>", deplacement) # Clic gauche pour déplacer la reine // .bind pour lier un evenement a une fonction



root.mainloop()
