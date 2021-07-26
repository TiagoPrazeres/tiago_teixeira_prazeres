# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dadosCliente.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


### Imports sistema ###
import mysql.connector
import pandas as pd

import tkinter
from tkinter import messagebox

### Arquivo variáveis de controle ###
import variaveisControle

### Variáveis de conexão com o banco de dados ###
host = variaveisControle.host
user = variaveisControle.user
password = variaveisControle.password
database = variaveisControle.database


class Ui_formDadosCliente(object):
    def setupUi(self, formDadosCliente):
        formDadosCliente.setObjectName("formDadosCliente")
        formDadosCliente.resize(599, 506)
        formDadosCliente.setStyleSheet("background-color: rgb(129, 181, 200);")
        self.lb_nome = QtWidgets.QLabel(formDadosCliente)
        self.lb_nome.setGeometry(QtCore.QRect(30, 73, 59, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lb_nome.setFont(font)
        self.lb_nome.setObjectName("lb_nome")
        self.lb_cidade = QtWidgets.QLabel(formDadosCliente)
        self.lb_cidade.setGeometry(QtCore.QRect(30, 253, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lb_cidade.setFont(font)
        self.lb_cidade.setObjectName("lb_cidade")
        self.txt_nome = QtWidgets.QLineEdit(formDadosCliente)
        self.txt_nome.setGeometry(QtCore.QRect(130, 80, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_nome.setFont(font)
        self.txt_nome.setStyleSheet("border-radius: 15px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px")
        self.txt_nome.setText("")
        self.txt_nome.setObjectName("txt_nome")
        self.txt_telefone = QtWidgets.QLineEdit(formDadosCliente)
        self.txt_telefone.setGeometry(QtCore.QRect(130, 170, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_telefone.setFont(font)
        self.txt_telefone.setStyleSheet("border-radius: 15px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px")
        self.txt_telefone.setText("")
        self.txt_telefone.setObjectName("txt_telefone")
        self.txt_cidade = QtWidgets.QLineEdit(formDadosCliente)
        self.txt_cidade.setGeometry(QtCore.QRect(130, 260, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_cidade.setFont(font)
        self.txt_cidade.setStyleSheet("border-radius: 15px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px")
        self.txt_cidade.setText("")
        self.txt_cidade.setObjectName("txt_cidade")
        self.lb_telefone = QtWidgets.QLabel(formDadosCliente)
        self.lb_telefone.setGeometry(QtCore.QRect(30, 163, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lb_telefone.setFont(font)
        self.lb_telefone.setObjectName("lb_telefone")
        self.bt_cadastrar = QtWidgets.QPushButton(formDadosCliente)
        self.bt_cadastrar.setGeometry(QtCore.QRect(140, 360, 111, 81))
        self.bt_cadastrar.setStyleSheet("image: url(:/confirmar/imagens/confirmar.png);\n"
"background-color: rgb(173, 200, 202);")
        self.bt_cadastrar.setText("")
        self.bt_cadastrar.setObjectName("bt_cadastrar")
        self.bt_cancelar = QtWidgets.QPushButton(formDadosCliente)
        self.bt_cancelar.setGeometry(QtCore.QRect(350, 360, 111, 81))
        self.bt_cancelar.setStyleSheet("image: url(:/cancelar/imagens/cancelar.png);\n"
"background-color: rgb(173, 200, 202);")
        self.bt_cancelar.setText("")
        self.bt_cancelar.setObjectName("bt_cancelar")

        self.retranslateUi(formDadosCliente)
        QtCore.QMetaObject.connectSlotsByName(formDadosCliente)

    def retranslateUi(self, formDadosCliente):
        _translate = QtCore.QCoreApplication.translate
        formDadosCliente.setWindowTitle(_translate("formDadosCliente", "Cliente"))
        self.lb_nome.setText(_translate("formDadosCliente", "Nome:"))
        self.lb_cidade.setText(_translate("formDadosCliente", "Cidade:"))
        self.lb_telefone.setText(_translate("formDadosCliente", "Telefone:"))
        self.bt_cadastrar.setToolTip(_translate("formDadosCliente", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Confirmar</span></p></body></html>"))
        self.bt_cancelar.setToolTip(_translate("formDadosCliente", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Cancelar</span></p></body></html>"))

##################################################################################################
######################################### BOTÕES SISTEMA #########################################
##################################################################################################

        self.bt_cancelar.clicked.connect(lambda: self.sairTela(formDadosCliente))
        if variaveisControle.tipoTelaDadosCliente == 'incluir':
            self.bt_cadastrar.clicked.connect(self.cadastrarCliente)
        if variaveisControle.tipoTelaDadosCliente == 'alterar':
            self.bt_cadastrar.clicked.connect(self.alterarCliente)

        ### Condições da tela ###
        ## Tipo form tela ##
        if variaveisControle.tipoTelaDadosCliente == 'incluir':
            self.txt_nome.setEnabled(True)
            self.txt_telefone.setEnabled(True)
            self.txt_cidade.setEnabled(True)
            self.bt_cadastrar.setEnabled(True)
        elif variaveisControle.tipoTelaDadosCliente == 'consultar':
            self.txt_nome.setEnabled(False)
            self.txt_telefone.setEnabled(False)
            self.txt_cidade.setEnabled(False)
            self.bt_cadastrar.setEnabled(False)
            # Conexão com o banco de dados #
            mydb = mysql.connector.connect(
                host = host,
                user = user,
                password = password,
                database = database
            )
            mycursor = mydb.cursor()
            consultaSQL = "SELECT * FROM cliente WHERE IdCliente = '" + variaveisControle.idConsulta + "'"
            mycursor.execute(consultaSQL)
            myresult = mycursor.fetchall()
            mycursor.close()
            # Converte resultados BD para DataFrame #
            df = pd.DataFrame(myresult, columns = ['ID', 'Nome', 'Telefone', 'Cidade'])
            nomeCliente = df['Nome'][0]
            telefoneCliente = df['Telefone'][0]
            cidadeCliente = df['Cidade'][0]
            # Seta variáveis na tela do sistema #
            self.txt_nome.setText(nomeCliente)
            self.txt_telefone.setText(telefoneCliente)
            self.txt_cidade.setText(cidadeCliente)
        elif variaveisControle.tipoTelaDadosCliente == 'alterar':
            self.txt_nome.setEnabled(True)
            self.txt_telefone.setEnabled(True)
            self.txt_cidade.setEnabled(True)
            self.bt_cadastrar.setEnabled(True)
            # Conexão com o banco de dados #
            mydb = mysql.connector.connect(
                host = host,
                user = user,
                password = password,
                database = database
            )
            mycursor = mydb.cursor()
            consultaSQL = "SELECT * FROM cliente WHERE IdCliente = '" + variaveisControle.idConsulta + "'"
            mycursor.execute(consultaSQL)
            myresult = mycursor.fetchall()
            mycursor.close()
            # Converte resultados BD para DataFrame #
            df = pd.DataFrame(myresult, columns = ['ID', 'Nome', 'Telefone', 'Cidade'])
            nomeCliente = df['Nome'][0]
            telefoneCliente = df['Telefone'][0]
            cidadeCliente = df['Cidade'][0]
            # Seta variáveis na tela do sistema #
            self.txt_nome.setText(nomeCliente)
            self.txt_telefone.setText(telefoneCliente)
            self.txt_cidade.setText(cidadeCliente)

##################################################################################################
##################################### FUNÇÕES DO SISTEMA #########################################
##################################################################################################

    ## Sair dadosCliente ##
    def sairTela(self, formDadosCliente):
        variaveisControle.tipoTelaDadosCliente == ''
        formDadosCliente.close()

    ## CADASTRAR CLIENTE ##
    def cadastrarCliente(self):
        nomeCliente = self.txt_nome.text()
        telefoneCliente = self.txt_telefone.text()
        cidadeCliente = self.txt_cidade.text()
        root = tkinter.Tk()
        root.withdraw()

        if nomeCliente == "" or telefoneCliente == "" or cidadeCliente == "":
            messagebox.showerror("Erro ao Cadastrar", "PREENCHA TODOS OS CAMPOS PARA CADASTRAR")
        else:

            mydb = mysql.connector.connect(
                host = host,
                user = user,
                password = password,
                database = database
            )

            mycursor = mydb.cursor()
            sql = "INSERT INTO cliente (Nome, Telefone, Cidade) values (%s,  %s, %s)"
            val = (nomeCliente, telefoneCliente, cidadeCliente)
            mycursor.execute(sql, val)
            mydb.commit()
            mycursor.close()
            self.txt_nome.setText("")
            self.txt_telefone.setText("")
            self.txt_cidade.setText("")
            messagebox.showinfo("Cadastrado", "CADASTRADO COM SUCESSO")
            

    ## ALTERAR CLIENTE ##
    def alterarCliente(self):
        nomeCliente = self.txt_nome.text()
        telefoneCliente = self.txt_telefone.text()
        cidadeCliente = self.txt_cidade.text()
        root = tkinter.Tk()
        root.withdraw()

        if nomeCliente == "" or telefoneCliente == "" or cidadeCliente == "":
            messagebox.showerror("Erro ao Alterar", "PREENCHA TODOS OS CAMPOS PARA ALTERAR")
        else:

            mydb = mysql.connector.connect(
                host = host,
                user = user,
                password = password,
                database = database
            )

            mycursor = mydb.cursor()
            sql = "UPDATE cliente SET Nome = '" + nomeCliente + "', Telefone = '" + telefoneCliente + "', Cidade = '" + cidadeCliente + "' WHERE IdCliente = '" + variaveisControle.idConsulta + "'"
            mycursor.execute(sql)
            mydb.commit()
            mycursor.close()
            messagebox.showinfo("Alterado", "ALTERADO COM SUCESSO")

import cancelar
import confirmar


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formDadosCliente = QtWidgets.QWidget()
    ui = Ui_formDadosCliente()
    ui.setupUi(formDadosCliente)
    formDadosCliente.show()
    sys.exit(app.exec_())
