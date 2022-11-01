#tamanho padrão 300x500


from sre_parse import State
from tkinter import *
from tela_endereco import f_endereco

def f_teste(root):
    for i in root.winfo_children():
        if(type(i) == type(Checkbutton())):
            print(i.instate(['alternate']))

def f_teste2(var, ch):
    print(var.get())
    if(var.get() == 1):
        ch.config(state= DISABLED)
    else:
        ch.config(state= NORMAL)

def f_tela_pessoa():
    root = Toplevel()

    root.geometry('300x500')
    root.title('Pessoa')
    #botões
    addM = Button(root, text='Voltar ao menu',command = root.destroy)
    addE = Button(root,text='Adicionar endereço', command=lambda: f_teste(root))
    #label
    label_pessoa = Label(root,text ="PESSOA")
    label_nome = Label(root,text="NOME:")
    label_tel = Label(root,text="TELEFONE:")
    label_cpf = Label(root,text="CPF:")
    label_cliente = Label(root,text='CLIENTE')
    label_entregador = Label(root,text="ENTREGADOR")
    #textos
    nome = StringVar()
    texto_nome = Entry(root, textvariable = nome, width=20)
    tel = StringVar()
    texto_tel = Entry(root, textvariable = tel, width=20)
    cpf = StringVar()
    texto_cpf = Entry(root, textvariable = cpf, width=20)

    #checkbutton
    var1 = IntVar()
    checkE = Checkbutton(root,text = "SIM",onvalue=1,offvalue=0,variable=var1, command=lambda: f_teste2(var1, checkC))
    checkC = Checkbutton(root,text= "SIM",onvalue=1,offvalue=0, variable=var1, command=lambda: f_teste2(var1, checkE))
    

    #posicionamento textos
    texto_nome.place(relx = 0.4, rely = 0.2, anchor = 'w')
    texto_tel.place(relx = 0.4, rely = 0.3, anchor = 'w')
    texto_cpf.place(relx = 0.4, rely =0.4, anchor = 'w')

    #posicionamento Label
    label_pessoa.place(relx = 0.5, rely = 0.1, anchor = 'n')
    label_nome.place(relx = 0.2, rely = 0.2, anchor = 'w')
    label_tel.place(relx = 0.14, rely = 0.3, anchor = 'w')
    label_cpf.place(relx = 0.25, rely = 0.4, anchor = 'w')
    label_cliente.place(relx = 0.2, rely = 0.5, anchor ='w')
    label_entregador.place(relx = 0.1, rely = 0.6, anchor = 'w')

    #posicionamento botões
    addE.place(relx = 0.5, rely = 0.83, anchor = 'center')
    addM.place(relx = 0.5, rely = 0.93, anchor = 'center')

    #posicionamento checkbutton
    checkC.place(relx = 0.6, rely = 0.5, anchor = 'center')
    checkE.place(relx= 0.6, rely = 0.6, anchor = 'center')

    root.mainloop()
