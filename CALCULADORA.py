from tkinter import*

raiz = Tk()
raiz.title("¨CAL-P¨")
raiz.geometry("350x400")

frame = Frame(raiz,bg="#040")
frame.config(width="600px",height="300px")
frame.pack(fill="both",expand=1)
titulo = Label(frame,text="Calculadora Perrona")
titulo.pack(side=TOP)
n1 = StringVar()
n2= StringVar()
r= StringVar()

def sumar():
   r.set(float(n1.get())+float(n2.get()))
   
def resta():
   r.set(float(n1.get())-float(n2.get()))
   
def multiplicar():
       r.set(float(n1.get())*float(n2.get()))
     
def divide():
       r.set(float(n1.get())/float(n2.get()))
   
def borrar():
     n1.set(" ")
     n2.set(" ")
     r.set(" ")
   
lbl_numeroa = Label(raiz, text="Numero A").place(relx=0.2,rely=0.2)

entrada_numeroaa = Entry(raiz,textvariable=n1).place(relx=0.4,rely=0.2)

lbl_numerob = Label(raiz, text="Numero B").place(relx=0.2,rely=0.3)

entrada_numerobb = Entry(raiz,textvariable=n2).place(relx=0.4,rely=0.3)

lbl_resultado = Label(raiz, text="Resultado").place(relx=0.2,rely=0.4)

entrada_resultadoo = Entry(raiz,textvariable=r).place(relx=0.4,rely=0.4)

rbt_suma = Button(raiz, text="     +     ",command=sumar).place(relx=0.2,rely=0.5)

rbt_mult = Button(raiz, text="     X     ",command=multiplicar).place(relx=0.4,rely=0.5)

rbt_borrar = Button(raiz, text="     C     ",command=borrar,width=5, height=4).place(relx=0.6,rely=0.5)

rbt_div = Button(raiz, text="     /     ", command=divide).place(relx=0.2,rely=0.6)

rbt_rest = Button(raiz, text="     -     ",command=resta).place(relx=0.4,rely=0.6)

raiz.mainloop()
