#Programme du Puissance4
from tkinter import *

def couleur():
    """Fonction qui change la couleur de la personne qui commence"""
    #Variable
    global sym, clé
    sym+=1
    if sym%2==0:
        couleur="yellow"
    else:
        couleur="red"
    ellipse=can.create_oval(680,45,690,55,fill=couleur,outline='black')

def clic(event):
    """Fonction qui prend en compte où l'utilisateur clic pour savoir où placer son pion"""
    #Position du pointeur de la souris
    X=event.x
    Y=event.y
    #Variable
    global sym, liste, clé
    a,b=0.5,0.5
    #Fonction
    for i in range(7):
        if X>(i*100) and (X<100+i*100):
            for j in range(6):
                if Y>(j*100+100) and Y<(200+j*100):
                    a,b=(i),(j)
    if sym%2==0:
        couleur="yellow"
        couleu="red"
    else:
        couleur="red"
        couleu="yellow"
    if a!=(0.5) and b!=(0.5) and liste[6-a][4-b]==0 and (liste[6-a][3-b]==1 or (4-b)==0) and clé==0 :
        ellipse=can.create_oval(10+100*a,110+100*b,90+100*a,190+100*b,fill=couleur,outline='black')
        liste[6-a][4-b]=1
        if sym%2==0:
            ly[6-a][4-b]=1
        else:
            lr[6-a][4-b]=1
        #On efface le bouton
        Couleur.place_forget()
        ellipse=can.create_oval(680,45,690,55,fill=couleu,outline='black')
    else:
        sym-=1
    #Verification Part
    #Vertical Verif
    for j in range(7):
        for i in range(2):
            if lr[j][i]==lr[j][i+1]==lr[j][i+2]==lr[j][i+3]==1:
                gagnant(1)
            if ly[j][i]==ly[j][i+1]==ly[j][i+2]==ly[j][i+3]==1:
                gagnant(2)
    #Horizontal Verif
    for j in range(4):
        for i in range(5):
            if lr[j][i]==lr[j+1][i]==lr[j+2][i]==lr[j+3][i]==1:
                gagnant(1)
            if ly[j][i]==ly[j+1][i]==ly[j+2][i]==ly[j+3][i]==1:
                gagnant(2)
    #Diagonal
    for j in range(4):
        for i in range(2):
            if lr[j][i]==lr[j+1][i+1]==lr[j+2][i+2]==lr[j+3][i+3]==1:
                gagnant(1)
            if ly[j][i]==ly[j+1][i+1]==ly[j+2][i+2]==ly[j+3][i+3]==1:
                gagnant(2)
    for j in range(4):
        for i in range(2):
            if lr[6-j][i]==lr[5-j][i+1]==lr[4-j][i+2]==lr[3-j][i+3]==1:
                gagnant(1)
            if ly[3-j][i+3]==ly[4-j][i+2]==ly[5-j][i+1]==ly[6-j][i]==1:
                gagnant(2)
    sym+=1

def gagnant(a):
    """Fonction qui affiche le gagnant et arrête le programme"""
    global clé
    clé=1
    can.create_rectangle(25,125,675,575,fill='white',outline='black',width=2)
    txt=can.create_text(350,225,text='Gagné !!!',fill="black",font=("Arial",50))
    if a==1:
        ellipse=can.create_oval(10+100*3,110+100*2,90+100*3,190+100*2,fill='red',outline='black',width=2)
    elif a==2:
        ellipse=can.create_oval(10+100*3,110+100*2,90+100*3,190+100*2,fill='yellow',outline='black',width=2)

#Programme Principal
# Création de la fenêtre principale
fen=Tk()
fen.geometry("700x600")
fen.title("Puissance4")
can=Canvas(fen,bg="white",width=700,height=600)
can.place(x=0,y=0)

#Title
txt=can.create_text(350,50,text='Puissance 4',fill="black",font=("Arial",40))
txt=can.create_text(600,50,text='Au tour de:',fill="black",font=("Arial",10))
#Plateau
can.create_line(0,100,700,100)  #Title line
can.create_line(0,200,700,200)  #Hozintal lines
can.create_line(0,300,700,300)
can.create_line(0,400,700,400)
can.create_line(0,500,700,500)
can.create_line(0,600,700,600)
can.create_line(1,100,1,600)    #Vertical lines
can.create_line(100,100,100,600)
can.create_line(200,100,200,600)
can.create_line(300,100,300,600)
can.create_line(400,100,400,600)
can.create_line(500,100,500,600)
can.create_line(600,100,600,600)

#Variables
sym=0
clé=0
liste=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
lr=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
ly=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
compteur=0
#Bouton
Couleur=Button(fen,text='Couleur',font=20, bg='white',command=couleur)
Couleur.place(x=675,y=50, width=150, height=50, anchor=E)
#Détection des clics
can.bind("<Button-1>",clic)

#Mainloop
fen.mainloop()