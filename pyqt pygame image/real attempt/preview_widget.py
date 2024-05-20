# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerLMcljh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from redegswidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(463, 324)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.startButton = QPushButton(Form)
        self.startButton.setObjectName(u"startButton")

        self.horizontalLayout.addWidget(self.startButton)

        self.resolutionComboBox = QComboBox(Form)
        self.resolutionComboBox.setObjectName(u"resolutionComboBox")

        self.horizontalLayout.addWidget(self.resolutionComboBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pygameWidget = PygameWidget(self.groupBox)
        self.pygameWidget.setObjectName(u"pygameWidget")

        self.horizontalLayout_2.addWidget(self.pygameWidget)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.startButton.setText(QCoreApplication.translate("Form", u"Play", None))
        self.resolutionComboBox.setCurrentText("")
        self.resolutionComboBox.setPlaceholderText(QCoreApplication.translate("Form", u"Preview Resolution", None))
    # retranslateUi
