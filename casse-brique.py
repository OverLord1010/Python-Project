import tkinter as tk

# Variables globales
LARGEUR, HAUTEUR = 600, 600
x1, y1 = 300, 500  # coordonnees initiales
dx, dy = 15, 0   # 'pas' du deplacement
flag =0          # indicateur de mouvement modifié par start_it et stop_it

def move():
    "deplacement de la balle"
    global x1, y1, dx, dy, flag
    x1, y1 = x1 +dx, y1 + dy
    if x1 >590:
        dx, dy = dx*-1, dy*-1
    if y1 >600:
        dx, dy = dx*-1, dy*-1
    if x1 <10:
        dx, dy = dx*-1, dy*-1
    if y1 <10:
        dx, dy = dx*-1, dy*-1
    c.coords(balle, x1, y1, x1 + 30, y1 + 30)

    # On gère le mouvement en rappelant la fonction move après 50 ms
    if flag >0:
        c.after(50,move)

def start_it():
    """demarrage de l'animation"""
    global flag
    if flag ==0:
        # pour ne lancer qu'une seule boucle
        flag =1
        move()

#========== Programme principal =============

# Création de la fenêtre principale (main window)
fen1 = tk.Tk()
fen1.title('Balle')

# Création d'un widget Canvas (zone graphique)
c = tk.Canvas(fen1, width = LARGEUR, height = HAUTEUR, bg = 'black')
c.pack(side = tk.LEFT, padx = 5, pady =5 )

# Creation de la balle. On memorise ici son nom, c'est important !!
balle = c.create_oval(x1, y1, x1 + 30, y1 + 30, width = 2, fill = 'green', outline = 'white')

tk.Button(fen1,text='Quitter', width = 8, command=fen1.destroy).pack(side=tk.BOTTOM)
tk.Button(fen1, text='Demarrer', width = 8, command=start_it).pack()

# demarrage du receptionnaire d'evenements (boucle principale) :
fen1.mainloop()