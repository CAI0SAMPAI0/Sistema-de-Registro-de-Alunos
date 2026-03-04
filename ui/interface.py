from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from PIL import ImageTk, Image, ImageDraw, ImageTk, ImageOps, ImageChops
from tkcalendar import Calendar, DateEntry
from datetime import date
from pathlib import Path

# IMPORT MAIN
from data.banco import *

BASE_DIR = Path(__file__).resolve().parent.parent
IMG_DIR = BASE_DIR / "images"

co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha

co6 = "#146C94"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

# criando a janela
janela = Tk()
janela.title('Sistema de Alunos')
janela.geometry('810x535')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

icon = PhotoImage(file=IMG_DIR / 'logo.png')
janela.iconphoto(False, icon)

style = Style(janela)
style.theme_use("clam")

# frames
frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, padx=0, pady=0, sticky=NSEW, columnspan=5)

frame_botoes = Frame(janela, width=100, height=200, bg=co1, relief=RAISED)
frame_botoes.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)

frame_details = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
frame_details.grid(row=1, column=1, padx=0, pady=1, sticky=NSEW)
 
frame_tabela = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
frame_tabela.grid(row=3, column=0, padx=10, pady=0, sticky=NSEW, columnspan=5)
 

# frame logo com img
global imagem, imagem_string, l_imagem

app_lg = Image.open(IMG_DIR / 'logo.png')
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text=" Sistema de Registro de Alunos", width=850, compound=LEFT, anchor=NW, font=('Verdana 15'), bg=co6, fg=co1)
app_logo.place(x=5, y=0)

# deixando a logo do sistema
def arredondar_img(img, radius):
    # abrindo img
    img = img.convert('RGBA')
    # pega alpha original
    largura, altura = img.size
    lado = min(largura, altura)

    # recorte central quadrado
    esquerda = (largura - lado) // 2
    topo = (altura - lado) // 2
    direita = esquerda + lado
    baixo = topo + lado

    img = img.crop((esquerda, topo, direita, baixo))
    img = img.resize((130,130), Image.LANCZOS)

    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle(
        (0, 0, img.size[0], img.size[1]),
        radius=30,
        fill=255
    )

    resultado = Image.new("RGBA", img.size)
    resultado.paste(img, (0, 0), mask)

    return ImageTk.PhotoImage(resultado)

imagem = Image.open(IMG_DIR / 'logo2.png')
imagem = imagem.resize((130,130), Image.LANCZOS)
imagem_rounded = arredondar_img(imagem, radius=30)
l_imagem = Label(frame_details, image=imagem_rounded, bg='white', fg=co4)
l_imagem.image = imagem_rounded
l_imagem.place(x=410, y=10)

# ------------------ criando funções para CRUD ------------------ 
# add
def adicionar():
    global imagem, imagem_string, l_imagem

    # obtendo valores
    nome = e_nome.get()
    email = e_email.get()
    tel = e_telefone.get()
    sexo = c_sexo.get()
    data = data_nascimento.get()
    endereco = e_endereco.get()
    curso = c_curso.get()
    img = imagem_string

    lista = [nome, email, tel, sexo, data, endereco, curso, img]

    # verificando se a lista contem valores vazios
    for i in lista:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos.')
            return

    # registrando os valores

    sistema_de_registro.register_student(lista)

    # limpando os campos de entradas
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_telefone.delete(0, END)
    c_sexo.delete(0, END)
    data_nascimento.delete(0, END)
    e_endereco.delete(0, END)
    c_curso.delete(0, END)

    # mostrando valores
    mostrar_alunos()

# func procurar
def procurar():
    global imagem, imagem_string, l_imagem

    id_aluno = int(e_procurar.get())
    dados = sistema_de_registro.search_student(id_aluno)

    # limpando os campos de entradas

    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_telefone.delete(0, END)
    c_sexo.delete(0, END)
    data_nascimento.delete(0, END)
    e_endereco.delete(0, END)
    c_curso.delete(0, END)

    # inserindo os campos de entrada

    e_nome.insert(END, dados[1])
    e_email.insert(END, dados[2])
    e_telefone.insert(END, dados[3])
    c_sexo.insert(END, dados[4])
    data_nascimento.insert(END, dados[5])
    e_endereco.insert(END, dados[6])
    c_curso.insert(END, dados[7])

    imagem = dados[8]
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130,130), Image.LANCZOS)
    imagem_rounded = arredondar_img(imagem, radius=30)
    l_imagem = Label(frame_details, image=imagem_rounded, bg='white', fg=co4)
    l_imagem.image = imagem_rounded
    l_imagem.place(x=410, y=10)

# func atualizar
def atualizar():
    global imagem, imagem_string, l_imagem
    id_aluno = int(e_procurar.get())

    # obtendo valores
    nome = e_nome.get()
    email = e_email.get()
    tel = e_telefone.get()
    sexo = c_sexo.get()
    data = data_nascimento.get()
    endereco = e_endereco.get()
    curso = c_curso.get()
    img = imagem_string

    lista = [nome, email, tel, sexo, data, endereco, curso, img, id_aluno]

    # verificando se a lista contem valores vazios
    for i in lista:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos.')
            return

    # registrando os valores

    sistema_de_registro.update_student(lista)

    
    # limpando os campos de entradas
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_telefone.delete(0, END)
    c_sexo.delete(0, END)
    data_nascimento.delete(0, END)
    e_endereco.delete(0, END)
    c_curso.delete(0, END)

    # abrindo a img
    imagem = Image.open(IMG_DIR / 'logo2.png')
    imagem = imagem.resize((130,130), Image.LANCZOS)
    imagem_rounded = arredondar_img(imagem, radius=30)
    l_imagem = Label(frame_details, image=imagem_rounded, bg='white', fg=co4)
    l_imagem.image = imagem_rounded
    l_imagem.place(x=410, y=10)

    # mostrando valores
    mostrar_alunos()

# função deletar
def deletar():
    global imagem, imagem_string, l_imagem
    id_aluno = int(e_procurar.get())

    # DELETANDO O ALUNO
    sistema_de_registro.delete_student(id_aluno)
    
    # limpando os campos de entradas
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_telefone.delete(0, END)
    c_sexo.delete(0, END)
    data_nascimento.delete(0, END)
    e_endereco.delete(0, END)
    c_curso.delete(0, END)

    e_procurar.delete(0, END)

    # abrindo a img
    imagem = Image.open(IMG_DIR / 'logo2.png')
    imagem = imagem.resize((130,130), Image.LANCZOS)
    imagem_rounded = arredondar_img(imagem, radius=30)
    l_imagem = Label(frame_details, image=imagem_rounded, bg='white', fg=co4)
    l_imagem.image = imagem_rounded
    l_imagem.place(x=410, y=10)

    # mostrando valores
    mostrar_alunos()

# ------- detalhes -------

l_nome = Label(frame_details, text='Nome *', anchor=CENTER, font=('Ivy 10'), bg=co1, foreground=co4)
l_nome.place(x=4,y=10)
e_nome = Entry(frame_details, width=30, justify='left', relief='solid')
e_nome.place(x=7, y=40)
 
l_email = Label(frame_details, text='Email *', anchor=CENTER, font=('Ivy 10'), bg=co1, foreground=co4)
l_email.place(x=4,y=70)
e_email = Entry(frame_details, width=30, justify='left', relief='solid')
e_email.place(x=7, y=100)
 
l_telefone = Label(frame_details, text='Telefone *', anchor=CENTER, font=('Ivy 10'), bg=co1, foreground=co4)
l_telefone.place(x=4,y=130)
e_telefone = Entry(frame_details, width=18, justify='left', relief='solid')
e_telefone.place(x=7, y=160)
 
l_sexo = Label(frame_details, text='Sexo *', anchor=CENTER, font=('Ivy 10'), bg=co1, foreground=co4)
l_sexo.place(x=127,y=130)
c_sexo = Combobox(frame_details, width=7, font=('Ivy 8 bold'), justify='center')
c_sexo['values'] = ('M','F')
c_sexo.place(x=130, y=160)

l_nascimento = Label(frame_details, text='Data de nascimento *', anchor=NW, font=('Ivy 10'), bg=co1, foreground=co4)
l_nascimento.place(x=220,y=10)
data_nascimento = DateEntry(frame_details, width=18, justify='center', background='darkblue', foreground='white', borderwidth=2, year=2026)
data_nascimento.place(x=224, y=40)
 
l_endereco = Label(frame_details, text='Endereço *', anchor=NW, font=('Ivy 10'), bg=co1, foreground=co4)
l_endereco.place(x=220,y=70)
e_endereco = Entry(frame_details, width=20, justify='left', relief='solid')
e_endereco.place(x=224, y=100)
 
cursos = ['Administração', 'Análise e Desenvolvimento de Sistemas', 'Arquitetura e Urbanismo', 'Biomedicina', 'Ciência da Computação', 'Ciência de Dados', 'Ciências Biológicas', 'Ciências Contábeis', 'Direito', 'Design', 'Educação Física', 'Enfermagem', 'Engenharia Civil', 'Engenharia da Computação', 'Engenharia de Software', 'Farmácia', 'Fisioterapia', 'Fonoaudiologia', 'Gestão Ambiental', 'Gestão de Recursos Humanos', 'Jornalismo', 'Logística', 'Marketing Digital', 'Matemática', 'Medicina', 'Medicina Veterinária', 'Nutrição', 'Odontologia', 'Pedagogia', 'Programação', 'Psicologia', 'Publicidade e Propaganda', 'Química', 'Relações Internacionais', 'Sistemas de Informação', 'Teatro']

l_curso = Label(frame_details, text='Cursos *', anchor=CENTER, font=('Ivy 10'), bg=co1, foreground=co4)
l_curso.place(x=220,y=130)
c_curso = Combobox(frame_details, width=20, font=('Ivy 8 bold'), justify='left')
c_curso['values'] = (cursos)
c_curso.place(x=224, y=160)

# func para escolher img

def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename(
        filetypes=[('Imagens', "*.png *.jpg *.jpeg")]
    )
    if not imagem:
        return
    imagem_string=imagem

    img = Image.open(imagem)
    imagem_rounded = arredondar_img(img, 30)

    l_imagem.config(image=imagem_rounded)
    l_imagem.image = imagem_rounded

    btn_carregar['text'] = 'Trocar a foto'

btn_carregar = Button(frame_details, command=escolher_imagem, text='Carregar foto'.upper(), width=20, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, foreground=co0)
btn_carregar.place(x=410, y=160)

# tabela de alunos
def mostrar_alunos():
    # árvore de vizualização dupla
    list_header = ['ID', 'Nome', 'E-mail', 'Telefone', 'Sexo', 'Data', 'Endereço', 'Curso']
    # listar todos os estudantes
    df_list = sistema_de_registro.view_all_students()
    tree_aluno = ttk.Treeview(frame_tabela, selectmode='extended', columns=list_header, show='headings')

    # barra de scroll vertical e horizontal
    vsb = ttk.Scrollbar(frame_tabela, orient='vertical', command=tree_aluno.yview)
    hsb = ttk.Scrollbar(frame_tabela, orient='horizontal', command=tree_aluno.xview)

    tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_aluno.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=1, row=1, sticky='ew')
    frame_tabela.grid_rowconfigure(0, weight=12)

    hd=['nw', 'nw', 'nw', 'center', 'center', 'center', 'center', 'center', 'center']
    h=[40,150,150,70,70,70,120,100,100]
    n=0

    for col in list_header:
        tree_aluno.heading(col, text=col.title(), anchor=NW)
        # ajuste do header nas colunas
        tree_aluno.column(col, width=h[n], anchor=hd[n])

        n+=1

    for item in df_list:
        tree_aluno.insert('', 'end', values=item)

# procurar aluno

frame_procurar = Frame(frame_botoes, width=40, height=55, bg=co1, relief=RAISED)
frame_procurar.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)

l_nome = Label(frame_procurar, text='Procurar aluno [ID]', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

e_procurar = Entry(frame_procurar, width=18, justify='left', relief='solid', font=('Ivy 10'))
e_procurar.grid(row=1, column=0, padx=0, pady=10, sticky=NSEW)

btn_procurar = Button(frame_procurar, command=procurar, text='Procurar', width=9, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, foreground=co0)
btn_procurar.grid(row=1, column=1, padx=0, pady=10, sticky=NSEW)


# ----- Botões -----

img_add=Image.open(IMG_DIR / 'add.png')
img_add=img_add.resize((25,25))
img_add=ImageTk.PhotoImage(img_add)
btn_adicionar = Button(frame_botoes, command=adicionar, image=img_add, relief=GROOVE, text='Adicionar', width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, foreground=co0)
btn_adicionar.grid(row=1, column=0, padx=10, pady=5, sticky=NSEW)

img_refresh=Image.open(IMG_DIR / 'refresh.png')
img_refresh=img_refresh.resize((25,25))
img_refresh=ImageTk.PhotoImage(img_refresh)
btn_atualizar = Button(frame_botoes, command=atualizar, image=img_refresh, relief=GROOVE, text='Atualizar', width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, foreground=co0)
btn_atualizar.grid(row=2, column=0, padx=10, pady=5, sticky=NSEW)

img_del=Image.open(IMG_DIR / 'delete.png')
img_del=img_del.resize((25,25))
img_del=ImageTk.PhotoImage(img_del)
btn_deletar = Button(frame_botoes, command=deletar, image=img_del, relief=GROOVE, text='Deletar', width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, foreground=co0)
btn_deletar.grid(row=3, column=0, padx=10, pady=5, sticky=NSEW)

# ----- linha separatória -----
l_linha = Button(frame_botoes, relief=GROOVE, text='h', width=1, height=123, anchor=NW, font=('Ivy 1'), bg=co1, foreground=co1)
l_linha.place(x=213, y=15)





# chamar a tabela
mostrar_alunos()



janela.mainloop()