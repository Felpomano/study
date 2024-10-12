## Acréscimo de loop e import
import sqlite3

conn = sqlite3.connect("ProjetoN2FeGui.db")
##while True:
##    data = input("Digite a data de hoje: ")
##    hora = input("Digite a hora: ")

    




while True:
    print(" CADASTRO DE CARROS ")
    vid = input("ID: ")
    vmodelo =  input("Modelo: ")
    vano =input("Ano: ")
    vtipo = input("Tipo: ")
    vfab = input("Fabricante: ")

    vconfirma = input("Deseja fazer o cadastro?(s/n)")
    if vconfirma == "s":
        conn.execute("insert into carros values (?, ?, ?, ?, ?); ",(vid, vmodelo, vano, vtipo, vfab,));
        conn.commit()
    else:
        print("Não será gravado no banco.")

    vcontinua = input("Digite S para continuar: ")
    if vcontinua != "s":
        break
quit()
