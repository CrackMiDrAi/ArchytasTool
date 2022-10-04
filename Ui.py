class Ui_MainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowFlags(Qt.FramelessWindowHint)  # 去边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 背景透明
        self.setObjectName(u"MainUI")
        self.resize(621, 457)
        self.setStyleSheet(u"")
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.closebtn = QPushButton(self.centralwidget)
        self.closebtn.setObjectName(u"closebtn")
        self.closebtn.setGeometry(QRect(550, 30, 21, 21))
        self.closebtn.setStyleSheet(u"QPushButton{\n"
                                    "    background:#CE0000;\n"
                                    "    color:white;\n"
                                    "    font-size:16px;border-radius: 8px;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "    background:#FF2D2D;\n"
                                    "}\n"
                                    "QPushButton:pressed{\n"
                                    "    border: 1px solid #3C3C3C!important;\n"
                                    "}")
        self.minisize = QPushButton(self.centralwidget)
        self.minisize.setObjectName(u"minisize")
        self.minisize.setGeometry(QRect(520, 30, 21, 21))
        self.minisize.setStyleSheet(u"QPushButton{\n"
                                    "    background:#6C6C6C;\n"
                                    "    color:white;\n"
                                    "    font-size:16px;border-radius: 8px;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "    background:#9D9D9D;\n"
                                    "}\n"
                                    "QPushButton:pressed{\n"
                                    "    border: 1px solid #3C3C3C!important;\n"
                                    "}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-10, -50, 641, 571))
        self.label.setPixmap(QPixmap(u":/res/Background.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(80, 60, 121, 31))
        self.checkBox.setStyleSheet(u"QCheckBox {\n"
                                    "	padding:2px;\n"
                                    "	font:16px \"Microsoft YaHei\";\n"
                                    "}\n"
                                    "QCheckBox:hover {\n"
                                    "	border:1px solid rgb(255,150,60);\n"
                                    "	border-radius:4px;\n"
                                    "	padding: 1px;\n"
                                    "	background-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(190, 90, 50, 50), stop:1 rgba(250, 130, 40, 50));\n"
                                    "}\n"
                                    "QCheckBox::indicator:checked {\n"
                                    "	border:1px solid rgb(246, 134, 86);\n"
                                    "	border-radius:4px;\n"
                                    "  	background-color:rgb(246, 134, 86)\n"
                                    "}\n"
                                    "QCheckBox::indicator:unchecked {\n"
                                    "	border-width:1px solid rgb(246, 134, 86);\n"
                                    "	border-radius:4px;\n"
                                    "  	background-color:rgb(255,255,255);\n"
                                    "}")
        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(80, 140, 121, 31))
        self.checkBox_2.setStyleSheet(u"QCheckBox {\n"
                                      "	padding:2px;\n"
                                      "	font:16px \"Microsoft YaHei\";\n"
                                      "}\n"
                                      "QCheckBox:hover {\n"
                                      "	border:1px solid rgb(255,150,60);\n"
                                      "	border-radius:4px;\n"
                                      "	padding: 1px;\n"
                                      "	background-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(190, 90, 50, 50), stop:1 rgba(250, 130, 40, 50));\n"
                                      "}\n"
                                      "QCheckBox::indicator:checked {\n"
                                      "	border:1px solid rgb(246, 134, 86);\n"
                                      "	border-radius:4px;\n"
                                      "  	background-color:rgb(246, 134, 86)\n"
                                      "}\n"
                                      "QCheckBox::indicator:unchecked {\n"
                                      "	border-width:1px solid rgb(246, 134, 86);\n"
                                      "	border-radius:4px;\n"
                                      "  	background-color:rgb(255,255,255);\n"
                                      "}")
        self.checkBox_3 = QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(80, 100, 121, 31))
        self.checkBox_3.setStyleSheet(u"QCheckBox {\n"
                                      "	padding:2px;\n"
                                      "	font:16px \"Microsoft YaHei\";\n"
                                      "}\n"
                                      "QCheckBox:hover {\n"
                                      "	border:1px solid rgb(255,150,60);\n"
                                      "	border-radius:4px;\n"
                                      "	padding: 1px;\n"
                                      "	background-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(190, 90, 50, 50), stop:1 rgba(250, 130, 40, 50));\n"
                                      "}\n"
                                      "QCheckBox::indicator:checked {\n"
                                      "	border:1px solid rgb(246, 134, 86);\n"
                                      "	border-radius:4px;\n"
                                      "  	background-color:rgb(246, 134, 86)\n"
                                      "}\n"
                                      "QCheckBox::indicator:unchecked {\n"
                                      "	border-width:1px solid rgb(246, 134, 86);\n"
                                      "	border-radius:4px;\n"
                                      "  	background-color:rgb(255,255,255);\n"
                                      "}")
        self.checkBox_4 = QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(80, 180, 201, 31))
        self.checkBox_4.setStyleSheet(u"QCheckBox {\n"
                                      "	padding:2px;\n"
                                      "	font:16px \"Microsoft YaHei\";\n"
                                      "}\n"
                                      "QCheckBox:hover {\n"
                                      "	border:1px solid rgb(255,150,60);\n"
                                      "	border-radius:4px;\n"
                                      "	padding: 1px;\n"
                                      "	background-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(190, 90, 50, 50), stop:1 rgba(250, 130, 40, 50));\n"
                                      "}\n"
                                      "QCheckBox::indicator:checked {\n"
                                      "	border:1px solid rgb(246, 134, 86);\n"
                                      "	border-radius:4px;\n"
                                      "  	background-color:rgb(246, 134, 86)\n"
                                      "}\n"
                                      "QCheckBox::indicator:unchecked {\n"
                                      "	border-width:1px solid rgb(246, 134, 86);\n"
                                      "	border-radius:4px;\n"
                                      "  	background-color:rgb(255,255,255);\n"
                                      "}")
        self.checkBox_5 = QCheckBox(self.centralwidget)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setGeometry(QRect(80, 220, 151, 31))
        self.checkBox_5.setStyleSheet(u"QCheckBox {\n"
                                      "	padding:2px;\n"
                                      "	font:16px \"Microsoft YaHei\";\n"
                                      "}\n"
                                      "QCheckBox:hover {\n"
                                      "	border:1px solid rgb(255,150,60);\n"
                                      "	border-radius:4px;\n"
                                      "	padding: 1px;\n"
                                      "	background-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(190, 90, 50, 50), stop:1 rgba(250, 130, 40, 50));\n"
                                      "}\n"
                                      "QCheckBox::indicator:checked {\n"
                                      "	border:1px solid rgb(246, 134, 86);\n"
                                      "	border-radius:4px;\n"
                                      "  	background-color:rgb(246, 134, 86)\n"
                                      "}\n"
                                      "QCheckBox::indicator:unchecked {\n"
                                      "	border-width:1px solid rgb(246, 134, 86);\n"
                                      "	border-radius:4px;\n"
                                      "  	background-color:rgb(255,255,255);\n"
                                      "}")
        self.checkBox_6 = QCheckBox(self.centralwidget)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setGeometry(QRect(80, 260, 211, 31))
        self.checkBox_6.setStyleSheet(u"QCheckBox {\n"
                                      "	padding:2px;\n"
                                      "	font:16px \"Microsoft YaHei\";\n"
                                      "}\n"
                                      "QCheckBox:hover {\n"
                                      "	border:1px solid rgb(255,150,60);\n"
                                      "	border-radius:4px;\n"
                                      "	padding: 1px;\n"
                                      "	background-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(190, 90, 50, 50), stop:1 rgba(250, 130, 40, 50));\n"
                                      "}\n"
                                      "QCheckBox::indicator:checked {\n"
                                      "	border:1px solid rgb(246, 134, 86);\n"
                                      "	border-radius:4px;\n"
                                      "  	background-color:rgb(246, 134, 86)\n"
                                      "}\n"
                                      "QCheckBox::indicator:unchecked {\n"
                                      "	border-width:1px solid rgb(246, 134, 86);\n"
                                      "	border-radius:4px;\n"
                                      "  	background-color:rgb(255,255,255);\n"
                                      "}")
        self.checkBox_7 = QCheckBox(self.centralwidget)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setGeometry(QRect(80, 300, 151, 31))
        self.checkBox_7.setStyleSheet(u"QCheckBox {\n"
                                      "	padding:2px;\n"
                                      "	font:16px \"Microsoft YaHei\";\n"
                                      "}\n"
                                      "QCheckBox:hover {\n"
                                      "	border:1px solid rgb(255,150,60);\n"
                                      "	border-radius:4px;\n"
                                      "	padding: 1px;\n"
                                      "	background-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(190, 90, 50, 50), stop:1 rgba(250, 130, 40, 50));\n"
                                      "}\n"
                                      "QCheckBox::indicator:checked {\n"
                                      "	border:1px solid rgb(246, 134, 86);\n"
                                      "	border-radius:4px;\n"
                                      "  	background-color:rgb(246, 134, 86)\n"
                                      "}\n"
                                      "QCheckBox::indicator:unchecked {\n"
                                      "	border-width:1px solid rgb(246, 134, 86);\n"
                                      "	border-radius:4px;\n"
                                      "  	background-color:rgb(255,255,255);\n"
                                      "}")
        self.checkBox_8 = QCheckBox(self.centralwidget)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setGeometry(QRect(80, 340, 121, 31))
        self.checkBox_8.setStyleSheet(u"QCheckBox {\n"
                                      "	padding:2px;\n"
                                      "	font:16px \"Microsoft YaHei\";\n"
                                      "}\n"
                                      "QCheckBox:hover {\n"
                                      "	border:1px solid rgb(255,150,60);\n"
                                      "	border-radius:4px;\n"
                                      "	padding: 1px;\n"
                                      "	background-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(190, 90, 50, 50), stop:1 rgba(250, 130, 40, 50));\n"
                                      "}\n"
                                      "QCheckBox::indicator:checked {\n"
                                      "	border:1px solid rgb(246, 134, 86);\n"
                                      "	border-radius:4px;\n"
                                      "  	background-color:rgb(246, 134, 86)\n"
                                      "}\n"
                                      "QCheckBox::indicator:unchecked {\n"
                                      "	border-width:1px solid rgb(246, 134, 86);\n"
                                      "	border-radius:4px;\n"
                                      "  	background-color:rgb(255,255,255);\n"
                                      "}")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(350, 80, 211, 291))
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
                                        "	border: 2px solid rgb(163, 140, 255);\n"
                                        "	border-radius: 5px;	\n"
                                        "	background-color:rgb(163, 140, 255);\n"
                                        "	color:gray;\n"
                                        "	font:44px \"Microsoft YaHei\";\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "	background-color: rgb(163, 140, 247);\n"
                                        "	border: 2px solid rgb(163, 140, 247);\n"
                                        "}\n"
                                        "QPushButton:pressed {	\n"
                                        "	background-color: rgb(163, 140, 238);\n"
                                        "	border: 2px solid rgb(163, 140, 238);\n"
                                        "}")
        self.checkBox_9 = QCheckBox(self.centralwidget)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setGeometry(QRect(80, 380, 121, 31))
        self.checkBox_9.setStyleSheet(u"QCheckBox {\n"
                                      "	padding:2px;\n"
                                      "	font:16px \"Microsoft YaHei\";\n"
                                      "}\n"
                                      "QCheckBox:hover {\n"
                                      "	border:1px solid rgb(255,150,60);\n"
                                      "	border-radius:4px;\n"
                                      "	padding: 1px;\n"
                                      "	background-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(190, 90, 50, 50), stop:1 rgba(250, 130, 40, 50));\n"
                                      "}\n"
                                      "QCheckBox::indicator:checked {\n"
                                      "	border:1px solid rgb(246, 134, 86);\n"
                                      "	border-radius:4px;\n"
                                      "  	background-color:rgb(246, 134, 86)\n"
                                      "}\n"
                                      "QCheckBox::indicator:unchecked {\n"
                                      "	border-width:1px solid rgb(246, 134, 86);\n"
                                      "	border-radius:4px;\n"
                                      "  	background-color:rgb(255,255,255);\n"
                                      "}")
        self.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.closebtn.raise_()
        self.minisize.raise_()
        self.checkBox.raise_()
        self.checkBox_2.raise_()
        self.checkBox_3.raise_()
        self.checkBox_4.raise_()
        self.checkBox_5.raise_()
        self.checkBox_6.raise_()
        self.checkBox_7.raise_()
        self.checkBox_8.raise_()
        self.pushButton_4.raise_()
        self.checkBox_9.raise_()

        self.retranslateUi(self)
        self.closebtn.clicked.connect(self.centralwidget.close)
        self.minisize.clicked.connect(self.centralwidget.showMinimized)
        self.pushButton_4.clicked.connect(self.slot1)

    def slot1(self):
        storea = self.checkBox.isChecked()
        dUPDATEa = self.checkBox_2.isChecked()
        eUPDATEa = self.checkBox_3.isChecked()
        pkginstallera = self.checkBox_4.isChecked()
        buildpropa = self.checkBox_5.isChecked()
        uninstallLaunchera = self.checkBox_9.isChecked()
        InstallLaunchera = self.checkBox_6.isChecked()
        VIAa = self.checkBox_7.isChecked()
        Magiska = self.checkBox_8.isChecked()
        StartThread = threading.Thread(target=START, args=(
        storea, dUPDATEa, eUPDATEa, pkginstallera, buildpropa, uninstallLaunchera, InstallLaunchera, VIAa, Magiska))
        StartThread.start()

        QMetaObject.connectSlotsByName(self)
        # setupUi

    def retranslateUi(self, MainUI):
        MainUI.setWindowTitle(QCoreApplication.translate("MainUI", u"Archytas_tool", None))
        self.closebtn.setText("")
        self.minisize.setText("")
        self.label.setText("")
        self.checkBox.setText(QCoreApplication.translate("MainUI", u"\u66ff\u6362\u5e94\u7528\u5546\u5e97", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainUI", u"\u542f\u7528\u7cfb\u7edf\u66f4\u65b0", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainUI", u"\u7981\u7528\u7cfb\u7edf\u66f4\u65b0", None))
        self.checkBox_4.setText(
            QCoreApplication.translate("MainUI", u"\u5b89\u88c5\u539f\u751f\u8f6f\u4ef6\u5305\u5b89\u88c5\u7a0b\u5e8f",
                                       None))
        self.checkBox_5.setText(QCoreApplication.translate("MainUI", u"\u66ff\u6362 build.prop", None))
        self.checkBox_6.setText(
            QCoreApplication.translate("MainUI", u"\u5b89\u88c5\u7cfb\u7edf\u684c\u9762/\u542f\u7528\u8d1f\u4e00\u5c4f",
                                       None))
        self.checkBox_7.setText(QCoreApplication.translate("MainUI", u"\u5b89\u88c5 Via \u6d4f\u89c8\u5668", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainUI", u"\u5237\u5165 Magisk", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainUI", u"\u542f\u52a8\n"
                                                                       "START", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainUI", u"\u5378\u8f7d\u7cfb\u7edf\u684c\u9762", None))

    # retranslateUi

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = e.globalPos() - self.pos()
            e.accept()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = False

    def mouseMoveEvent(self, e):
        try:
            if Qt.LeftButton and self.m_drag:
                self.move(e.globalPos() - self.m_DragPosition)
                e.accept()
        except Exception:
            pass