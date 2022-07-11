# coding = utf-8
import os
import sys
import urllib.request
from multiprocessing import Process
import threading
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtGui import QCloseEvent
import RCMain


###########################################################################################################


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


localVer = 3.9


def adv():
    global choiceadv
    choiceadv = input(
        "A.安装自定义应用为系统应用（priv-app）\nB.安装自定义应用为系统应用（app）\nC.卸载系统应用（priv-app）\nD.卸载系统应用（app）\nE.推送指定文件到 /sdcard（内部储存根目录）\n0.返回主页\n------------------------\n请输入序号（不区分大小写，可多选）：")
    choiceadv = choiceadv.lower()

    if "a" in choiceadv:
        print("\n安装自定义应用为系统应用（priv-app）")
        apkpath = input("请拖入需要安装的 apk：")
        os.system("adb push " + apkpath + " /system/priv-app")

    if "b" in choiceadv:
        print("\n安装自定义应用为系统应用（app）")
        apkpath = input("请拖入需要安装的 apk：")
        os.system("adb push " + apkpath + " /system/app")

    if "c" in choiceadv:
        print("\n卸载系统应用（priv-app）")
        os.system("adb shell")
        os.system("cd /system/priv-app")
        os.system("ls")
        apkpath = input("请输入需要删除的文件/文件夹名：")
        os.system("rm -r " + apkpath)
        os.system("exit")

    if "d" in choiceadv:
        print("\n卸载系统应用（app）")
        os.system("adb shell")
        os.system("cd /system/app")
        os.system("ls")
        apkpath = input("请输入需要删除的文件/文件夹名：")
        os.system("rm -r " + apkpath)
        os.system("exit")

    if "e" in choiceadv:
        print("\n推送指定文件到 /sdcard")
        filepath = input("请输入需要推送文件的路径（可拖动）并回车：")
        os.system("adb push " + filepath + " /sdcard")

    print("------------------------")


def doAgain(mode):
    doAgainChoice = input("执行完成，您是否需要再次执行？（y/n）：")
    doAgainChoice = doAgainChoice.lower()
    if doAgainChoice == "y":
        print("------------------------")
        if mode == 0:
            adv()
        else:
            main()
    elif doAgainChoice == "n":
        if mode == 0:
            main()
        else:
            return 0
    else:
        print("输入错误！")
        doAgain(mode)


def Store():
    print("正在替换应用商店..")
    os.system("adb push files/MiStore.apk /system/priv-app/MiStore")
    print("完成\n")


def delUpdator():
    print("正在删除更新程序...")
    os.system("adb shell rm -r /system/priv-app/MiSysUpdator")
    print("完成\n")


def pushUpdator():
    print("正在推送更新程序...")
    os.system("adb push files/MiSysUpdator.apk /system/priv-app")
    print("完成\n")


def installPackage():
    print("正在安装原生软件包安装程序...")
    os.system("adb push files/MiPackageInstaller.apk /system/priv-app/MiPackageInstaller")
    print("完成\n")


def installSetting():
    print("正在安装旧版设置...")
    os.system("adb push files/MiSettings.apk /system/priv-app/MiSettings")
    print("完成\n")


def lowRam():
    print("正在替换 build.prop...")
    os.system("adb push files/build.prop /system")
    print("完成\n")


def delLauncher():
    print("正在卸载默认桌面...")
    os.system("adb shell rm -r /system/priv-app/MiLauncher")
    print("完成\n")


def installLauncher():
    print("正在安装默认桌面...")
    os.system("adb push files/MiLauncher.apk /system/priv-app")
    print("完成\n")


def installVia():
    print("正在安装 Via 浏览器...")
    os.system("adb push files/via.apk /system/priv-app")
    print("完成\n")


def enableWallpaper():
    print("正在启用壁纸服务...")
    os.system("adb push files/framework-res.apk /system/framework")
    os.system("adb shell chmod 644 /system/framework/framework-res.apk")
    print("完成\n")


def flashMagisk():
    input("请进入 高级 -> Adb Sideload -> 滑动滑块，完成后回车...")
    print("正在刷入...")
    os.system("adb sideload files/Magisk-Canary-23016.zip")
    print("完成\n")


def START(store, dUPDATE, eUPDATE, pkginstaller, buildprop, uninstallLauncher, InstallLauncher, VIA, Magisk):
    if store == True:
        Store()
    if dUPDATE == True:
        delUpdator()
    if eUPDATE == True:
        pushUpdator()
    if pkginstaller == True:
        installPackage()
    if buildprop == True:
        lowRam()
    if uninstallLauncher == True:
        delLauncher()
    if InstallLauncher == True:
        installLauncher()
    if VIA == True:
        installVia()
    if Magisk == True:
        flashMagisk()


if not os.path.exists("adb.exe"):
    print("请解压后运行！\n------------------------")
    os.system("pause")
    sys.exit()


def main():
    advUsed = 0
    choice = input("""A.替换应用商店（可防止第三方 app 被删除，由 @xluzo 修改）
    B.关闭系统更新
    C.启用系统更新
    D.安装原生软件包安装程序（可直接安装第三方 app）
    E.安装旧版设置（支持开发者选项）
    F.关闭 lowram 模式（可获取通知使用权、修改堆叠后台）
    G.卸载默认桌面（请确定已安装可使用的第三方桌面）
    H.恢复默认桌面并启用负一屏
    I.安装 Via 浏览器
    J.启用壁纸服务（不稳定且有变砖风险，可使用第三方启动器）
    K.刷入 Magisk
    0.一键执行首次破解的推荐操作
    1.高级选项
    2.退出程序
    3.检查更新
    ------------------------
    请输入序号（不区分大小写，可多选）：""")
    choice = choice.lower()
    print("------------------------")

    if "2" in choice:
        return 0
    if "3" in choice:
        choice = "3"
        ver = float(urllib.request.urlopen("https://rponeawa.github.io/ArchytasToolVer/ver").read().decode("utf-8"))
        if localVer < ver:
            input("检查到新版本，回车以前往下载...")
            os.system("start https://github.com/CrackMiDrAi/ArchytasTool/releases")
        else:
            print("您使用的是最新版本！")
    if "1" in choice:
        print("高级选项（不建议小白使用，变砖不负责）")
        adv()
        advUsed = 1
        if "0" not in choiceadv:
            doAgain(0)
    if "0" in choice:
        choice = "adefik"
        print("正在执行推荐操作...\n")
    if "a" in choice:
        Store()
    if "b" in choice:
        delUpdator()
    if "c" in choice:
        pushUpdator()
    if "d" in choice:
        installPackage()
    if "e" in choice:
        installSetting()
    if "f" in choice:
        lowRam()
    if "g" in choice:
        delLauncher()
    if "h" in choice:
        installLauncher()
    if "i" in choice:
        installVia()
    if "j" in choice:
        enableWallpaper()
    if "k" in choice:
        flashMagisk()
    print("------------------------")
    if advUsed == 1:
        if "0" in choiceadv:
            main()
        else:
            doAgain(1)
    else:
        doAgain(1)


def GUIstarter():
    app = QApplication(sys.argv)
    ui = Ui_MainUI()
    ui.show()
    app.exec_()


def RUNNER():
    global f
    print("Tool by @rpone && @Hotspring\n---------")
    print("请在关机后按住 电源键+复读键+红键+音量上键 以进入 TWRP Recovery 并挂载 System 分区")
    print("检查连接状态...\n------------------------\n")
    f = os.popen(r"adb devices", "r")
    output = f.read()
    f.close()
    s = output.split("\n")
    new = [x for x in s if x != '']
    devices = []
    for i in new:
        dev = i.split('\trecovery')
        if len(dev) >= 2:
            devices.append(dev[0])
    if not devices:
        print("设备未连接！\n\n------------------------")
        os.system("pause")
        sys.exit()
    else:
        print("当前连接设备:%s" % str(devices) + "\n")
    print("------------------------")
    Console_Process = Process(target=main)  # 实例化console
    GUI_Process = Process(target=GUIstarter)  # 实例化GUI
    GUI_Process.start()
    Console_Process.start()


if __name__ == '__main__':
    RUNNER()
