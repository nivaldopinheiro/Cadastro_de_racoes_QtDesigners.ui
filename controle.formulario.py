from PyQt5 import uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host= "localhost",
    user = "root",
    passwd = "",
    database = "Cadastro_de_racoes_QtDesigners"
)

def funcao_principal():
    linha1 = Cadastro_de_racoes_QtDesigners.lineEdit.text()
    linha2 = Cadastro_de_racoes_QtDesigners.lineEdit_2.text()
    linha3 = Cadastro_de_racoes_QtDesigners.lineEdit_3.text()
    linha4 = Cadastro_de_racoes_QtDesigners.lineEdit_4.text()
    linha5 = Cadastro_de_racoes_QtDesigners.lineEdit_5.text()
    linha6 = Cadastro_de_racoes_QtDesigners.lineEdit_6.text()

    categoria = ""

    if Cadastro_de_racoes_QtDesigners.radioButton.isChecked():
        print("Categoria Gato selecionada")
        categoria ="Gato"
    elif Cadastro_de_racoes_QtDesigners.radioButton_2.isChecked():
        print("Categoria Cachorro selecionada")
        categoria ="Cachorro"
    else:
        print("Categoria Outros selecionada")
        categoria ="Outro"

    print("Id_doação:", linha1)
    print("Parceiro:", linha2)
    print("CPF/CNPJ:", linha3)
    print("Descrição:", linha4)
    print("Data da doação:", linha5)
    print("Quantidade Kg:", linha6)

    '''cursor = banco.cursor()
    comando_SQL = "INSERT INTO doacoes (Id_doação,Parceiro,CPF/CNPJ,Data da doação, Quantidade Kg, categoria) VALUES (%s,%s,%s,%s,%s,%s)"
    dados = (str(linha1),str(linha2),str(linha3),str(linha4),str(linha5),str(linha6),categoria)
    cursor.execute(comando_SQL,dados)
    banco.commit()'''

    Cadastro_de_racoes_QtDesigners.lineEdit.setText("")
    Cadastro_de_racoes_QtDesigners.lineEdit_1.setText("")
    Cadastro_de_racoes_QtDesigners.lineEdit_2.setText("")
    Cadastro_de_racoes_QtDesigners.lineEdit_3.setText("")
    Cadastro_de_racoes_QtDesigners.lineEdit_4.setText("")
    Cadastro_de_racoes_QtDesigners.lineEdit_5.setText("")
    Cadastro_de_racoes_QtDesigners.lineEdit_6.setText("")

def chama_segunda_tela():
        segunda_tela.show()

app=QtWidgets.QApplication([])
Cadastro_de_racoes_QtDesigners=uic.loadUi("Cadastro_de_racoes_QtDesigners.ui")
segunda_tela=uic.loadUi("Listar_dados.ui")
Cadastro_de_racoes_QtDesigners.pushButton.cliked.connect(funcao_principal)
Cadastro_de_racoes_QtDesigners.pushButton_2.cliked.connect(chama_segunda_tela)


Cadastro_de_racoes_QtDesigners.show()
app.exec()