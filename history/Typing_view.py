# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Typing_view.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Typing(object):
    def setupUi(self, Typing):
        if not Typing.objectName():
            Typing.setObjectName(u"Typing")
        Typing.resize(725, 269)
        self.label = QLabel(Typing)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 40, 55, 16))
        self.Text = QLineEdit(Typing)
        self.Text.setObjectName(u"Text")
        self.Text.setEnabled(True)
        self.Text.setGeometry(QRect(30, 60, 661, 31))
        self.label_2 = QLabel(Typing)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 110, 55, 16))
        self.label_3 = QLabel(Typing)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 180, 55, 16))
        self.Enter = QLineEdit(Typing)
        self.Enter.setObjectName(u"Enter")
        self.Enter.setEnabled(True)
        self.Enter.setGeometry(QRect(30, 130, 661, 31))
        self.Sms = QLineEdit(Typing)
        self.Sms.setObjectName(u"Sms")
        self.Sms.setEnabled(True)
        self.Sms.setGeometry(QRect(30, 200, 661, 31))
        self.timeEdit = QTimeEdit(Typing)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(600, 20, 61, 21))
        self.timeEdit.setReadOnly(True)
        self.timeEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.retranslateUi(Typing)

        QMetaObject.connectSlotsByName(Typing)
    # setupUi

    def retranslateUi(self, Typing):
        Typing.setWindowTitle(QCoreApplication.translate("Typing", u"Form", None))
        self.label.setText(QCoreApplication.translate("Typing", u"Text", None))
        self.label_2.setText(QCoreApplication.translate("Typing", u"Enter", None))
        self.label_3.setText(QCoreApplication.translate("Typing", u"Sms", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("Typing", u"HH:mm:ss", None))
    # retranslateUi

