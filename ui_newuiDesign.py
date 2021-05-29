# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newuiDesignhbsrjX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(989, 539)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"\n"
"border:none;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.BaseFrame = QFrame(self.centralwidget)
        self.BaseFrame.setObjectName(u"BaseFrame")
        self.BaseFrame.setStyleSheet(u"background-color: rgb(18, 19, 25);")
        self.BaseFrame.setFrameShape(QFrame.StyledPanel)
        self.BaseFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.BaseFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Titlebar = QFrame(self.BaseFrame)
        self.Titlebar.setObjectName(u"Titlebar")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Titlebar.sizePolicy().hasHeightForWidth())
        self.Titlebar.setSizePolicy(sizePolicy)
        self.Titlebar.setMinimumSize(QSize(0, 24))
        self.Titlebar.setMaximumSize(QSize(16777215, 31))
        self.Titlebar.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"border-top-right-radius:8px;\n"
"border-top-left-radius:8px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
"	background-color: rgb(30, 31, 41);\n"
"\n"
"}")
        self.Titlebar.setFrameShape(QFrame.NoFrame)
        self.Titlebar.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_2 = QHBoxLayout(self.Titlebar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.QSizeGrip_top_left = QFrame(self.Titlebar)
        self.QSizeGrip_top_left.setObjectName(u"QSizeGrip_top_left")
        self.QSizeGrip_top_left.setMinimumSize(QSize(10, 0))
        self.QSizeGrip_top_left.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.QSizeGrip_top_left.setFrameShape(QFrame.StyledPanel)
        self.QSizeGrip_top_left.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_2.addWidget(self.QSizeGrip_top_left)

        self.DragFrameTop = QFrame(self.Titlebar)
        self.DragFrameTop.setObjectName(u"DragFrameTop")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.DragFrameTop.sizePolicy().hasHeightForWidth())
        self.DragFrameTop.setSizePolicy(sizePolicy1)
        self.DragFrameTop.setStyleSheet(u"border-radius:none;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"")
        self.DragFrameTop.setFrameShape(QFrame.StyledPanel)
        self.DragFrameTop.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.DragFrameTop)

        self.UtilityButtonsFrame = QFrame(self.Titlebar)
        self.UtilityButtonsFrame.setObjectName(u"UtilityButtonsFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.UtilityButtonsFrame.sizePolicy().hasHeightForWidth())
        self.UtilityButtonsFrame.setSizePolicy(sizePolicy2)
        self.UtilityButtonsFrame.setStyleSheet(u"border-radius:none;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.UtilityButtonsFrame.setFrameShape(QFrame.StyledPanel)
        self.UtilityButtonsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.UtilityButtonsFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.MiniButton = QPushButton(self.UtilityButtonsFrame)
        self.MiniButton.setObjectName(u"MiniButton")
        self.MiniButton.setMinimumSize(QSize(32, 17))
        self.MiniButton.setStyleSheet(u"QPushButton {\n"
"    qproperty-icon: url(\" \"); /* empty image */\n"
"    qproperty-iconSize: 20px 20px; /* space for the background image */\n"
"border:none;\n"
"\n"
"	background-image: url(:/newPrefix/Utility Icons/minimize_focused_normal.png);\n"
"background-position:centre-bottom;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"	background-image: url(:/newPrefix/Utility Icons/minimize_unfocused_pressed.png);\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"\n"
"	background-image: url(:/newPrefix/Utility Icons/shade_unfocused.png);\n"
"\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/newPrefix/Utility Icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MiniButton.setIcon(icon)
        self.MiniButton.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.MiniButton)

        self.MaxiButton = QPushButton(self.UtilityButtonsFrame)
        self.MaxiButton.setObjectName(u"MaxiButton")
        self.MaxiButton.setMinimumSize(QSize(32, 17))
        self.MaxiButton.setStyleSheet(u"QPushButton {\n"
"    qproperty-icon: url(\" \"); /* empty image */\n"
"  qproperty-iconSize: 20px 20px;/* space for the background image */\n"
"\n"
"border:none;\n"
"\n"
"	background-image: url(:/newPrefix/Utility Icons/maximize_focused_normal.png);\n"
"background-position:centre-bottom;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"	background-image: url(:/newPrefix/Utility Icons/maximize_focused_prelight.png);\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"\n"
"	background-image: url(:/newPrefix/Utility Icons/shade_unfocused.png);\n"
"\n"
"}")
        self.MaxiButton.setIcon(icon)
        self.MaxiButton.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.MaxiButton)

        self.CloseButton = QPushButton(self.UtilityButtonsFrame)
        self.CloseButton.setObjectName(u"CloseButton")
        self.CloseButton.setMinimumSize(QSize(32, 17))
        self.CloseButton.setStyleSheet(u"QPushButton {\n"
"    qproperty-icon: url(\" \"); /* empty image */\n"
"   qproperty-iconSize: 20px 20px; /* space for the background image */\n"
"border:none;\n"
"\n"
"\n"
"	background-image: url(:/newPrefix/Utility Icons/close.png);\n"
"background-position:centre-bottom;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"	background-image: url(:/newPrefix/Utility Icons/close_focused_pressed.png);\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"\n"
"	background-image: url(:/newPrefix/Utility Icons/shade_unfocused.png);\n"
"\n"
"}")
        self.CloseButton.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.CloseButton)


        self.horizontalLayout_2.addWidget(self.UtilityButtonsFrame)


        self.verticalLayout_3.addWidget(self.Titlebar)

        self.ContentFrame = QFrame(self.BaseFrame)
        self.ContentFrame.setObjectName(u"ContentFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ContentFrame.sizePolicy().hasHeightForWidth())
        self.ContentFrame.setSizePolicy(sizePolicy3)
        self.ContentFrame.setStyleSheet(u"\n"
"\n"
"QFrame{\n"
"\n"
"\n"
"\n"
"\n"
"}")
        self.ContentFrame.setFrameShape(QFrame.StyledPanel)
        self.ContentFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.ContentFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuFrame = QFrame(self.ContentFrame)
        self.LeftMenuFrame.setObjectName(u"LeftMenuFrame")
        self.LeftMenuFrame.setMinimumSize(QSize(46, 0))
        self.LeftMenuFrame.setStyleSheet(u"QFrame{\n"
"\n"
"	background-color: rgb(21, 22, 29);\n"
"border-bottom-right-radius:7px;\n"
"border-top-right-radius:7px;\n"
"\n"
"}")
        self.LeftMenuFrame.setFrameShape(QFrame.StyledPanel)
        self.LeftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.LeftMenuFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 2)
        self.LeftMenuExpandButton = QPushButton(self.LeftMenuFrame)
        self.LeftMenuExpandButton.setObjectName(u"LeftMenuExpandButton")
        self.LeftMenuExpandButton.setMinimumSize(QSize(0, 32))
        self.LeftMenuExpandButton.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(30, 31, 41);\n"
"	background-color: rgb(19, 20, 26);\n"
"\n"
"border-bottom-right-radius:6px;\n"
"border-bottom-left-radius:6px;\n"
"border-top-right-radius:7px;\n"
"border-top-left-radius:0px;\n"
"\n"
"color:rgba(255,255,255,200);\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"\n"
"background-color: rgba(4, 4, 4, 120);\n"
"\n"
"border-bottom:1px solid rgba(255, 18, 255, 60);\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"\n"
"	background-color: rgb(0, 0, 0);\n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/Utility Icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.LeftMenuExpandButton.setIcon(icon1)
        self.LeftMenuExpandButton.setIconSize(QSize(27, 25))

        self.verticalLayout_4.addWidget(self.LeftMenuExpandButton)

        self.MenuoptionsFrame = QFrame(self.LeftMenuFrame)
        self.MenuoptionsFrame.setObjectName(u"MenuoptionsFrame")
        self.MenuoptionsFrame.setFrameShape(QFrame.StyledPanel)
        self.MenuoptionsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.MenuoptionsFrame)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 2, 0, 0)
        self.Menu1Base = QFrame(self.MenuoptionsFrame)
        self.Menu1Base.setObjectName(u"Menu1Base")
        sizePolicy4 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Menu1Base.sizePolicy().hasHeightForWidth())
        self.Menu1Base.setSizePolicy(sizePolicy4)
        self.Menu1Base.setMinimumSize(QSize(0, 235))
        self.Menu1Base.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(111, 114, 135,100);\n"
"	background-color: rgb(14, 15, 18);\n"
"}")
        self.Menu1Base.setFrameShape(QFrame.StyledPanel)
        self.Menu1Base.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.Menu1Base)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, -1, 0, 19)
        self.frame_2 = QFrame(self.Menu1Base)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(22, 24, 31);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setSpacing(13)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.Home = QFrame(self.frame_2)
        self.Home.setObjectName(u"Home")
        self.Home.setMinimumSize(QSize(171, 41))
        self.Home.setMaximumSize(QSize(16777215, 41))
        self.Home.setStyleSheet(u"QFrame::hover{\n"
"\n"
"background-color: rgba(4, 4, 4, 120);\n"
"\n"
"}\n"
"\n"
"")
        self.Home.setFrameShape(QFrame.StyledPanel)
        self.Home.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.Home)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.HomeButton = QPushButton(self.Home)
        self.HomeButton.setObjectName(u"HomeButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.HomeButton.sizePolicy().hasHeightForWidth())
        self.HomeButton.setSizePolicy(sizePolicy5)
        self.HomeButton.setMinimumSize(QSize(0, 0))
        self.HomeButton.setMaximumSize(QSize(46, 16777215))
        self.HomeButton.setStyleSheet(u"QPushButton{border-top-right-radius:5px;\n"
"border-bottom-right-radius:20px;\n"
"border-top-left-radius:20px;\n"
"border-top-right-radius:0px;\n"
"	background-color: rgb(19, 20, 26);\n"
"border-style:inset;\n"
"border-width:1px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgba(4, 4, 4, 120);\n"
"	border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"\n"
"	border-right-color: rgb(247, 173, 24);\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgba(31, 32, 39,225);\n"
"\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/Utility Icons/lmms.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.HomeButton.setIcon(icon2)
        self.HomeButton.setIconSize(QSize(24, 25))

        self.horizontalLayout_8.addWidget(self.HomeButton)

        self.HomeLabel = QLabel(self.Home)
        self.HomeLabel.setObjectName(u"HomeLabel")
        self.HomeLabel.setMinimumSize(QSize(125, 41))
        font = QFont()
        font.setFamily(u"Quicksand Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.HomeLabel.setFont(font)
        self.HomeLabel.setStyleSheet(u"QLabel{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(216, 216, 216);\n"
"border-bottom-left-radius:20px;\n"
"border-top-right-radius:25px;\n"
"padding-left:8px;\n"
"}\n"
"\n"
"\n"
"QLabel::hover{\n"
"border-left:1px solid rgba(85, 255, 127,170);\n"
"}")

        self.horizontalLayout_8.addWidget(self.HomeLabel)


        self.verticalLayout_6.addWidget(self.Home)

        self.Accounts = QFrame(self.frame_2)
        self.Accounts.setObjectName(u"Accounts")
        self.Accounts.setMinimumSize(QSize(171, 41))
        self.Accounts.setMaximumSize(QSize(16777215, 41))
        self.Accounts.setStyleSheet(u"QFrame::hover{\n"
"\n"
"background-color: rgba(4, 4, 4, 120);\n"
"\n"
"}")
        self.Accounts.setFrameShape(QFrame.StyledPanel)
        self.Accounts.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.Accounts)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.AccountButton = QPushButton(self.Accounts)
        self.AccountButton.setObjectName(u"AccountButton")
        sizePolicy5.setHeightForWidth(self.AccountButton.sizePolicy().hasHeightForWidth())
        self.AccountButton.setSizePolicy(sizePolicy5)
        self.AccountButton.setMinimumSize(QSize(0, 0))
        self.AccountButton.setMaximumSize(QSize(46, 16777215))
        self.AccountButton.setStyleSheet(u"QPushButton{border-top-right-radius:5px;\n"
"border-bottom-right-radius:20px;\n"
"border-top-left-radius:20px;\n"
"border-top-right-radius:0px;\n"
"	background-color: rgb(19, 20, 26);\n"
"border-style:inset;\n"
"border-width:1px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgba(4, 4, 4, 120);\n"
"	border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"\n"
"	border-right-color: rgb(247, 173, 24);\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgba(31, 32, 39,225);\n"
"\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/Utility Icons/preferences-desktop-user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.AccountButton.setIcon(icon3)
        self.AccountButton.setIconSize(QSize(26, 26))

        self.horizontalLayout_9.addWidget(self.AccountButton)

        self.AccountLabel = QLabel(self.Accounts)
        self.AccountLabel.setObjectName(u"AccountLabel")
        self.AccountLabel.setMinimumSize(QSize(125, 41))
        font1 = QFont()
        font1.setFamily(u"Quicksand Medium")
        font1.setPointSize(12)
        self.AccountLabel.setFont(font1)
        self.AccountLabel.setStyleSheet(u"QLabel{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(216, 216, 216);\n"
"border-bottom-left-radius:20px;\n"
"border-top-right-radius:25px;\n"
"padding-left:8px;\n"
"}\n"
"\n"
"\n"
"QLabel::hover{\n"
"border-left:1px solid rgba(85, 255, 127,170);\n"
"}")

        self.horizontalLayout_9.addWidget(self.AccountLabel)


        self.verticalLayout_6.addWidget(self.Accounts)

        self.Contact = QFrame(self.frame_2)
        self.Contact.setObjectName(u"Contact")
        self.Contact.setMinimumSize(QSize(171, 41))
        self.Contact.setMaximumSize(QSize(16777215, 41))
        self.Contact.setStyleSheet(u"QFrame::hover{\n"
"\n"
"background-color: rgba(4, 4, 4, 120);\n"
"\n"
"}")
        self.Contact.setFrameShape(QFrame.StyledPanel)
        self.Contact.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.Contact)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.ContactButton = QPushButton(self.Contact)
        self.ContactButton.setObjectName(u"ContactButton")
        sizePolicy5.setHeightForWidth(self.ContactButton.sizePolicy().hasHeightForWidth())
        self.ContactButton.setSizePolicy(sizePolicy5)
        self.ContactButton.setMinimumSize(QSize(0, 0))
        self.ContactButton.setMaximumSize(QSize(46, 16777215))
        self.ContactButton.setStyleSheet(u"QPushButton{border-top-right-radius:5px;\n"
"border-bottom-right-radius:20px;\n"
"border-top-left-radius:20px;\n"
"border-top-right-radius:0px;\n"
"	background-color: rgb(19, 20, 26);\n"
"border-style:inset;\n"
"border-width:1px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgba(4, 4, 4, 120);\n"
"	border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"\n"
"	border-right-color: rgb(247, 173, 24);\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgba(31, 32, 39,225);\n"
"\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/Utility Icons/smartphone.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ContactButton.setIcon(icon4)
        self.ContactButton.setIconSize(QSize(26, 26))

        self.horizontalLayout_10.addWidget(self.ContactButton)

        self.ContactLabel = QLabel(self.Contact)
        self.ContactLabel.setObjectName(u"ContactLabel")
        self.ContactLabel.setMinimumSize(QSize(125, 41))
        self.ContactLabel.setFont(font1)
        self.ContactLabel.setStyleSheet(u"QLabel{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(216, 216, 216);\n"
"border-bottom-left-radius:20px;\n"
"border-top-right-radius:25px;\n"
"padding-left:8px;\n"
"}\n"
"\n"
"\n"
"QLabel::hover{\n"
"border-left:1px solid rgba(85, 255, 127,170);\n"
"}")

        self.horizontalLayout_10.addWidget(self.ContactLabel)


        self.verticalLayout_6.addWidget(self.Contact)

        self.Browser = QFrame(self.frame_2)
        self.Browser.setObjectName(u"Browser")
        self.Browser.setMinimumSize(QSize(171, 41))
        self.Browser.setMaximumSize(QSize(16777215, 41))
        self.Browser.setStyleSheet(u"QFrame::hover{\n"
"\n"
"background-color: rgba(4, 4, 4, 120);\n"
"\n"
"}")
        self.Browser.setFrameShape(QFrame.StyledPanel)
        self.Browser.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.Browser)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.BrowserButton = QPushButton(self.Browser)
        self.BrowserButton.setObjectName(u"BrowserButton")
        sizePolicy5.setHeightForWidth(self.BrowserButton.sizePolicy().hasHeightForWidth())
        self.BrowserButton.setSizePolicy(sizePolicy5)
        self.BrowserButton.setMinimumSize(QSize(0, 0))
        self.BrowserButton.setMaximumSize(QSize(46, 16777215))
        self.BrowserButton.setStyleSheet(u"QPushButton{border-top-right-radius:5px;\n"
"border-bottom-right-radius:20px;\n"
"border-top-left-radius:20px;\n"
"border-top-right-radius:0px;\n"
"	background-color: rgb(19, 20, 26);\n"
"border-style:inset;\n"
"border-width:1px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgba(4, 4, 4, 120);\n"
"	border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"\n"
"	border-right-color: rgb(247, 173, 24);\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgba(31, 32, 39,225);\n"
"\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/Utility Icons/yast-network-group.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BrowserButton.setIcon(icon5)
        self.BrowserButton.setIconSize(QSize(23, 25))

        self.horizontalLayout_11.addWidget(self.BrowserButton)

        self.BrowserLabel = QLabel(self.Browser)
        self.BrowserLabel.setObjectName(u"BrowserLabel")
        self.BrowserLabel.setMinimumSize(QSize(125, 41))
        self.BrowserLabel.setFont(font1)
        self.BrowserLabel.setStyleSheet(u"QLabel{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(216, 216, 216);\n"
"border-bottom-left-radius:20px;\n"
"border-top-right-radius:25px;\n"
"padding-left:8px;\n"
"}\n"
"\n"
"\n"
"QLabel::hover{\n"
"border-left:1px solid rgba(85, 255, 127,170);\n"
"}")

        self.horizontalLayout_11.addWidget(self.BrowserLabel)


        self.verticalLayout_6.addWidget(self.Browser)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.frame_7 = QFrame(self.Menu1Base)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frame_7)


        self.verticalLayout_5.addWidget(self.Menu1Base)

        self.Menu2Base = QFrame(self.MenuoptionsFrame)
        self.Menu2Base.setObjectName(u"Menu2Base")
        sizePolicy6 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.Menu2Base.sizePolicy().hasHeightForWidth())
        self.Menu2Base.setSizePolicy(sizePolicy6)
        self.Menu2Base.setMinimumSize(QSize(0, 33))
        self.Menu2Base.setStyleSheet(u"")
        self.Menu2Base.setFrameShape(QFrame.StyledPanel)
        self.Menu2Base.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.Menu2Base)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 9, 0)
        self.Settings = QFrame(self.Menu2Base)
        self.Settings.setObjectName(u"Settings")
        self.Settings.setMinimumSize(QSize(171, 41))
        self.Settings.setMaximumSize(QSize(16777215, 41))
        self.Settings.setStyleSheet(u"QFrame::hover{\n"
"\n"
"background-color: rgba(4, 4, 4, 120);\n"
"\n"
"}")
        self.Settings.setFrameShape(QFrame.StyledPanel)
        self.Settings.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.Settings)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.SettingButton = QPushButton(self.Settings)
        self.SettingButton.setObjectName(u"SettingButton")
        sizePolicy5.setHeightForWidth(self.SettingButton.sizePolicy().hasHeightForWidth())
        self.SettingButton.setSizePolicy(sizePolicy5)
        self.SettingButton.setMinimumSize(QSize(0, 0))
        self.SettingButton.setMaximumSize(QSize(46, 16777215))
        self.SettingButton.setStyleSheet(u"QPushButton{border-top-right-radius:5px;\n"
"border-bottom-right-radius:20px;\n"
"border-top-left-radius:20px;\n"
"border-top-right-radius:0px;\n"
"	background-color: rgb(19, 20, 26);\n"
"border-style:inset;\n"
"border-width:1px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgba(4, 4, 4, 120);\n"
"	border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"\n"
"	border-right-color: rgb(247, 173, 24);\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgba(31, 32, 39,225);\n"
"\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/Utility Icons/drive-optical.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.SettingButton.setIcon(icon6)
        self.SettingButton.setIconSize(QSize(23, 25))

        self.horizontalLayout_12.addWidget(self.SettingButton)

        self.SettingsLabel = QLabel(self.Settings)
        self.SettingsLabel.setObjectName(u"SettingsLabel")
        self.SettingsLabel.setMinimumSize(QSize(125, 41))
        self.SettingsLabel.setFont(font1)
        self.SettingsLabel.setStyleSheet(u"QLabel{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(216, 216, 216);\n"
"border-bottom-left-radius:20px;\n"
"border-top-right-radius:25px;\n"
"padding-left:8px;\n"
"}\n"
"\n"
"\n"
"QLabel::hover{\n"
"border-left:1px solid rgba(85, 255, 127,170);\n"
"}")

        self.horizontalLayout_12.addWidget(self.SettingsLabel)


        self.horizontalLayout_13.addWidget(self.Settings)


        self.verticalLayout_5.addWidget(self.Menu2Base)


        self.verticalLayout_4.addWidget(self.MenuoptionsFrame)


        self.horizontalLayout_3.addWidget(self.LeftMenuFrame)

        self.InnerContentFrame = QFrame(self.ContentFrame)
        self.InnerContentFrame.setObjectName(u"InnerContentFrame")
        self.InnerContentFrame.setStyleSheet(u"")
        self.InnerContentFrame.setFrameShape(QFrame.StyledPanel)
        self.InnerContentFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.InnerContentFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 0, 0, 0)
        self.MainContentstackedWidget = QStackedWidget(self.InnerContentFrame)
        self.MainContentstackedWidget.setObjectName(u"MainContentstackedWidget")
        self.MainContentstackedWidget.setMinimumSize(QSize(0, 0))
        self.MainContentstackedWidget.setStyleSheet(u"border-top-right-radius:6px;\n"
"border-bottom-right-radius:6px;")
        self.Browser_Page = QWidget()
        self.Browser_Page.setObjectName(u"Browser_Page")
        self.Browser_Page.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.Browser_Page)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Browser_Page_Base = QFrame(self.Browser_Page)
        self.Browser_Page_Base.setObjectName(u"Browser_Page_Base")
        self.Browser_Page_Base.setStyleSheet(u"\n"
"image:none;\n"
"background-color: qlineargradient(spread:pad, x1:0.61, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 118), stop:1 rgba(0, 0, 0, 198));")
        self.Browser_Page_Base.setFrameShape(QFrame.StyledPanel)
        self.Browser_Page_Base.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.Browser_Page_Base)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.browserWidgets = QWidget(self.Browser_Page_Base)
        self.browserWidgets.setObjectName(u"browserWidgets")
        self.horizontalLayout_7 = QHBoxLayout(self.browserWidgets)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label = QLabel(self.browserWidgets)
        self.label.setObjectName(u"label")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy7)
        self.label.setMinimumSize(QSize(60, 60))
        self.label.setMaximumSize(QSize(60, 60))
        self.label.setStyleSheet(u"border-image: url(:/newPrefix/Utility Icons/globe.svg);")
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label)


        self.horizontalLayout_6.addWidget(self.browserWidgets)


        self.horizontalLayout_5.addWidget(self.Browser_Page_Base)

        self.MainContentstackedWidget.addWidget(self.Browser_Page)
        self.Contact_Page = QWidget()
        self.Contact_Page.setObjectName(u"Contact_Page")
        self.Contact_Page.setStyleSheet(u"image:none;\n"
"background-color: qlineargradient(spread:pad, x1:0.61, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 118), stop:1 rgba(0, 0, 0, 198));")
        self.horizontalLayout_17 = QHBoxLayout(self.Contact_Page)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.Contact_Page_base = QFrame(self.Contact_Page)
        self.Contact_Page_base.setObjectName(u"Contact_Page_base")
        self.Contact_Page_base.setFrameShape(QFrame.StyledPanel)
        self.Contact_Page_base.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.Contact_Page_base)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_2 = QLabel(self.Contact_Page_base)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(60, 60))
        self.label_2.setStyleSheet(u"border-image: url(:/newPrefix/Utility Icons/mail.png);")

        self.horizontalLayout_18.addWidget(self.label_2)


        self.horizontalLayout_17.addWidget(self.Contact_Page_base)

        self.MainContentstackedWidget.addWidget(self.Contact_Page)
        self.Home_Page = QWidget()
        self.Home_Page.setObjectName(u"Home_Page")
        self.Home_Page.setStyleSheet(u"image:none;\n"
"background-color: qlineargradient(spread:pad, x1:0.61, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 118), stop:1 rgba(0, 0, 0, 198));")
        self.horizontalLayout_14 = QHBoxLayout(self.Home_Page)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.Home_Page_base = QFrame(self.Home_Page)
        self.Home_Page_base.setObjectName(u"Home_Page_base")
        self.Home_Page_base.setStyleSheet(u"")
        self.Home_Page_base.setFrameShape(QFrame.StyledPanel)
        self.Home_Page_base.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.Home_Page_base)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_5 = QLabel(self.Home_Page_base)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(60, 60))
        self.label_5.setStyleSheet(u"border-image: url(:/newPrefix/Utility Icons/home.png);")

        self.horizontalLayout_19.addWidget(self.label_5)


        self.horizontalLayout_14.addWidget(self.Home_Page_base)

        self.MainContentstackedWidget.addWidget(self.Home_Page)
        self.Settings_Page = QWidget()
        self.Settings_Page.setObjectName(u"Settings_Page")
        self.Settings_Page.setStyleSheet(u"image:none;\n"
"background-color: qlineargradient(spread:pad, x1:0.61, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 118), stop:1 rgba(0, 0, 0, 198));")
        self.horizontalLayout_15 = QHBoxLayout(self.Settings_Page)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.Settings_Page_base = QFrame(self.Settings_Page)
        self.Settings_Page_base.setObjectName(u"Settings_Page_base")
        self.Settings_Page_base.setFrameShape(QFrame.StyledPanel)
        self.Settings_Page_base.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.Settings_Page_base)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_4 = QLabel(self.Settings_Page_base)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(60, 60))
        self.label_4.setStyleSheet(u"border-image: url(:/newPrefix/Utility Icons/settings.png);")

        self.horizontalLayout_20.addWidget(self.label_4)


        self.horizontalLayout_15.addWidget(self.Settings_Page_base)

        self.MainContentstackedWidget.addWidget(self.Settings_Page)
        self.Account_Page = QWidget()
        self.Account_Page.setObjectName(u"Account_Page")
        self.Account_Page.setStyleSheet(u"image:none;\n"
"background-color: qlineargradient(spread:pad, x1:0.61, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 118), stop:1 rgba(0, 0, 0, 198));")
        self.horizontalLayout_16 = QHBoxLayout(self.Account_Page)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.Account_Page_base = QFrame(self.Account_Page)
        self.Account_Page_base.setObjectName(u"Account_Page_base")
        self.Account_Page_base.setFrameShape(QFrame.StyledPanel)
        self.Account_Page_base.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.Account_Page_base)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_3 = QLabel(self.Account_Page_base)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(60, 60))
        self.label_3.setStyleSheet(u"border-image: url(:/newPrefix/Utility Icons/users.png);")

        self.horizontalLayout_21.addWidget(self.label_3)


        self.horizontalLayout_16.addWidget(self.Account_Page_base)

        self.MainContentstackedWidget.addWidget(self.Account_Page)

        self.verticalLayout_2.addWidget(self.MainContentstackedWidget)


        self.horizontalLayout_3.addWidget(self.InnerContentFrame)


        self.verticalLayout_3.addWidget(self.ContentFrame)

        self.BottomMarginFrame = QFrame(self.BaseFrame)
        self.BottomMarginFrame.setObjectName(u"BottomMarginFrame")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.BottomMarginFrame.sizePolicy().hasHeightForWidth())
        self.BottomMarginFrame.setSizePolicy(sizePolicy8)
        self.BottomMarginFrame.setMinimumSize(QSize(0, 18))
        self.BottomMarginFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(24, 25, 33);\n"
"}")
        self.BottomMarginFrame.setFrameShape(QFrame.StyledPanel)
        self.BottomMarginFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.BottomMarginFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.BottomDrag = QFrame(self.BottomMarginFrame)
        self.BottomDrag.setObjectName(u"BottomDrag")
        self.BottomDrag.setStyleSheet(u"background-color: rgb(85, 255, 255);\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.BottomDrag.setFrameShape(QFrame.StyledPanel)
        self.BottomDrag.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.BottomDrag)

        self.QSizeGrip_botto_right = QFrame(self.BottomMarginFrame)
        self.QSizeGrip_botto_right.setObjectName(u"QSizeGrip_botto_right")
        sizePolicy7.setHeightForWidth(self.QSizeGrip_botto_right.sizePolicy().hasHeightForWidth())
        self.QSizeGrip_botto_right.setSizePolicy(sizePolicy7)
        self.QSizeGrip_botto_right.setMinimumSize(QSize(22, 18))
        self.QSizeGrip_botto_right.setCursor(QCursor(Qt.ArrowCursor))
        self.QSizeGrip_botto_right.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"image: url(:/newPrefix/Utility Icons/arrow-down-right.svg);\n"
"background-color: rgb(24, 25, 33);")
        self.QSizeGrip_botto_right.setFrameShape(QFrame.StyledPanel)
        self.QSizeGrip_botto_right.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.QSizeGrip_botto_right)


        self.verticalLayout_3.addWidget(self.BottomMarginFrame)


        self.verticalLayout.addWidget(self.BaseFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.MainContentstackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.MiniButton.setText("")
        self.MaxiButton.setText("")
        self.CloseButton.setText("")
        self.LeftMenuExpandButton.setText("")
        self.HomeButton.setText("")
        self.HomeLabel.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.AccountButton.setText("")
        self.AccountLabel.setText(QCoreApplication.translate("MainWindow", u"Accounts", None))
        self.ContactButton.setText("")
        self.ContactLabel.setText(QCoreApplication.translate("MainWindow", u"Contact", None))
        self.BrowserButton.setText("")
        self.BrowserLabel.setText(QCoreApplication.translate("MainWindow", u"Browser", None))
        self.SettingButton.setText("")
        self.SettingsLabel.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_5.setText("")
        self.label_4.setText("")
        self.label_3.setText("")
    # retranslateUi

