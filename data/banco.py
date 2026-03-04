import sqlite3
from tkinter import messagebox
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "estudante.db"

class SistemaDeRegistro:
    def __init__(self): # criar o banco
        self.conn = sqlite3.connect(DB_PATH)
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS estudantes (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL,
                                email TEXT NOT NULL,
                                tel TEXT NOT NULL,
                                sexo TEXT NOT NULL,
                                data_nascimento TEXT NOT NULL,
                                endereco TEXT NOT NULL, 
                                curso TEXT NOT NULL,
                                picture TEXT NOT NULL)''')

    def register_student(self, estudantes):
        self.c.execute('INSERT INTO estudantes (nome, email, tel, sexo, data_nascimento, endereco, curso, picture) VALUES (?,?,?,?,?,?,?,?)', (estudantes))
        self.conn.commit()
        # mostrando mensagem de sucesso
        messagebox.showinfo("Sucesso", 'Registro com sucesso!')
        
    def view_all_students(self):
        self.c.execute('SELECT * FROM estudantes')
        dados = self.c.fetchall()

        return dados

    def search_student(self, id):
        self.c.execute("SELECT * FROM estudantes WHERE id=?", (id,))
        dados = self.c.fetchone()
        return dados

    def update_student(self, novos_valores):
        query = "UPDATE estudantes SET nome=?, email=?, tel=?, sexo=?, data_nascimento=?, endereco=?, curso=?, picture=? WHERE id=?"
        self.c.execute(query, novos_valores)
        self.conn.commit()
        messagebox.showinfo("Sucesso", f'Registro do estudante com o ID {novos_valores[8]} foi atualizado com sucesso!')

    def delete_student(self, id):
        self.c.execute("DELETE FROM estudantes WHERE id=?", (id,))
        self.conn.commit()
        messagebox.showinfo("Sucesso", f'Registro do estudante com o ID {id} foi deletado com sucesso!')

# criando instância do sis de registro
sistema_de_registro = SistemaDeRegistro()
