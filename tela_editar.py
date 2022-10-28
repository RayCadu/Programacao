from msilib.schema import ComboBox
from tkinter import *
from tkinter.ttk import Combobox
def f_tela_editar():
    root = Toplevel()
    root.geometry('300x500')
    root.title('Editar')

    #label
    label_editar = Label(root, text="EDITAR",background='black',foreground='white')
    label_cliente = Label(root, text="CLIENTE:")
    label_produto = Label(root, text="PRODUTO:")
    label_entregador = Label(root,text="ENTREGADOR:")

    #checkbutton

    checkC = Checkbutton(root, text="SIM",onvalue=1,offvalue=0)
    checkP = Checkbutton(root, text="SIM",onvalue=1,offvalue=0)
    checkE = Checkbutton(root, text="SIM",onvalue=1,offvalue=0)

    #combobox

    cpe = StringVar()
    ComboBoxCPE = Combobox(root,textvariable = cpe ,height= 0.5 , width= 20)

    #botão
    addEI = Button(root,text="Editar informações")
    addM = Button(root,text="Voltar ao menu",command=root.destroy)

    #posicionamento label

    label_editar.place(relx= 0.5,rely= 0.1,anchor='center')
    label_cliente.place(relx= 0.35,rely= 0.2,anchor='center')
    label_produto.place(relx= 0.33,rely= 0.3,anchor='center')
    label_entregador.place(relx= 0.3,rely= 0.4,anchor='center')

    #posicionamento checkbutton

    checkC.place(relx=0.6,rely=0.2,anchor='center')
    checkP.place(relx=0.6,rely=0.3,anchor='center')
    checkE.place(relx=0.6,rely=0.4,anchor='center')

    #posicionamento combobox
    ComboBoxCPE.place(relx= 0.5,rely= 0.5,anchor='center')

    #posicionamento botão
    addEI.place(relx=0.5,rely=0.7,anchor='center')
    addM.place(relx=0.5,rely=0.8,anchor='center')

    root.mainloop()