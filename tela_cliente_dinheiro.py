from tkinter import *

def f_tela_cliente_dinheiro():
    root = Toplevel()
    root.geometry('300x500')
    root.title('Cliente')

    #label
    label_cliente = Label(root,text = "CLIENTE")
    label_codigo = Label(root,text = "CÓDIGO:")
    label_nome = Label(root,text = "NOME:")
    label_telefone = Label(root, text ="TELEFONE:")
    label_fp = Label(root,text="FORMA\nDE PAGAMENTO", background= 'black', foreground= 'white')
    label_pc = Label(root,text = "PAGAMENTO NO\nCARTÃO")
    label_dinheiro = Label(root,text = "DINHEIRO")
    label_pix = Label(root,text = "PIX")

    #textos
    texto_codigo = Text(root,height = 0.5, width = 20)
    texto_nome = Text(root,height = 0.5, width = 20)
    texto_telefone = Text(root,height = 0.5, width = 20)

    #checkbutton
    checkPC = Checkbutton(root,text = "SIM", onvalue = 1, offvalue = 0)
    checkDINHEIRO = Checkbutton(root,text = "SIM",onvalue = 1, offvalue = 0)
    checkPIX = Checkbutton(root,text = "SIM",onvalue = 1, offvalue = 0)

    #botões
    addAE = Button(root,text ="Adicionar endereço")
    addTP = Button(root,text = "Voltar a tela pessoa")

    #posicionamento label
    label_cliente.place(relx = 0.5, rely = 0.05, anchor='center')
    label_codigo.place(relx = 0.1, rely = 0.1, anchor = 'w')
    label_nome.place(relx = 0.1, rely = 0.2, anchor = 'w')
    label_telefone.place(relx = 0.05, rely = 0.3, anchor = 'w')
    label_fp.place(relx = 0.01, rely = 0.4, anchor = 'w')
    label_pc.place(relx = 0.1, rely =0.5, anchor = 'w')
    label_dinheiro.place(relx = 0.15, rely =0.6, anchor = 'w')
    label_pix.place(relx = 0.2, rely = 0.7, anchor = 'w')

    #posicionamento textos
    texto_codigo.place(relx = 0.3, rely = 0.1 , anchor = 'w')
    texto_nome.place(relx = 0.3 , rely = 0.2 , anchor = 'w')
    texto_telefone.place(relx = 0.3, rely = 0.3 , anchor = 'w')

    #posicionamento checkbutton
    checkPC.place(relx = 0.5,rely = 0.5,anchor = 'w')
    checkDINHEIRO.place(relx = 0.5,rely = 0.6,anchor = 'w')
    checkPIX.place(relx = 0.5,rely = 0.7,anchor = 'w')

    #posicionamento botões
    addAE.place(relx= 0.5,rely= 0.8,anchor='center')
    addTP.place(relx= 0.5,rely= 0.9,anchor='center')


    root.mainloop()