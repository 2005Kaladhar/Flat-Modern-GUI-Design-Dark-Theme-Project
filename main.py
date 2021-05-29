
from PySide2 import QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import sys
from ui_newuiDesign import Ui_MainWindow as mainScreen

class MainApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = mainScreen()
        self.ui.setupUi(self)

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)
         
        # Button Label List
        self.buttonLabelrecord = { self.ui.HomeLabel.text() : self.ui.Home, 
        self.ui.AccountLabel.text() : self.ui.Accounts, 
        self.ui.ContactLabel.text() : self.ui.Contact,
        self.ui.SettingsLabel.text() : self.ui.Settings,
        self.ui.BrowserLabel.text() : self.ui.Browser }
    
        # Dictionary as a cache memory for the click style event
        self.oldstyle = {}
    
        # self.leftMenuDefaultWidth = self.ui.LeftMenuFrame.width()
        self.leftMenuDefaultWidth = 45

        self.windowDimension = QApplication.desktop().screenGeometry()

        # Utility Buttons
        self.ui.MiniButton.clicked.connect(lambda :self.showMinimized())
        self.ui.MaxiButton.clicked.connect(self.maxi)
        self.ui.CloseButton.clicked.connect(lambda : quit() )
        

        # Left Menu Frame Buttons
        self.ui.LeftMenuExpandButton.clicked.connect(self.leftMenuExpandAnimation)
        self.ui.HomeButton.clicked.connect(self.HomeButtonClicked)
        self.ui.AccountButton.clicked.connect(self.AccountButtonClicked)
        self.ui.BrowserButton.clicked.connect(self.BrowserButtonClicked)
        self.ui.SettingButton.clicked.connect(self.SettingButtonClicked)
        self.ui.ContactButton.clicked.connect(self.ContactButtonClicked)

        QSizeGrip(self.ui.QSizeGrip_top_left)
        QSizeGrip(self.ui.QSizeGrip_botto_right)

       
        def labelClickedEvent(e,child=None,button_func=None):
            if e.buttons() == Qt.LeftButton:
                parent = self.buttonLabelrecord[child.text()]
                self.ClickStyleChanger(parent_frame=parent)
                button_func()
                # print("Label is clicked:",child.text())
            
        self.ui.HomeLabel.mousePressEvent = lambda event : labelClickedEvent(event,self.ui.HomeLabel,self.HomeButtonClicked)
        self.ui.AccountLabel.mousePressEvent = lambda event : labelClickedEvent(event,self.ui.AccountLabel, self.AccountButtonClicked)
        self.ui.BrowserLabel.mousePressEvent = lambda event : labelClickedEvent(event,self.ui.BrowserLabel, self.BrowserButtonClicked)
        self.ui.SettingsLabel.mousePressEvent = lambda event : labelClickedEvent(event,self.ui.SettingsLabel, self.SettingButtonClicked)
        self.ui.ContactLabel.mousePressEvent = lambda event : labelClickedEvent(event,self.ui.ContactLabel, self.ContactButtonClicked)


        def moveWindow(e):
            screenGeo = QApplication.desktop().screenGeometry()
            fullscreen = (self.height(), self.width() )==(screenGeo.height(), screenGeo.width())

            if not fullscreen:
                if e.buttons() == Qt.LeftButton:    
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
            else:
                self.setGeometry(self.prevGeo.x() , e.globalPos().y(), self.prevGeo.width(),
                self.prevGeo.height())
                # self.setGeometry(self.prevGeo)

    
        self.ui.DragFrameTop.mouseMoveEvent = moveWindow
        self.ui.DragFrameTop.mouseDoubleClickEvent = self.maxi
        self.ui.BottomDrag.mouseMoveEvent = moveWindow

        # self.show()

        self.windowEntryAnimation()
        # while True:
        #     QApplication.processEvents()
        #     print("Geo: ",self.geometry())


    def mousePressEvent(self,event):
        self.clickPosition = event.globalPos()

    # Open Window in an Animated Style
    def windowEntryAnimation(self):

        # QRect(186, 107, 999, 593)
        
        self.ui.MainContentstackedWidget.setCurrentWidget(self.ui.Home_Page)
        self.animation = QPropertyAnimation(self,b'geometry')
        self.animation.setDuration(250)
        self.animation.setEasingCurve(QEasingCurve.Custom)
        self.animation.setStartValue(QRect(186, 107, 0, 0))
        self.animation.setEndValue(QRect(186, 107, 999, 593))
        self.animation.start()
        self.show()

    
    
    # Left Menu Frame Buttons Functions
    def ClickStyleChanger(self,parent_frame=None,child_lable=None,action_button=None):
       

        default_frame_style = '''
        QFrame::hover{

        background-color: rgba(4, 4, 4, 120);

        }
         '''

        selection_style = '''
         QFrame{
        background-color: rgba(4, 4, 4, 120);
            }

        QLabel{
        border-top:1px solid rgba(85, 255, 127,170);
        }
         
        QPushButton{
            border-bottom-color: rgba(247, 173, 24,180);
            border-right-color: rgba(247, 173, 24,180);
        }
          '''
        # If there is already a button clicked then first make it normal and then do it
        if len( list(self.oldstyle.keys()) ) == 0:
            self.oldstyle.update({'parent':parent_frame})
            parent_frame.setStyleSheet(selection_style)
        
        
        # When no button is clicked then do it simply
        else:
            self.oldstyle['parent' ].setStyleSheet(default_frame_style)
            self.oldstyle.clear()
            self.ClickStyleChanger(parent_frame)
        
        
    # Small Expand and Shrink Animation of LeftMenuFrame when buttons are clicked
    def left_menu_expandAndshrink(self,condition=True):
        duration =200
        
        if condition :
            self.animation = QPropertyAnimation(self.ui.LeftMenuFrame,b'minimumWidth')
            self.animation.setDuration(duration)
            self.animation.setEasingCurve(QEasingCurve.Linear)

            start_val = self.ui.LeftMenuFrame.width()
            end_val = 170

            self.animation.setStartValue(start_val)
            self.animation.setEndValue(end_val)
            self.animation.start()

            loop = QEventLoop()
            QTimer.singleShot(duration+100,loop.quit)
            loop.exec_()

            start_val, end_val = self.ui.LeftMenuFrame.width(), 46
            self.animation.setStartValue(start_val)
            self.animation.setEndValue(end_val)
            self.animation.setDuration(duration)
            self.animation.start()
        
    
    # Defining LeftMenuFrame buttons functions
    def HomeButtonClicked(self):
        parent = (self.buttonLabelrecord[self.ui.HomeLabel.text() ])
        self.ClickStyleChanger(parent,self.ui.HomeLabel)

        self.left_menu_expandAndshrink(self.ui.LeftMenuFrame.width()<=46)

        self.ui.MainContentstackedWidget.setCurrentWidget(self.ui.Home_Page)
        
        

    def ContactButtonClicked(self):
        parent = (self.buttonLabelrecord[self.ui.ContactLabel.text() ])
        self.ClickStyleChanger(parent,self.ui.ContactLabel)

        self.left_menu_expandAndshrink(self.ui.LeftMenuFrame.width()<=46)

        self.ui.MainContentstackedWidget.setCurrentWidget(self.ui.Contact_Page)

    def AccountButtonClicked(self):
        parent = (self.buttonLabelrecord[self.ui.AccountLabel.text() ])
        self.ClickStyleChanger(parent,self.ui.AccountLabel)
        self.left_menu_expandAndshrink(self.ui.LeftMenuFrame.width()<=46)

        self.ui.MainContentstackedWidget.setCurrentWidget(self.ui.Account_Page)

    def BrowserButtonClicked(self):
        parent = (self.buttonLabelrecord[self.ui.BrowserLabel.text() ])
        self.ClickStyleChanger(parent,self.ui.BrowserLabel)

        self.left_menu_expandAndshrink(self.ui.LeftMenuFrame.width()<=46)

        self.ui.MainContentstackedWidget.setCurrentWidget(self.ui.Browser_Page)


    def SettingButtonClicked(self):
        parent = (self.buttonLabelrecord[self.ui.SettingsLabel.text() ])
        self.ClickStyleChanger(parent,self.ui.SettingsLabel)
        self.left_menu_expandAndshrink()
    
        self.ui.MainContentstackedWidget.setCurrentWidget(self.ui.Settings_Page)
    
    
    
    # Defining Utility Button Functions
    def maxi(self,extra=None):
        screenGeo = QApplication.desktop().screenGeometry()
        fullscreen = (self.height(), self.width() )==(screenGeo.height(), screenGeo.width())
        # print(f"is it fullscreen ??? : {fullscreen}")

        if fullscreen :
            # self.setGeometry(self.prevGeo)
            self.resizeWindowAnimation(expand=False)
        else:
            self.prevGeo = self.geometry()
            # self.setGeometry(screenGeo)
            self.resizeWindowAnimation(expand=True)

    
    
    # Window resize animation for smooth view
    def resizeWindowAnimation(self,expand=True):
        start_Val = self.geometry()
        end_val = self.windowDimension
        duration = 80
        easingCurve = QEasingCurve.InBack

        self.animation = QPropertyAnimation(self,b'geometry')
        self.animation.setDuration(duration)
        

        if not expand:
            start_Val = self.geometry()
            end_val = self.prevGeo
            easingCurve = QEasingCurve.InQuad

        self.animation.setEasingCurve(easingCurve)
        self.animation.setStartValue(start_Val)
        self.animation.setEndValue(end_val)
        self.animation.start()
    
    
    # Expand and Shrink the LeftMenu frame with Aniamtion
    def leftMenuExpandAnimation(self):
        tarWidht = 170
        condition = self.ui.LeftMenuFrame.width() < tarWidht
        
        self.animation = QPropertyAnimation(self.ui.LeftMenuFrame,b'minimumWidth')
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutBack)
        
        if condition:
            start_val = self.ui.LeftMenuFrame.width()
            end_val = tarWidht
        else:
            start_val = self.ui.LeftMenuFrame.width()
            end_val = self.leftMenuDefaultWidth

        self.animation.setStartValue(start_val)
        self.animation.setEndValue(end_val)
        self.animation.start()
        


if __name__ == '__main__':
    app = QApplication()
    window = MainApplication()
    sys.exit(app.exec_())
    