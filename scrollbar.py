from tkinter import *
from tkinter.ttk import *

def verificaBotao(msg):
        print(msg)


def main():
    root = Tk()
    root.geometry('700x500')
    root.maxsize(700, 500)
    root.minsize(700, 500)
    root.title("Login")
    #mainFrame
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)

    #canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    #Adicionando scrollbar ao Canvas
    my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command= my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    #configurando o canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion= my_canvas.bbox("all")))

    #Create ANOTHER
    second_frame = Frame(my_canvas)

    #Adicionando janela ao canvas
    my_canvas.create_window((0,200), window=second_frame, anchor="nw")
    y = 10
    Label(second_frame).grid(row=0, column=0, padx=20, pady=40, sticky=E)
    Label(second_frame).grid(row=1, column=1, padx=20, pady=y, sticky=E)
    Label(second_frame).grid(row=2, column=2, padx=20, pady=y, sticky=E)
    Label(second_frame).grid(row=3, column=3, padx=20, pady=y, sticky=E)
    Label(second_frame).grid(row=4, column=4, padx=20, pady=y, sticky=E)
    Label(second_frame).grid(row=5, column=5, padx=20, pady=y, sticky=E)
    for i in range(5, 100):
        Label(second_frame, text=f"Produto {i}").grid(row=i, column=6, padx=20, pady=y, sticky=E)
        Label(second_frame, text=f"Valor {i}").grid(row=i, column=7, padx=20, pady=y, sticky=E)
        Button(second_frame, text=f'Botão {i}', command= lambda m=f"Botão {i}": verificaBotao(m)).grid(row=i, column=8, padx=20, pady=y, sticky=E)

    root.mainloop()
if __name__ == "__main__": main()

