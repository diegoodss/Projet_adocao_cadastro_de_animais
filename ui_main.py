# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastrowZQCQg.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QToolBox,
    QVBoxLayout, QWidget)
import icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1864, 884)
        MainWindow.setStyleSheet(u"\n"
"background-color: rgb(253, 253, 150);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border:none;\n"
"}\n"
"QLabel{\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_frame = QFrame(self.centralwidget)
        self.left_frame.setObjectName(u"left_frame")
        self.left_frame.setMaximumSize(QSize(200, 16777215))
        self.left_frame.setStyleSheet(u"")
        self.left_frame.setFrameShape(QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.frame_2 = QFrame(self.left_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.left_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame{\n"
"\n"
"	\n"
"\n"
"}\n"
"\n"
"QToolBox{\n"
"\n"
"	text-align:left;\n"
"	rgb(240, 240, 142)\n"
"	\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"	border-radius: 5px;\n"
"	\n"
"	background-color: rgb(240, 240, 142);\n"
"	text-align: left;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, 0, 0)
        self.toolBox = QToolBox(self.frame_3)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(204, 204, 121);\n"
"	border-top-left-radius:15px\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(229, 229, 136);\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 182, 711))
        self.page.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setSizeIncrement(QSize(0, 30))
        self.btn_home.setBaseSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(11)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(u"border-radius: 5px;")

        self.verticalLayout_5.addWidget(self.btn_home)

        self.btn_cadastrar = QPushButton(self.page)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setBaseSize(QSize(0, 30))
        self.btn_cadastrar.setFont(font)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"border-radius: 5px;")

        self.verticalLayout_5.addWidget(self.btn_cadastrar)

        self.btn_contratos = QPushButton(self.page)
        self.btn_contratos.setObjectName(u"btn_contratos")
        self.btn_contratos.setBaseSize(QSize(0, 30))
        self.btn_contratos.setFont(font)
        self.btn_contratos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_contratos.setStyleSheet(u"border-radius: 5px;")

        self.verticalLayout_5.addWidget(self.btn_contratos)

        self.btn_contato = QPushButton(self.page)
        self.btn_contato.setObjectName(u"btn_contato")
        self.btn_contato.setBaseSize(QSize(0, 30))
        self.btn_contato.setFont(font)
        self.btn_contato.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_contato.setStyleSheet(u"border-radius: 5px;")

        self.verticalLayout_5.addWidget(self.btn_contato)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Page 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 182, 711))
        self.horizontalLayout_3 = QHBoxLayout(self.page_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.textEdit = QTextEdit(self.page_2)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_3.addWidget(self.textEdit)

        self.toolBox.addItem(self.page_2, u"Page 2")

        self.verticalLayout_4.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.left_frame)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.botao_menu = QPushButton(self.top_frame)
        self.botao_menu.setObjectName(u"botao_menu")
        self.botao_menu.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"icons/cardapio.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botao_menu.setIcon(icon)
        self.botao_menu.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.botao_menu, 0, Qt.AlignLeft)

        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Sitka"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_fram = QFrame(self.main_container)
        self.main_fram.setObjectName(u"main_fram")
        self.main_fram.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_fram.sizePolicy().hasHeightForWidth())
        self.main_fram.setSizePolicy(sizePolicy)
        self.main_fram.setStyleSheet(u"")
        self.main_fram.setFrameShape(QFrame.StyledPanel)
        self.main_fram.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.main_fram)
        self.verticalLayout_6.setSpacing(9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, 9, 9, 9)
        self.Paginas = QStackedWidget(self.main_fram)
        self.Paginas.setObjectName(u"Paginas")
        self.Paginas.setStyleSheet(u"	background-color: rgb(220, 220, 130);")
        self.pagina_cadastrar = QWidget()
        self.pagina_cadastrar.setObjectName(u"pagina_cadastrar")
        self.verticalLayout_8 = QVBoxLayout(self.pagina_cadastrar)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tabWidget = QTabWidget(self.pagina_cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_5 = QFrame(self.tab)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: rgb(240, 240, 150);\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setPixmap(QPixmap(u"icons/adocao.png.png"))

        self.verticalLayout_12.addWidget(self.label_9)


        self.horizontalLayout_6.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_15 = QFrame(self.frame_6)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy1)
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.frame_27 = QFrame(self.frame_15)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setGeometry(QRect(300, 120, 431, 59))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_27)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_27 = QLabel(self.frame_27)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_30.addWidget(self.label_27)

        self.input_nome_4 = QLineEdit(self.frame_27)
        self.input_nome_4.setObjectName(u"input_nome_4")
        self.input_nome_4.setStyleSheet(u"border-radius: 5px;\n"
"\n"
"border:1px solid rgb(200, 200, 118) ;\n"
"")

        self.verticalLayout_30.addWidget(self.input_nome_4)

        self.frame_28 = QFrame(self.frame_15)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setGeometry(QRect(20, 120, 251, 61))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_28)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_28 = QLabel(self.frame_28)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"font: 10pt \"Sitka\";")

        self.verticalLayout_31.addWidget(self.label_28)

        self.input_especie_4 = QLineEdit(self.frame_28)
        self.input_especie_4.setObjectName(u"input_especie_4")
        self.input_especie_4.setStyleSheet(u"\n"
"border:1px solid rgb(200, 200, 118) ;\n"
"border-radius: 5px;")

        self.verticalLayout_31.addWidget(self.input_especie_4)

        self.frame_29 = QFrame(self.frame_15)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setGeometry(QRect(20, 200, 251, 59))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_29)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_29 = QLabel(self.frame_29)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_32.addWidget(self.label_29)

        self.input_raca_4 = QLineEdit(self.frame_29)
        self.input_raca_4.setObjectName(u"input_raca_4")
        self.input_raca_4.setStyleSheet(u"\n"
"border:1px solid rgb(200, 200, 118) ;\n"
"border-radius: 5px;")

        self.verticalLayout_32.addWidget(self.input_raca_4)

        self.frame_30 = QFrame(self.frame_15)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setGeometry(QRect(300, 200, 411, 59))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_30)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_30 = QLabel(self.frame_30)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_33.addWidget(self.label_30)

        self.input_cor_4 = QLineEdit(self.frame_30)
        self.input_cor_4.setObjectName(u"input_cor_4")
        self.input_cor_4.setStyleSheet(u"\n"
"border:1px solid rgb(200, 200, 118) ;\n"
"border-radius: 5px;")

        self.verticalLayout_33.addWidget(self.input_cor_4)

        self.frame_31 = QFrame(self.frame_15)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setGeometry(QRect(20, 290, 281, 59))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_31)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_31 = QLabel(self.frame_31)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_34.addWidget(self.label_31)

        self.input_idade_4 = QLineEdit(self.frame_31)
        self.input_idade_4.setObjectName(u"input_idade_4")
        self.input_idade_4.setStyleSheet(u"\n"
"border:1px solid rgb(200, 200, 118) ;\n"
"border-radius: 5px;")

        self.verticalLayout_34.addWidget(self.input_idade_4)

        self.frame_32 = QFrame(self.frame_15)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setGeometry(QRect(340, 290, 321, 59))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_32)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_32 = QLabel(self.frame_32)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_35.addWidget(self.label_32)

        self.input_peso_4 = QLineEdit(self.frame_32)
        self.input_peso_4.setObjectName(u"input_peso_4")
        self.input_peso_4.setStyleSheet(u"\n"
"border:1px solid rgb(200, 200, 118) ;\n"
"border-radius: 5px;")

        self.verticalLayout_35.addWidget(self.input_peso_4)

        self.frame_33 = QFrame(self.frame_15)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setGeometry(QRect(20, 420, 211, 61))
        self.frame_33.setStyleSheet(u"")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_33)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_33 = QLabel(self.frame_33)
        self.label_33.setObjectName(u"label_33")

        self.verticalLayout_36.addWidget(self.label_33)

        self.input_sexo_4 = QComboBox(self.frame_33)
        self.input_sexo_4.setObjectName(u"input_sexo_4")
        self.input_sexo_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(200, 200, 118) ;\n"
"border-radius: 5px;")

        self.verticalLayout_36.addWidget(self.input_sexo_4)

        self.frame_34 = QFrame(self.frame_15)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setGeometry(QRect(470, 420, 211, 60))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_34)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_34 = QLabel(self.frame_34)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_37.addWidget(self.label_34)

        self.input_porte_4 = QComboBox(self.frame_34)
        self.input_porte_4.setObjectName(u"input_porte_4")
        self.input_porte_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(200, 200, 118) ;\n"
"border-radius: 5px;")

        self.verticalLayout_37.addWidget(self.input_porte_4)

        self.frame_35 = QFrame(self.frame_15)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setGeometry(QRect(250, 420, 191, 60))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_35)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_35 = QLabel(self.frame_35)
        self.label_35.setObjectName(u"label_35")

        self.verticalLayout_38.addWidget(self.label_35)

        self.input_situacao_4 = QComboBox(self.frame_35)
        self.input_situacao_4.setObjectName(u"input_situacao_4")
        self.input_situacao_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(200, 200, 118) ;\n"
"border-radius: 5px;")

        self.verticalLayout_38.addWidget(self.input_situacao_4)

        self.btn_cadastrar_4 = QPushButton(self.frame_15)
        self.btn_cadastrar_4.setObjectName(u"btn_cadastrar_4")
        self.btn_cadastrar_4.setGeometry(QRect(600, 580, 91, 31))
        self.btn_cadastrar_4.setStyleSheet(u"\n"
"border:1px solid rgb(200, 200, 118) ;\n"
"border-radius: 5px;")
        self.label_37 = QLabel(self.frame_15)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(30, 20, 681, 71))
        font2 = QFont()
        font2.setFamilies([u"Sitka Text"])
        font2.setPointSize(50)
        self.label_37.setFont(font2)
        self.label_37.setTextFormat(Qt.RichText)

        self.horizontalLayout_7.addWidget(self.frame_15)


        self.horizontalLayout_6.addWidget(self.frame_6)


        self.gridLayout_2.addWidget(self.frame_5, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_41 = QVBoxLayout(self.tab_2)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_41.addWidget(self.label_4)

        self.frame_37 = QFrame(self.tab_2)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_37)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_40 = QLabel(self.frame_37)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font2)
        self.label_40.setTextFormat(Qt.RichText)

        self.verticalLayout_16.addWidget(self.label_40)

        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(251, 61))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.frame_38)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 9, 641, 38))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_pesquisar = QLabel(self.frame)
        self.label_pesquisar.setObjectName(u"label_pesquisar")
        self.label_pesquisar.setMinimumSize(QSize(233, 13))
        self.label_pesquisar.setStyleSheet(u"font: 10pt \"Sitka\";")

        self.horizontalLayout_8.addWidget(self.label_pesquisar)

        self.input_pesquisar = QLineEdit(self.frame)
        self.input_pesquisar.setObjectName(u"input_pesquisar")
        self.input_pesquisar.setMinimumSize(QSize(233, 20))
        self.input_pesquisar.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(200, 200, 118) ;\n"
"border-radius: 5px;")

        self.horizontalLayout_8.addWidget(self.input_pesquisar)


        self.verticalLayout_16.addWidget(self.frame_38)


        self.verticalLayout_41.addWidget(self.frame_37)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tableWidget = QTableWidget(self.tab_2)
        if (self.tableWidget.columnCount() < 9):
            self.tableWidget.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTableWidget{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(162)

        self.horizontalLayout_4.addWidget(self.tableWidget)

        self.frame_4 = QFrame(self.tab_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.btn_alterar = QPushButton(self.frame_4)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(153, 30))
        self.btn_alterar.setMaximumSize(QSize(153, 16777215))
        self.btn_alterar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar.setStyleSheet(u"\n"
"border:1px solid rgb(200, 200, 118) ;\n"
"border-radius: 5px;")

        self.verticalLayout_9.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame_4)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setEnabled(True)
        self.btn_excluir.setMinimumSize(QSize(153, 30))
        self.btn_excluir.setMaximumSize(QSize(153, 16777215))
        self.btn_excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir.setStyleSheet(u"\n"
"border:1px solid rgb(200, 200, 118) ;\n"
"border-radius: 5px;")

        self.verticalLayout_9.addWidget(self.btn_excluir)

        self.btn_relatorio_pdf = QPushButton(self.frame_4)
        self.btn_relatorio_pdf.setObjectName(u"btn_relatorio_pdf")
        self.btn_relatorio_pdf.setMinimumSize(QSize(153, 30))
        self.btn_relatorio_pdf.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_relatorio_pdf.setStyleSheet(u"\n"
"border:1px solid rgb(200, 200, 118) ;\n"
"border-radius: 5px;")

        self.verticalLayout_9.addWidget(self.btn_relatorio_pdf)

        self.btn_relatorio_excel_2 = QPushButton(self.frame_4)
        self.btn_relatorio_excel_2.setObjectName(u"btn_relatorio_excel_2")
        self.btn_relatorio_excel_2.setMinimumSize(QSize(153, 30))
        self.btn_relatorio_excel_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_relatorio_excel_2.setStyleSheet(u"\n"
"border:1px solid rgb(200, 200, 118) ;\n"
"border-radius: 5px;")

        self.verticalLayout_9.addWidget(self.btn_relatorio_excel_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)


        self.horizontalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_41.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_8.addWidget(self.tabWidget)

        self.Paginas.addWidget(self.pagina_cadastrar)
        self.pagina_inicial = QWidget()
        self.pagina_inicial.setObjectName(u"pagina_inicial")
        self.verticalLayout_7 = QVBoxLayout(self.pagina_inicial)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.logo = QLabel(self.pagina_inicial)
        self.logo.setObjectName(u"logo")
        self.logo.setStyleSheet(u"\n"
"	background-color: rgb(220, 220, 130);")
        self.logo.setPixmap(QPixmap(u"icons/logo1.png.png"))

        self.verticalLayout_7.addWidget(self.logo, 0, Qt.AlignHCenter)

        self.Paginas.addWidget(self.pagina_inicial)
        self.pagina_contato = QWidget()
        self.pagina_contato.setObjectName(u"pagina_contato")
        self.verticalLayout_15 = QVBoxLayout(self.pagina_contato)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_36 = QFrame(self.pagina_contato)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_36)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_38 = QLabel(self.frame_36)
        self.label_38.setObjectName(u"label_38")
        font3 = QFont()
        font3.setFamilies([u"Sitka"])
        font3.setPointSize(50)
        self.label_38.setFont(font3)

        self.verticalLayout_39.addWidget(self.label_38)


        self.verticalLayout_15.addWidget(self.frame_36)

        self.frame_8 = QFrame(self.pagina_contato)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_8)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setPixmap(QPixmap(u"icons/github (1).png"))

        self.verticalLayout_13.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.label_5 = QLabel(self.frame_8)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_13.addWidget(self.label_5)


        self.verticalLayout_15.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.pagina_contato)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_9)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_10 = QLabel(self.frame_9)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setPixmap(QPixmap(u"icons/e-mail.png"))

        self.verticalLayout_14.addWidget(self.label_10, 0, Qt.AlignHCenter)

        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_14.addWidget(self.label_11)


        self.verticalLayout_15.addWidget(self.frame_9)

        self.Paginas.addWidget(self.pagina_contato)
        self.pagina_sobre_2 = QWidget()
        self.pagina_sobre_2.setObjectName(u"pagina_sobre_2")
        self.verticalLayout_11 = QVBoxLayout(self.pagina_sobre_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_7 = QLabel(self.pagina_sobre_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_11.addWidget(self.label_7)

        self.label_8 = QLabel(self.pagina_sobre_2)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_11.addWidget(self.label_8)

        self.Paginas.addWidget(self.pagina_sobre_2)

        self.verticalLayout_6.addWidget(self.Paginas)


        self.verticalLayout.addWidget(self.main_fram)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, 0, 0)
        self.label_2 = QLabel(self.footer_frame)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setFamilies([u"Sitka Small"])
        font4.setPointSize(11)
        self.label_2.setFont(font4)

        self.horizontalLayout_5.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1864, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.Paginas.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"codeds", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.btn_contratos.setText(QCoreApplication.translate("MainWindow", u"CONTATOS", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.botao_menu.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"SISTEMA DE CADASTRO", None))
        self.label_9.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"NOME", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"ESPECIE", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"RA\u00c7A", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"COR", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"IDADE", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"PESO", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"SEXO", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"PORTE", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"SITUA\u00c7\u00c2O", None))
        self.btn_cadastrar_4.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR ANIMAL", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CONSULTA", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"ANIMAIS CADASTRADOS", None))
        self.label_pesquisar.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ESPECIE", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"RA\u00c7A", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"COR", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"IDADE", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"PESO", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"SEXO", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"SITUA\u00c7\u00c2O", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"PORTE", None));
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"ALTERAR", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None))
        self.btn_relatorio_pdf.setText(QCoreApplication.translate("MainWindow", u"RELATORIO - PDF", None))
        self.btn_relatorio_excel_2.setText(QCoreApplication.translate("MainWindow", u"RELATORIO - EXCEL", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"CONSULTAR", None))
        self.logo.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">CONTATO</p></body></html>", None))
        self.label_6.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">github.com/diegoodss</p></body></html>", None))
        self.label_10.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">diegosantossilva094@gmail.com</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">SOBRE O TEXTO </p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">SOBRE</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u00a9 Codeds 2023", None))
    # retranslateUi

