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

root.mainloop()
