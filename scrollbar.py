from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry('300x500')
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
my_canvas.create_window((0,0), window=second_frame, anchor="nw")

for i in range(100):
    Button(second_frame, text=f'Botão {i}').grid(row=i, column=0, pady=10, padx=10)

root.mainloop()
