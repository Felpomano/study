import sqlite3

conn = sqlite3.connect("ProjetoN2FeGui.db")

while True:
    print(" CADASTRO DE USUÁRIO ")
    idusu = int(input("ID: "))
    nome = input("NOME: ")
    login = input("LOGIN: ")
    senha = input("SENHA: ")
    vconfirma = input("Deseja fazer o cadastro? (s/n)")
    if vconfirma == "s":
        conn.execute("insert into usuario values (?, ?, ?, ?); ",(idusu, nome, login, senha, ));
        conn.commit()
    else:
        print("Não será gravado no banco.")

        break
    quit()
        
