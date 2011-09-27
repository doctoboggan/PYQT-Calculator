#!/usr/bin/python -d
 
import sys
from PyQt4 import QtCore, QtGui
from interface import Ui_MainWindow
 
class MyCalc(QtGui.QMainWindow):
#Instance Vars
  lcdString = ''      #Stores string for lcd display
  operation = ''      #Current operation
  currentNum = 0
  previousNum = 0
  ans = 0


  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.initUI()
    
  def initUI(self):
    #Connect Num Buttons
    self.connect(self.ui.b1, QtCore.SIGNAL('clicked()'), self.buttonClicked)
    self.connect(self.ui.b2, QtCore.SIGNAL('clicked()'), self.buttonClicked)
    self.connect(self.ui.b3, QtCore.SIGNAL('clicked()'), self.buttonClicked)
    self.connect(self.ui.b4, QtCore.SIGNAL('clicked()'), self.buttonClicked)
    self.connect(self.ui.b5, QtCore.SIGNAL('clicked()'), self.buttonClicked)
    self.connect(self.ui.b6, QtCore.SIGNAL('clicked()'), self.buttonClicked)
    self.connect(self.ui.b7, QtCore.SIGNAL('clicked()'), self.buttonClicked)
    self.connect(self.ui.b8, QtCore.SIGNAL('clicked()'), self.buttonClicked)
    self.connect(self.ui.b9, QtCore.SIGNAL('clicked()'), self.buttonClicked)
    self.connect(self.ui.b0, QtCore.SIGNAL('clicked()'), self.buttonClicked)
    self.connect(self.ui.period, QtCore.SIGNAL('clicked()'), self.buttonClicked)
    
    #Connect Clr
    self.connect(self.ui.clr, QtCore.SIGNAL('clicked()'), self.clrClicked)
    
    #Connect Op buttons
    self.connect(self.ui.plus, QtCore.SIGNAL('clicked()'), self.opClicked)
    self.connect(self.ui.minus, QtCore.SIGNAL('clicked()'), self.opClicked)
    self.connect(self.ui.multiply, QtCore.SIGNAL('clicked()'), self.opClicked)
    self.connect(self.ui.divide, QtCore.SIGNAL('clicked()'), self.opClicked)
    
    #Connect Enter
    self.connect(self.ui.enter, QtCore.SIGNAL('clicked()'), self.enterClicked)
    
  def buttonClicked(self):
    self.lcdString = self.lcdString + self.sender().text()
    self.ui.lcd.display(self.lcdString)
    self.currentNum = float(self.lcdString)
    
  def clrClicked(self):
    #update vars
    self.lcdString = ''
    self.currentNum = 0
    self.previousNum = 0
    #update display
    self.ui.lcd.display(0)
    
  def opClicked(self):
    self.previousNum = self.currentNum
    self.currentNum = 0
    self.lcdString = ''
    self.operation = self.sender().objectName()
    
  def enterClicked(self):
    if self.operation == 'plus':
      self.ans = self.previousNum + self.currentNum
      
    if self.operation == 'minus':
      self.ans = self.previousNum - self.currentNum
      
    if self.operation == 'multiply':
      self.ans = self.previousNum * self.currentNum
      
    if self.operation == 'divide':
      self.ans = self.previousNum / self.currentNum
       
    self.currentNum = self.ans
    self.ui.lcd.display(self.ans)
    self.lcdString = ''
    
 
if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  myapp = MyCalc()
  myapp.show()
  sys.exit(app.exec_())
