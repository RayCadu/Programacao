#tamanho padrão 300x500


from tkinter import *

root = Tk()
root.geometry('300x500')
root.title('Pessoa')
#botões
addP = Button(root, text ='Cadastrar')
addM = Button(root, text='Voltar ao menu')
addE = Button(root,text='Adicionar endereço')
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

#posicionamento textos
texto_nome.place(relx = 0.4, rely = 0.2, anchor = 'w')
texto_tel.place(relx = 0.4, rely = 0.3, anchor = 'w')
texto_cpf.place(relx = 0.4, rely =0.4, anchor = 'w')

#posicionamento Label
label_pessoa.place(relx = 0.5, rely = 0.1, anchor = 'n')
label_nome.place(relx = 0.2, rely = 0.2, anchor = 'w')
label_tel.place(relx = 0.11, rely = 0.3, anchor = 'w')
label_cpf.place(relx = 0.25, rely = 0.4, anchor = 'w')
label_cliente.place(relx = 0.2, rely = 0.5, anchor ='w')
label_entregador.place(relx = 0.1, rely = 0.6, anchor = 'w')

#posicionamento botões
addP.place(relx = 0.5, rely = 0.73, anchor = 'center')
addE.place(relx = 0.5, rely = 0.83, anchor = 'center')
addM.place(relx = 0.5, rely = 0.93, anchor = 'center')

root.mainloop()