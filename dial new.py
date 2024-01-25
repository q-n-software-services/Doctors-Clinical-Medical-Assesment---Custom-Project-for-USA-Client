import math
from PyQt5.QtWidgets import QApplication, QDialog,QComboBox, QLineEdit, QFontComboBox, QVBoxLayout, QHBoxLayout,QDial, QTextEdit, QLCDNumber, QMessageBox, QListWidget, QListWidgetItem, QListView, QPushButton, QCalendarWidget, QLabel, QWidget, QTableWidget, QTableWidgetItem
import sys, calendar, datetime
from PyQt5.QtGui import QFont, QIcon, QPainter, QPen, QColor
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt5.QtCore import QSize, QTime, QTimer, QLocale, Qt, QRect
import time
from random import randint
import sqlite3, sys, os

arcWidth = 20
gaugeSpacer = 12
rowDim = 5
minP = 5
maxP = 6
logoPos = [5]
logoDim = [7]
windowPos = [255, 255]
rectPrimPPos = [logoPos[0]+logoDim[0]+(arcWidth/2)+2*gaugeSpacer, windowPos[1]] # primary power gauge position [x,y]
rectPrimPDim = [(rowDim*5/27),(rowDim*5/27)] # primary power gauge dimension [x,y]
rectPrimP = QRect(int(rectPrimPPos[0]),int(rectPrimPPos[1]),int(rectPrimPDim[0]),int(rectPrimPDim[1])) # rectangle in which to enscribe primary power gauge

minValPrimP = minP
maxValPrimP = maxP
gaugeMaxValPrimP = 180*16 # angle of gauge at max of scale: 180 1/16's degrees
startAnglePrimP = 0 # primary power gauge: beginning degree of angle
spanAnglePrimP = int(((1200-minValPrimP)*gaugeMaxValPrimP/(maxValPrimP-minValPrimP))) # primary power gauge: end degree of angle

qp = QPainter()
qp.setPen(QPen(QColor(40,40,40), arcWidth, Qt.SolidLine)) # set pen for outer arc

qp.drawArc(rectPrimP, startAnglePrimP, 180*16)  # draw outer arc
qp.setPen(QPen(QColor(226, 47, 223), arcWidth-5, Qt.SolidLine)) # set pen for inner arc
qp.drawArc(rectPrimP, startAnglePrimP, spanAnglePrimP) # draw inner arc
