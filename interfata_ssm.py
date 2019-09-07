from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import sys
from cilindru_script import moment_de_inertie


def get_iesire(event):
    quit()

def get_executa(event):
    #arbore
    phi4 = fi4.get()
    phi3 = fi3.get()
    l1 = L1.get()
    l2 = L2.get()
    ro2 = Ro2.get()
    
    phi4 = float(phi4)
    phi3 = float(phi3)
    l1 = float(l1)
    l2 = float(l2)
    ro2 = float(ro2)

    #arborele este format din "varf" si "corp"
    varf_arbore = moment_de_inertie(phi3, l2, ro2, 0)
    ax_arbore = moment_de_inertie(phi4, l1-l2-l2, ro2, 0)
    arbore = []
    arbore.append(ax_arbore[0]+varf_arbore[0]+varf_arbore[0])
    arbore.append(ax_arbore[1]+varf_arbore[1]+varf_arbore[1])
    arbore.append(ax_arbore[2]+varf_arbore[2]+varf_arbore[2])
    Label(root, text = str(arbore[0])).place(x = 400,y = 200)
    Label(root, text = str(arbore[1])).place(x = 400,y = 230)
    Label(root, text = str(arbore[2])).place(x = 475,y = 260)

    #bucsa este formata din "baza", "top", 2 "gauri mici" si o "gaura mare"
    phi1 = fi1.get()
    phi4 = fi4.get()
    phi5 = fi5.get()
    phi6 = fi6.get()
    l3 = L3.get()
    l4 = L4.get()
    ro1 = Ro1.get()

    phi1 = float(phi1)
    phi4 = float(phi4)
    phi5 = float(phi5)
    phi6 = float(phi6)
    l3 = float(l3)
    l4 = float(l4)
    ro1 = float(ro1)

    baza_bucsa = moment_de_inertie(phi1,l4,ro1, 0)
    top_bucsa = moment_de_inertie(phi5, l3-l4, ro1, 0)
    gaura_mica = moment_de_inertie(phi6, l4,ro1, 0)
    gaura_baza = moment_de_inertie(phi4, l4, ro1, 0)
    gaura_mare = moment_de_inertie(phi4, l3-l4, ro1, 0)
    bucsa = []
    bucsa.append(baza_bucsa[0]+top_bucsa[0]-gaura_mica[0]-gaura_mica[0]-gaura_baza[0]-gaura_mare[0])
    bucsa.append(baza_bucsa[1]+top_bucsa[1]-gaura_mica[1]-gaura_mica[1]-gaura_baza[1]-gaura_mare[1])
    bucsa.append(baza_bucsa[2]+top_bucsa[2]-gaura_mica[2]-gaura_mica[2]-gaura_baza[2]-gaura_mare[2])
    Label(root, text = str(bucsa[0])).place(x = 400,y = 290)
    Label(root, text = str(bucsa[1])).place(x = 400,y = 320)
    Label(root, text = str(bucsa[2])).place(x = 475,y = 350)

    #piesa este format din "arbore" si "bucsa"
    piesa = []
    piesa.append(arbore[0]+bucsa[0])
    piesa.append(arbore[1]+bucsa[1])
    piesa.append(arbore[2]+bucsa[2])
    Label(root, text = str(piesa[0])).place(x = 400,y = 380)
    Label(root, text = str(piesa[1])).place(x = 400,y = 410)
    Label(root, text = str(piesa[2])).place(x = 475,y = 440)
    
root = Tk()
#initializare interfata grafica
root.title('Interfata SSM')
root.geometry('1200x600')
root.resizable(width = False, height = False)

style=ttk.Style()
style.configure('TButton',
                font = 'Serif 15',
                padding = 10)

#incarcare imagini in aplicatie
load1 = Image.open("Logo_UPB.png")
render = ImageTk.PhotoImage(load1)
img = Label(image=render)
img.image = render
img.place(x=0, y=0)

load2 = Image.open("Logo_FIMM.png")
render = ImageTk.PhotoImage(load2)
img = Label(image=render)
img.image = render
img.place(x=1080, y=0)

load3 = Image.open("piesa_i.jpg")
render = ImageTk.PhotoImage(load3)
img = Label(image=render)
img.image = render
img.place(x=750, y=170)

#pozitionarea etichetelor si a campurilor aferente in interfata grafica
Label(root, text = 'Phi1: ').place(x = 0,y = 200)
fi1 = Entry(root)
fi1.place(x=50, y = 200)

Label(root, text = 'Phi2: ').place(x = 0,y = 230)
fi2 = Entry(root)
fi2.place(x=50, y = 230)

Label(root, text = 'Phi3: ').place(x = 0,y = 260)
fi3 = Entry(root)
fi3.place(x=50, y = 260)

Label(root, text = 'Phi4: ').place(x = 0,y = 290)
fi4 = Entry(root)
fi4.place(x=50, y = 290)

Label(root, text = 'Phi5: ').place(x = 0,y = 320)
fi5 = Entry(root)
fi5.place(x=50, y = 320)

Label(root, text = 'Phi6: ').place(x = 0,y = 350)
fi6 = Entry(root)
fi6.place(x=50, y = 350)

Label(root, text = 'L1: ').place(x = 0,y = 380)
L1 = Entry(root)
L1.place(x=50, y = 380)

Label(root, text = 'L2: ').place(x = 0,y = 410)
L2 = Entry(root)
L2.place(x=50, y = 410)

Label(root, text = 'L3: ').place(x = 0,y = 440)
L3 = Entry(root)
L3.place(x=50, y = 440)

Label(root, text = 'L4: ').place(x = 0,y = 470)
L4 = Entry(root)
L4.place(x=50, y = 470)

Label(root, text = 'ro1: ').place(x = 0,y = 500)
Ro1 = Entry(root)
Ro1.place(x=50, y = 500)

Label(root, text = 'ro2: ').place(x = 0,y = 530)
Ro2 = Entry(root)
Ro2.place(x=50, y = 530)

Label(root, text = 'REZULTATE').place(x = 300,y = 170)
Label(root, text = 'ARBORE - masa:  ').place(x = 300,y = 200)
Label(root, text = 'ARBORE - volum: ').place(x = 300,y = 230)
Label(root, text = 'ARBORE - moment de inertie:').place(x = 300,y = 260)
Label(root, text = 'BUCSA - masa: ').place(x = 300,y = 290)
Label(root, text = 'BUCSA - volum: ').place(x = 300,y = 320)
Label(root, text = 'BUCSA - moment de inertie: ').place(x = 300,y = 350)
Label(root, text = 'PIESA - masa: ').place(x = 300,y = 380)
Label(root, text = 'PIESA - volum: ').place(x = 300,y = 410)
Label(root, text = 'PIESA - moment de inertie: ').place(x = 300,y = 440)

#fiecare buton corespunde unei functii:
buton_executa = ttk.Button(root,text = 'EXECUTA')
buton_executa.bind('<Button-1>',get_executa)
buton_executa.place(x = 400, y = 50)

buton_iesire = ttk.Button(root,text = 'IESIRE')
buton_iesire.bind('<Button-1>',get_iesire)
buton_iesire.place(x = 600, y = 50)


Label(root, text = 'ISAILA GABRIEL').place(x = 500,y = 550)
