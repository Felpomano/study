## apagar itens do banco de dados

import sqlite3

conn = sqlite3.connect("ProjetoN2FeGui.db")

while True:
    print(" APAGADOR DE ID ")
    vid = input("ID: ")

    vconfirma = input("Deseja apagar este id? (s/n)")
    if vconfirma == "s":
        conn.execute("delete from carros where id ='" + vid + "'");
        print("O id deste carro foi apagado.")
        conn.commit()
        

    vcontinua = input("Digite S para continuar: ")
    if vcontinua != "s":
        break
quit()
