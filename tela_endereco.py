from cgitb import text
from tkinter import *
from tkinter.ttk import Combobox

def f_endereco():
    root = Toplevel()
    root.geometry('300x500')
    root.title('ENDEREÇO')

    #label
    label_endereco = Label(root, text= "ENDEREÇO",background='orange')
    label_cc = Label(root, text = "CÓDIGO CLIENTE:",background='black', foreground='white')
    label_nm = Label(root, text = "NOME DO CLIENTE:",background='black', foreground='white')
    label_tl = Label(root, text = "TIPO\nLOGRADOURO:",background='black', foreground='white')
    label_logradouro = Label(root, text = "LOGADOURO:",background='black', foreground='white')
    label_numero = Label(root, text = "NÚMERO:",background='black', foreground='white')
    label_cep = Label(root, text = "CEP:",background='black', foreground='white')
    label_bairro = Label(root, text = "BAIRRO:",background='black', foreground='white')
    label_cidade = Label(root, text = "CIDADE:",background='black', foreground='white')

    #texto 
    cc = StringVar()
    texto_cc = Entry(root,textvariable = cc, width= 20)
    nm = StringVar()
    texto_nm = Entry(root,textvariable = nm, width=20)
    logradouro = StringVar()
    texto_logradouro = Entry(root, textvariable = logradouro, width=20)
    numero = StringVar()
    texto_numero = Entry(root, textvariable = numero, width=20)
    cep = StringVar()
    texto_cep = Entry(root, textvariable = cep, width=20)

    #combobox
    boxtl = StringVar()
    comboBoxTl = Combobox(root,textvariable = boxtl ,height= 0.5 , width= 20)
    boxcidade = StringVar()
    comboBoxCidade = Combobox(root,textvariable = boxcidade ,height= 0.5 , width= 20)
    boxbairro = StringVar()
    comboBoxBairro = Combobox(root,textvariable = boxbairro ,height= 0.5 , width= 20)

    #botão
    addE = Button(root, text ="Cadastrar pessoa")
    btnVoltar = Button(root, text="Voltar para\ntela pessoa", command= root.destroy)

    #posicionamento label
    label_endereco.place(relx = 0.5,rely = 0.025,anchor = 'center')
    label_cc.place(relx = 0.08,rely = 0.1,anchor = 'w')
    label_nm.place(relx= 0.05,rely= 0.15,anchor='w')
    label_tl.place(relx= 0.13,rely= 0.3,anchor= 'w')
    label_logradouro.place(relx= 0.15,rely= 0.4,anchor= 'w')
    label_numero.place(relx=0.23,rely= 0.5,anchor='w')
    label_cep.place(relx = 0.32, rely= 0.6,anchor ='w')
    label_bairro.place(relx = 0.25, rely= 0.7, anchor='w')
    label_cidade.place(relx= 0.25 ,rely= 0.8,anchor= 'w')

    #posicionamento texto
    texto_cc.place(relx= 0.5,rely= 0.1,anchor = 'w')
    texto_nm.place(relx= 0.5,rely= 0.15,anchor = 'w')
    texto_logradouro.place(relx= 0.5,rely= 0.4,anchor ='w')
    texto_numero.place(relx= 0.5,rely= 0.5,anchor ='w')
    texto_cep.place(relx= 0.5,rely= 0.6,anchor ='w')


    #posicionamento botão

    addE.place(relx= 0.5, rely= 0.85, anchor='center')
    btnVoltar.place(relx= 0.5, rely= 0.95, anchor='center')
    #posicionameto 
    comboBoxTl.place(relx=0.5 ,rely=0.3 ,anchor= 'w')
    comboBoxCidade.place(relx= 0.5,rely=0.8 ,anchor= 'w')
    comboBoxBairro.place(relx= 0.5,rely=0.7 ,anchor= 'w')




    root.mainloop()
