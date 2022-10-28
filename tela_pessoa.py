#tamanho padrão 300x500


from tkinter import *
from tela_endereco import f_endereco

def f_tela_pessoa():
    root = Toplevel()
    root.geometry('300x500')
    root.title('Pessoa')
    #botões
    addM = Button(root, text='Voltar ao menu',command = root.destroy)
    addE = Button(root,text='Adicionar endereço', command= f_endereco)
    #label
    label_pessoa = Label(root,text ="PESSOA")
    label_nome = Label(root,text="NOME:")
    label_tel = Label(root,text="TELEFONE:")
    label_cpf = Label(root,text="CPF:")
    label_cliente = Label(root,text='CLIENTE')
    label_entregador = Label(root,text="ENTREGADOR")
    #textos
    texto_nome = Text(root, height = 0.5, width = 20)
    texto_tel = Text(root, height = 0.5, width = 20)
    texto_cpf = Text(root, height = 0.5, width = 20)

    #checkbutton
    checkC = Checkbutton(root,text= "SIM")
    checkE = Checkbutton(root,text = "SIM")

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
