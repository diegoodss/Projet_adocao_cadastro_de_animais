from PySide6 import QtCore
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import*
from PySide6.QtWidgets import *
import sys
from ui_main import *
import pandas as pd
#from icons import *
import re

from database1 import DataBase1




class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow
        self.setupUi(self)
        self.setWindowTitle("CODEDS - Sistema de Cadastro")
        appIcon = QIcon(u'')
        #ESTANCIAR O BANCO DE DADOS
        self.db = DataBase1()

        self.botao_menu.clicked.connect(lambda: self.ui.page.set(self.pagina_inicial))

        self.botao_menu.clicked.connect(self.left_menu)
        #BOTÂO PARA CADASTRAR 
        self.btn_cadastrar_4.clicked.connect(self.cadastrar_animal)

        self.buscar_animal()

        #BOTAO DELET
        self.btn_excluir.clicked.connect(self.delet)

        #BOTÃO PARA GERAR O EXCEL
        self.btn_relatorio_excel_2.clicked.connect(self.gerar_excel)

        #BOTÃO PARA ATUALIZAR
        self.btn_alterar.clicked.connect(self.atualizar_animal)

        #BOTÃO PARA PESQUISAR OS DADOS
        self.input_pesquisar.textChanged.connect(self.filtrar_dados)

        #self.btn_alterar.clicked.connect(self.editar_animal)

    def left_menu(self):
        width = self.left_frame.width
        
        if width ==9:
            newWidth = 200
        else:
            newWidth = 9 
        self.animation = QtCore.QPropertyAnimation(self.left_menu, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.animation.start()

    #FUNÇÃO PARA CADASTRAR
    def cadastrar_animal(self):
        especie = self.input_especie_4.text()
        nome = self.input_nome_4.text()
        raca = self.input_raca_4.text()
        cor = self.input_cor_4.text()
        idade = self.input_idade_4.text()
        peso = self.input_peso_4.text()
        sexo = self.input_sexo_4.currentText()
        situacao = self.input_situacao_4.currentText()
        porte = self.input_porte_4.currentText()

        tupla = (especie,nome,raca,cor,idade,peso,sexo,situacao,porte)

        result=self.db.cadastrar_animal(tupla)
        print(result)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("EMPRESAS")
        msg.setText(result)
        msg.exec()
        self.clean()
        self.buscar_animal()

    #FUNÇÃO PARA LIMPAR OS CAMPOS APOS OS DADOS CADASTRADOS
    def clean(self):
        self.input_especie_4.setText("")
        self.input_nome_4.setText("")
        self.input_raca_4.setText("")
        self.input_cor_4.setText("")
        self.input_idade_4.setText("")
        self.input_peso_4.setText("")
        self.input_sexo_4.setCurrentText("")
        self.input_situacao_4.setCurrentText("")
        self.input_porte_4.setCurrentText("")

    #FUNÇÃO PARA BUSCAR OS DADOS DO BANCO DE DADOS 
    def buscar_animal(self):

        result  = self.db.buscar_todos()

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tableWidget.setItem(row, column,QTableWidgetItem(str(data)))

    #FUNÇÃO PARA DELETAR
    def delet(self):

        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registor será excluído.")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            id = self.tableWidget.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = self.db.deletar_animal(id)
            self.buscar_animal()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("EMPRESAS")
            msg.setText(result)
            msg.exec()

    def atualizar_animal(self):
        
        dados = []
        update_dados = []

        for row in range(self.tableWidget.rowCount()):
            for column in range(self.tableWidget.columnCount()):
                dados.append(self.tableWidget.item(row, column).text())
            update_dados.append(dados)
            dados = []

        for emp in update_dados:
            db.alterar_animal(tuple(emp))

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização de Dados")
        msg.setText("Dados atualizados com sucesso!")
        msg.exec()

        self.tableWidget.reset()
        self.buscar_animal()

    def filtrar_dados(self):
        txt = re.sub('[\W_]+','',self.input_pesquisar.text())
        res = self.db.filter(txt)
        #print(res)

        self.tableWidget.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(data)))

    #GERAR RELATORIO EM EXCEL
    def gerar_excel(self):

        dados = []
        all_dados =  []

        for row in range(self.tableWidget.rowCount()):
            for column in range(self.tableWidget.columnCount()):
                dados.append(self.tableWidget.item(row, column).text())
        
            all_dados.append(dados)
            dados = []

        columns = ['epecie', 'nome', 'raça', 
            'cor', 'idade', 'peso', 'sexo','situação','porte']
        
        empresas = pd.DataFrame(all_dados, columns= columns)
        
        file, _ = QFileDialog.getSaveFileName(self, "Selecionar pasta de saida", "/relatorio", "Text files (*.xlsx)") #ESCOLHER ONDE VAI SALVAR O ARQUIVO
        empresas.to_excel("Animasi.xlsx", sheet_name='animais', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excel")
        msg.setText("Relatório Excel gerado com sucesso!")
        msg.exec()

if __name__ == "__main__":

    db = DataBase1()
    db.connect
    db.close_connection

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
