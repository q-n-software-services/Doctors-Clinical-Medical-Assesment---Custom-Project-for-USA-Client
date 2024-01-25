import datetime
import random
import sqlite3
import time
import os
# os.system("python test4.py")

from PyQt5.QtWidgets import QApplication, QDialog, QListWidget, QListWidgetItem, QHBoxLayout, QVBoxLayout, QLabel, QGridLayout,  QSpinBox, QLineEdit, QWidget, QDial, QGroupBox, QPushButton, QTextEdit, QComboBox, QRadioButton, QFileDialog
import sys
from PyQt5.QtGui import QIcon, QFont, QPixmap, QPainter, QMouseEvent
from PyQt5.QtCore import QSize, Qt, QTimer, QRect, QEvent, pyqtSignal, QLineF

image_link12 = 'BROWSE'
prescription = ''
keys = ['T2M1', 'T2M2', 'T2M3', 'T2M4', 'T2M5', 'T2M6', 'T2M7', 'T2M8', 'T2M9', 'T2M10', 'T2F1', 'T2F2',
                'T2F3',
                'T2F4', 'T2F5', 'T2F6', 'T2F7', 'T2F8', 'T2F9', 'T2F10', 'T3M1', 'T3M2', 'T3M3', 'T3M4', 'T3M5',
                'T3M6',
                'T3M7', 'T3M8', 'T3M9', 'T3M10', 'T3F1', 'T3F2', 'T3F3', 'T3F4', 'T3F5', 'T3F6', 'T3F7', 'T3F8',
                'T3F9',
                'T3F10', 'T4M1', 'T4M2', 'T4M3', 'T4M4', 'T4M5', 'T4M6', 'T4M7', 'T4M8', 'T4M9', 'T4M10', 'T4F1',
                'T4F2', 'T4F3', 'T4F4', 'T4F5', 'T4F6', 'T4F7', 'T4F8', 'T4F9', 'T4F10', 'T5M1', 'T5M2', 'T5M3',
                'T5M4',
                'T5M5', 'T5M6', 'T5M7', 'T5M8', 'T5M9', 'T5M10', 'T5F1', 'T5F2', 'T5F3', 'T5F4', 'T5F5', 'T5F6',
                'T5F7',
                'T5F8', 'T5F9', 'T5F10']

key = keys[0]

questions = []
question_index = 0

user_category_name = ''
user_category_value = 0

# pics = ['D:/My Data/Dilruba pics\\FB_IMG_1595984115715.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1595986014037.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1595986017357.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1595986270296.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1595986296832.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1595986933088.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596015968390.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596015971378.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596015974294.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596015976978.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596015979785.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596015997564.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596016002084.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596160055868.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596160058763.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596160061529.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596160070640.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596160190391.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596255607608.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596256822501.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596331159323.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596332324028.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596723792565.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596724125171.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596821711985.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597125347304.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597125352431.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597125621472.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597125626540.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597125628574.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142774318.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142776668.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142779478.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142783582.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142787289.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142790181.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142794136.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142810387.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142812848.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142819892.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597143902650.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597143905590.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597255016787.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597255019701.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597255023814.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597255026874.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597313700554.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597340822859.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597340825759.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597340829118.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597378568005.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597394519046.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597425650713.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597541417585.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597541430322.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597541471567.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597686782476.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597686784860.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597686853650.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597687099799.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597687102225.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597687104639.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597687383363.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597687400129.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597727988593.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597728003154.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597728021598.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597728109110.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597768273722.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597768649045.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597858897965.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597859601628.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597918668927.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597918671922.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597918677578.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597918677600.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597918683290.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597918687776.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597918691826.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597918702629.jpg']
pics = {'T2M1': 'D:/My Data/Dilruba pics\\FB_IMG_1595984115715.jpg', 'T2M2': 'D:/My Data/Dilruba pics\\FB_IMG_1595986014037.jpg', 'T2M3': 'D:/My Data/Dilruba pics\\FB_IMG_1595986017357.jpg', 'T2M4': 'D:/My Data/Dilruba pics\\FB_IMG_1595986270296.jpg', 'T2M5': 'D:/My Data/Dilruba pics\\FB_IMG_1595986296832.jpg', 'T2M6': 'D:/My Data/Dilruba pics\\FB_IMG_1595986933088.jpg', 'T2M7': 'D:/My Data/Dilruba pics\\FB_IMG_1596015968390.jpg', 'T2M8': 'D:/My Data/Dilruba pics\\FB_IMG_1596015971378.jpg', 'T2M9': 'D:/My Data/Dilruba pics\\FB_IMG_1596015974294.jpg', 'T2M10': 'D:/My Data/Dilruba pics\\FB_IMG_1596015976978.jpg', 'T2F1': 'D:/My Data/Dilruba pics\\FB_IMG_1596015979785.jpg', 'T2F2': 'D:/My Data/Dilruba pics\\FB_IMG_1596015997564.jpg', 'T2F3': 'D:/My Data/Dilruba pics\\FB_IMG_1596016002084.jpg', 'T2F4': 'D:/My Data/Dilruba pics\\FB_IMG_1596160055868.jpg', 'T2F5': 'D:/My Data/Dilruba pics\\FB_IMG_1596160058763.jpg', 'T2F6': 'D:/My Data/Dilruba pics\\FB_IMG_1596160061529.jpg', 'T2F7': 'D:/My Data/Dilruba pics\\FB_IMG_1596160070640.jpg', 'T2F8': 'D:/My Data/Dilruba pics\\FB_IMG_1596160190391.jpg', 'T2F9': 'D:/My Data/Dilruba pics\\FB_IMG_1596255607608.jpg', 'T2F10': 'D:/My Data/Dilruba pics\\FB_IMG_1596256822501.jpg', 'T3M1': 'D:/My Data/Dilruba pics\\FB_IMG_1596331159323.jpg', 'T3M2': 'D:/My Data/Dilruba pics\\FB_IMG_1596332324028.jpg', 'T3M3': 'D:/My Data/Dilruba pics\\FB_IMG_1596723792565.jpg', 'T3M4': 'D:/My Data/Dilruba pics\\FB_IMG_1596724125171.jpg', 'T3M5': 'D:/My Data/Dilruba pics\\FB_IMG_1596821711985.jpg', 'T3M6': 'D:/My Data/Dilruba pics\\FB_IMG_1597125347304.jpg', 'T3M7': 'D:/My Data/Dilruba pics\\FB_IMG_1597125352431.jpg', 'T3M8': 'D:/My Data/Dilruba pics\\FB_IMG_1597125621472.jpg', 'T3M9': 'D:/My Data/Dilruba pics\\FB_IMG_1597125626540.jpg', 'T3M10': 'D:/My Data/Dilruba pics\\FB_IMG_1597125628574.jpg', 'T3F1': 'D:/My Data/Dilruba pics\\FB_IMG_1597142774318.jpg', 'T3F2': 'D:/My Data/Dilruba pics\\FB_IMG_1597142776668.jpg', 'T3F3': 'D:/My Data/Dilruba pics\\FB_IMG_1597142779478.jpg', 'T3F4': 'D:/My Data/Dilruba pics\\FB_IMG_1597142783582.jpg', 'T3F5': 'D:/My Data/Dilruba pics\\FB_IMG_1597142787289.jpg', 'T3F6': 'D:/My Data/Dilruba pics\\FB_IMG_1597142790181.jpg', 'T3F7': 'D:/My Data/Dilruba pics\\FB_IMG_1597142794136.jpg', 'T3F8': 'D:/My Data/Dilruba pics\\FB_IMG_1597142810387.jpg', 'T3F9': 'D:/My Data/Dilruba pics\\FB_IMG_1597142812848.jpg', 'T3F10': 'D:/My Data/Dilruba pics\\FB_IMG_1597142819892.jpg', 'T4M1': 'D:/My Data/Dilruba pics\\FB_IMG_1597143902650.jpg', 'T4M2': 'D:/My Data/Dilruba pics\\FB_IMG_1597143905590.jpg', 'T4M3': 'D:/My Data/Dilruba pics\\FB_IMG_1597255016787.jpg', 'T4M4': 'D:/My Data/Dilruba pics\\FB_IMG_1597255019701.jpg', 'T4M5': 'D:/My Data/Dilruba pics\\FB_IMG_1597255023814.jpg', 'T4M6': 'D:/My Data/Dilruba pics\\FB_IMG_1597255026874.jpg', 'T4M7': 'D:/My Data/Dilruba pics\\FB_IMG_1597313700554.jpg', 'T4M8': 'D:/My Data/Dilruba pics\\FB_IMG_1597340822859.jpg', 'T4M9': 'D:/My Data/Dilruba pics\\FB_IMG_1597340825759.jpg', 'T4M10': 'D:/My Data/Dilruba pics\\FB_IMG_1597340829118.jpg', 'T4F1': 'D:/My Data/Dilruba pics\\FB_IMG_1597378568005.jpg', 'T4F2': 'D:/My Data/Dilruba pics\\FB_IMG_1597394519046.jpg', 'T4F3': 'D:/My Data/Dilruba pics\\FB_IMG_1597425650713.jpg', 'T4F4': 'D:/My Data/Dilruba pics\\FB_IMG_1597541417585.jpg', 'T4F5': 'D:/My Data/Dilruba pics\\FB_IMG_1597541430322.jpg', 'T4F6': 'D:/My Data/Dilruba pics\\FB_IMG_1597541471567.jpg', 'T4F7': 'D:/My Data/Dilruba pics\\FB_IMG_1597686782476.jpg', 'T4F8': 'D:/My Data/Dilruba pics\\FB_IMG_1597686784860.jpg', 'T4F9': 'D:/My Data/Dilruba pics\\FB_IMG_1597686853650.jpg', 'T4F10': 'D:/My Data/Dilruba pics\\FB_IMG_1597687099799.jpg', 'T5M1': 'D:/My Data/Dilruba pics\\FB_IMG_1597687102225.jpg', 'T5M2': 'D:/My Data/Dilruba pics\\FB_IMG_1597687104639.jpg', 'T5M3': 'D:/My Data/Dilruba pics\\FB_IMG_1597687383363.jpg', 'T5M4': 'D:/My Data/Dilruba pics\\FB_IMG_1597687400129.jpg', 'T5M5': 'D:/My Data/Dilruba pics\\FB_IMG_1597727988593.jpg', 'T5M6': 'D:/My Data/Dilruba pics\\FB_IMG_1597728003154.jpg', 'T5M7': 'D:/My Data/Dilruba pics\\FB_IMG_1597728021598.jpg', 'T5M8': 'D:/My Data/Dilruba pics\\FB_IMG_1597728109110.jpg', 'T5M9': 'D:/My Data/Dilruba pics\\FB_IMG_1597768273722.jpg', 'T5M10': 'D:/My Data/Dilruba pics\\FB_IMG_1597768649045.jpg', 'T5F1': 'D:/My Data/Dilruba pics\\FB_IMG_1597858897965.jpg', 'T5F2': 'D:/My Data/Dilruba pics\\FB_IMG_1597859601628.jpg', 'T5F3': 'D:/My Data/Dilruba pics\\FB_IMG_1597918668927.jpg', 'T5F4': 'D:/My Data/Dilruba pics\\FB_IMG_1597918671922.jpg', 'T5F5': 'D:/My Data/Dilruba pics\\FB_IMG_1597918677578.jpg', 'T5F6': 'D:/My Data/Dilruba pics\\FB_IMG_1597918677600.jpg', 'T5F7': 'D:/My Data/Dilruba pics\\FB_IMG_1597918683290.jpg', 'T5F8': 'D:/My Data/Dilruba pics\\FB_IMG_1597918687776.jpg', 'T5F9': 'D:/My Data/Dilruba pics\\FB_IMG_1597918691826.jpg', 'T5F10': 'D:/My Data/Dilruba pics\\FB_IMG_1597918702629.jpg'}
i12 = 0
# Database setup and related stuff of SQLite3
conn = sqlite3.connect("userData.sqlite")
cur = conn.cursor()

# cur.execute('''DROP TABLE IF EXISTS userData''')
#
# cur.execute('''CREATE TABLE userData (id text, dateStamp TEXT, name TEXT, age REAL, T2M1 INTEGER, T2M2 INTEGER, T2M3 INTEGER, T2M4 INTEGER, T2M5 INTEGER, T2M6 INTEGER, T2M7 INTEGER, T2M8 INTEGER, T2M9 INTEGER, T2M10 INTEGER, T2F1 INTEGER, T2F2 INTEGER, T2F3 INTEGER, T2F4 INTEGER, T2F5 INTEGER, T2F6 INTEGER, T2F7 INTEGER, T2F8 INTEGER, T2F9 INTEGER, T2F10 INTEGER, T3M1 INTEGER, T3M2 INTEGER, T3M3 INTEGER, T3M4 INTEGER, T3M5 INTEGER, T3M6 INTEGER, T3M7 INTEGER, T3M8 INTEGER, T3M9 INTEGER, T3M10 INTEGER, T3F1 INTEGER, T3F2 INTEGER, T3F3 INTEGER, T3F4 INTEGER, T3F5 INTEGER, T3F6 INTEGER, T3F7 INTEGER, T3F8 INTEGER, T3F9 INTEGER, T3F10 INTEGER, T4M1 INTEGER, T4M2 INTEGER, T4M3 INTEGER, T4M4 INTEGER, T4M5 INTEGER, T4M6 INTEGER, T4M7 INTEGER, T4M8 INTEGER, T4M9 INTEGER, T4M10 INTEGER, T4F1 INTEGER, T4F2 INTEGER, T4F3 INTEGER, T4F4 INTEGER, T4F5 INTEGER, T4F6 INTEGER, T4F7 INTEGER, T4F8 INTEGER, T4F9 INTEGER, T4F10 INTEGER, T5M1 INTEGER, T5M2 INTEGER, T5M3 INTEGER, T5M4 INTEGER, T5M5 INTEGER, T5M6 INTEGER, T5M7 INTEGER, T5M8 INTEGER, T5M9 INTEGER, T5M10 INTEGER, T5F1 INTEGER, T5F2 INTEGER, T5F3 INTEGER, T5F4 INTEGER, T5F5 INTEGER, T5F6 INTEGER, T5F7 INTEGER, T5F8 INTEGER, T5F9 INTEGER, T5F10 INTEGER, T2Mscore TEXT, T2Fscore TEXT, T3Mscore TEXT, T3Fscore TEXT, T4Mscore TEXT, T4Fscore TEXT, T5Mscore TEXT, T5Fscore TEXT, userCategory text, answers text, prescription text)''')

# conn.commit()


# Database setup and related stuff of SQLite3
conn2 = sqlite3.connect("imageData.sqlite")
cur2 = conn2.cursor()

# cur2.execute('''DROP TABLE IF EXISTS imageData''')
# cur2.execute('''CREATE TABLE imageData (id text, dateStamp TEXT, T2M1 TEXT, T2M2 TEXT, T2M3 TEXT, T2M4 TEXT, T2M5 TEXT, T2M6 TEXT, T2M7 TEXT, T2M8 TEXT, T2M9 TEXT, T2M10 TEXT, T2F1 TEXT, T2F2 TEXT, T2F3 TEXT, T2F4 TEXT, T2F5 TEXT, T2F6 TEXT, T2F7 TEXT, T2F8 TEXT, T2F9 TEXT, T2F10 TEXT, T3M1 TEXT, T3M2 TEXT, T3M3 TEXT, T3M4 TEXT, T3M5 TEXT, T3M6 TEXT, T3M7 TEXT, T3M8 TEXT, T3M9 TEXT, T3M10 TEXT, T3F1 TEXT, T3F2 TEXT, T3F3 TEXT, T3F4 TEXT, T3F5 TEXT, T3F6 TEXT, T3F7 TEXT, T3F8 TEXT, T3F9 TEXT, T3F10 TEXT, T4M1 TEXT, T4M2 TEXT, T4M3 TEXT, T4M4 TEXT, T4M5 TEXT, T4M6 TEXT, T4M7 TEXT, T4M8 TEXT, T4M9 TEXT, T4M10 TEXT, T4F1 TEXT, T4F2 TEXT, T4F3 TEXT, T4F4 TEXT, T4F5 TEXT, T4F6 TEXTR, T4F7 TEXT, T4F8 TEXT, T4F9 TEXT, T4F10 TEXT, T5M1 TEXT, T5M2 TEXT, T5M3 TEXT, T5M4 TEXT, T5M5 TEXT, T5M6 TEXT, T5M7 TEXT, T5M8 TEXT, T5M9 TEXT, T5M10 TEXT, T5F1 TEXT, T5F2 TEXT, T5F3 TEXT, T5F4 TEXT, T5F5 TEXT, T5F6 TEXT, T5F7 TEXT, T5F8 TEXT, T5F9 TEXT, T5F10 TEXT)''')
# cur2.execute('INSERT INTO imageData (id, dateStamp, T2M1, T2M2, T2M3, T2M4, T2M5, T2M6, T2M7, T2M8, T2M9, T2M10, T2F1, T2F2, T2F3, T2F4, T2F5, T2F6, T2F7, T2F8, T2F9, T2F10, T3M1, T3M2, T3M3, T3M4, T3M5, T3M6, T3M7, T3M8, T3M9, T3M10, T3F1, T3F2, T3F3, T3F4, T3F5, T3F6, T3F7, T3F8, T3F9, T3F10, T4M1, T4M2, T4M3, T4M4, T4M5, T4M6, T4M7, T4M8, T4M9, T4M10, T4F1, T4F2, T4F3, T4F4, T4F5, T4F6, T4F7, T4F8, T4F9, T4F10, T5M1, T5M2, T5M3, T5M4, T5M5, T5M6, T5M7, T5M8, T5M9, T5M10, T5F1, T5F2, T5F3, T5F4, T5F5, T5F6, T5F7, T5F8, T5F9, T5F10) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', ('1', str(now), '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80'))
# now = datetime.datetime.now()
# cur2.execute('INSERT INTO imageData (id, dateStamp, T2M1, T2M2, T2M3, T2M4, T2M5, T2M6, T2M7, T2M8, T2M9, T2M10, T2F1, T2F2, T2F3, T2F4, T2F5, T2F6, T2F7, T2F8, T2F9, T2F10, T3M1, T3M2, T3M3, T3M4, T3M5, T3M6, T3M7, T3M8, T3M9, T3M10, T3F1, T3F2, T3F3, T3F4, T3F5, T3F6, T3F7, T3F8, T3F9, T3F10, T4M1, T4M2, T4M3, T4M4, T4M5, T4M6, T4M7, T4M8, T4M9, T4M10, T4F1, T4F2, T4F3, T4F4, T4F5, T4F6, T4F7, T4F8, T4F9, T4F10, T5M1, T5M2, T5M3, T5M4, T5M5, T5M6, T5M7, T5M8, T5M9, T5M10, T5F1, T5F2, T5F3, T5F4, T5F5, T5F6, T5F7, T5F8, T5F9, T5F10) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', ('2', str(now), 'D:/My Data/Dilruba pics\\FB_IMG_1595984115715.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1595986014037.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1595986017357.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1595986270296.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1595986296832.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1595986933088.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596015968390.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596015971378.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596015974294.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596015976978.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596015979785.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596015997564.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596016002084.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596160055868.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596160058763.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596160061529.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596160070640.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596160190391.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596255607608.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596256822501.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596331159323.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596332324028.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596723792565.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596724125171.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596821711985.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597125347304.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597125352431.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597125621472.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597125626540.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597125628574.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142774318.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142776668.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142779478.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142783582.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142787289.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142790181.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142794136.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142810387.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142812848.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142819892.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597143902650.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597143905590.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597255016787.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597255019701.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597255023814.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597255026874.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597313700554.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597340822859.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597340825759.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597340829118.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597378568005.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597394519046.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597425650713.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597541417585.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597541430322.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597541471567.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597686782476.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597686784860.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597686853650.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597687099799.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597687102225.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597687104639.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597687383363.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597687400129.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597727988593.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597728003154.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597728021598.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597728109110.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597768273722.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597768649045.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597858897965.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597859601628.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597918668927.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597918671922.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597918677578.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597918677600.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597918683290.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597918687776.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597918691826.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597918702629.jpg'))
# conn2.commit()
statement = '''SELECT * FROM imageData'''
cur2.execute(statement)
output = cur2.fetchall()

conn3 = sqlite3.connect("questions.sqlite")
cur3 = conn3.cursor()

# cur3.execute('''DROP TABLE IF EXISTS questions''')
# cur3.execute('''CREATE TABLE questions (dateStamp TEXT, question text, options TEXT)''')
# cur3.execute('INSERT INTO imageData (id, dateStamp, T2M1, T2M2, T2M3, T2M4, T2M5, T2M6, T2M7, T2M8, T2M9, T2M10, T2F1, T2F2, T2F3, T2F4, T2F5, T2F6, T2F7, T2F8, T2F9, T2F10, T3M1, T3M2, T3M3, T3M4, T3M5, T3M6, T3M7, T3M8, T3M9, T3M10, T3F1, T3F2, T3F3, T3F4, T3F5, T3F6, T3F7, T3F8, T3F9, T3F10, T4M1, T4M2, T4M3, T4M4, T4M5, T4M6, T4M7, T4M8, T4M9, T4M10, T4F1, T4F2, T4F3, T4F4, T4F5, T4F6, T4F7, T4F8, T4F9, T4F10, T5M1, T5M2, T5M3, T5M4, T5M5, T5M6, T5M7, T5M8, T5M9, T5M10, T5F1, T5F2, T5F3, T5F4, T5F5, T5F6, T5F7, T5F8, T5F9, T5F10) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', ('1', str(now), '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80'))
# now = datetime.datetime.now()
# cur3.execute('INSERT INTO imageData (id, dateStamp, T2M1, T2M2, T2M3, T2M4, T2M5, T2M6, T2M7, T2M8, T2M9, T2M10, T2F1, T2F2, T2F3, T2F4, T2F5, T2F6, T2F7, T2F8, T2F9, T2F10, T3M1, T3M2, T3M3, T3M4, T3M5, T3M6, T3M7, T3M8, T3M9, T3M10, T3F1, T3F2, T3F3, T3F4, T3F5, T3F6, T3F7, T3F8, T3F9, T3F10, T4M1, T4M2, T4M3, T4M4, T4M5, T4M6, T4M7, T4M8, T4M9, T4M10, T4F1, T4F2, T4F3, T4F4, T4F5, T4F6, T4F7, T4F8, T4F9, T4F10, T5M1, T5M2, T5M3, T5M4, T5M5, T5M6, T5M7, T5M8, T5M9, T5M10, T5F1, T5F2, T5F3, T5F4, T5F5, T5F6, T5F7, T5F8, T5F9, T5F10) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', ('2', str(now), 'D:/My Data/Dilruba pics\\FB_IMG_1595984115715.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1595986014037.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1595986017357.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1595986270296.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1595986296832.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1595986933088.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596015968390.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596015971378.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596015974294.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596015976978.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596015979785.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596015997564.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596016002084.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596160055868.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596160058763.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596160061529.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596160070640.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596160190391.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596255607608.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596256822501.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596331159323.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596332324028.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596723792565.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596724125171.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1596821711985.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597125347304.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597125352431.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597125621472.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597125626540.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597125628574.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142774318.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142776668.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142779478.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142783582.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142787289.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142790181.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142794136.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142810387.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142812848.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597142819892.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597143902650.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597143905590.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597255016787.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597255019701.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597255023814.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597255026874.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597313700554.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597340822859.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597340825759.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597340829118.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597378568005.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597394519046.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597425650713.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597541417585.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597541430322.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597541471567.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597686782476.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597686784860.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597686853650.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597687099799.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597687102225.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597687104639.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597687383363.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597687400129.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597727988593.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597728003154.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597728021598.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597728109110.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597768273722.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597768649045.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597858897965.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597859601628.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597918668927.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597918671922.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597918677578.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597918677600.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597918683290.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597918687776.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597918691826.jpg', 'D:/My Data/Dilruba pics\\FB_IMG_1597918702629.jpg'))
# conn3.commit()
answers_chosen = {}
statement = '''SELECT * FROM questions'''
cur3.execute(statement)
output2 = cur3.fetchall()
for data in output2:
    questions.append({'text': data[1], 'options': [item.lstrip().rstrip() for item in data[2].split('\n')]})
    answers_chosen[data[1]] =  'Nill'



# now = datetime.datetime.now()
# cur3.execute('INSERT INTO questions (dateStamp, question, options) VALUES (?, ?, ?)', (str(now), "What is your favourite food", "Spinach\n Chicken Qorma\n Achari Chana Pulao"))
# cur3.execute('INSERT INTO questions (dateStamp, question, options) VALUES (?, ?, ?)', (str(now), "What is your Sports hobby", "Pithu Garam\n Gulli Danda\n Kabaddi\n Patang Bazi\n Baraf Pani"))
# conn3.commit()



c = 0
for key12 in pics:
    pics[key12] = output[-1][c+2]
    c += 1

ids = []

abc = "D:/My Data/Dilruba pics/FB_IMG_1597425650713.jpg"

class ValueDial(QWidget):
    _dialProperties = ('minimum', 'maximum', 'value', 'singleStep', 'pageStep',
        'notchesVisible', 'tracking', 'wrapping',
        'invertedAppearance', 'invertedControls', 'orientation')
    _inPadding = 3
    _outPadding = 2
    valueChanged = pyqtSignal(int)

    def __init__(self, *args, **kwargs):
        # remove properties used as keyword arguments for the dial
        dialArgs = {k:v for k, v in kwargs.items() if k in self._dialProperties}
        for k in dialArgs.keys():
            kwargs.pop(k)
        super().__init__(*args, **kwargs)
        layout = QVBoxLayout(self)
        self.dial = QDial(self, **dialArgs)
        layout.addWidget(self.dial)
        self.dial.valueChanged.connect(self.valueChanged)
        # make the dial the focus proxy (so that it captures focus *and* key events)
        self.setFocusProxy(self.dial)

        # simple "monkey patching" to access dial functions
        self.value = self.dial.value
        self.setValue = self.dial.setValue
        self.minimum = self.dial.minimum
        self.maximum = self.dial.maximum
        self.wrapping = self.dial.wrapping
        self.notchesVisible = self.dial.notchesVisible
        self.setNotchesVisible = self.dial.setNotchesVisible
        self.setNotchTarget = self.dial.setNotchTarget
        self.notchSize = self.dial.notchSize
        self.invertedAppearance = self.dial.invertedAppearance
        self.setInvertedAppearance = self.dial.setInvertedAppearance

        self.updateSize()

    def inPadding(self):
        return self._inPadding

    def setInPadding(self, padding):
        self._inPadding = max(0, padding)
        self.updateSize()

    def outPadding(self):
        return self._outPadding

    def setOutPadding(self, padding):
        self._outPadding = max(0, padding)
        self.updateSize()

    # the following functions are required to correctly update the layout
    def setMinimum(self, minimum):
        self.dial.setMinimum(minimum)
        self.updateSize()

    def setMaximum(self, maximum):
        self.dial.setMaximum(maximum)
        self.updateSize()

    def setWrapping(self, wrapping):
        self.dial.setWrapping(wrapping)
        self.updateSize()

    def updateSize(self):
        # a function that sets the margins to ensure that the value strings always
        # have enough space
        fm = self.fontMetrics()
        minWidth = max(fm.width(str(v)) for v in range(self.minimum(), self.maximum() + 1))
        self.offset = max(minWidth, fm.height()) / 2
        margin = self.offset + self._inPadding + self._outPadding
        self.layout().setContentsMargins(int(margin), int(margin), int(margin), int(margin))

    def translateMouseEvent(self, event):
        # a helper function to translate mouse events to the dial
        return QMouseEvent(event.type(),
            self.dial.mapFrom(self, event.pos()),
            event.button(), event.buttons(), event.modifiers())

    def changeEvent(self, event):
        if event.type() == QEvent.FontChange:
            self.updateSize()

    def mousePressEvent(self, event):
        self.dial.mousePressEvent(self.translateMouseEvent(event))

    def mouseMoveEvent(self, event):
        self.dial.mouseMoveEvent(self.translateMouseEvent(event))

    def mouseReleaseEvent(self, event):
        self.dial.mouseReleaseEvent(self.translateMouseEvent(event))

    def paintEvent(self, event):
        radius = min(self.width(), self.height()) / 2
        radius -= (self.offset / 2 + self._outPadding)
        invert = -1 if self.invertedAppearance() else 1
        if self.wrapping():
            angleRange = 360
            startAngle = 270
            rangeOffset = 0
        else:
            angleRange = 300
            startAngle = 240 if invert > 0 else 300
            rangeOffset = 1
        fm = self.fontMetrics()

        # a reference line used for the target of the text rectangle
        reference = QLineF.fromPolar(radius, 0).translated(self.rect().center())
        fullRange = self.maximum() - self.minimum()
        textRect = QRect()

        qp = QPainter(self)
        qp.setRenderHints(qp.Antialiasing)
        for p in range(0, fullRange + rangeOffset, self.notchSize()):
            value = self.minimum() + p
            if invert < 0:
                value -= 1
                if value < self.minimum():
                    continue
            angle = p / fullRange * angleRange * invert
            reference.setAngle(startAngle - angle)
            textRect.setSize(fm.size(Qt.TextSingleLine, str(value)))
            textRect.moveCenter(reference.p2().toPoint())
            qp.drawText(textRect, Qt.AlignCenter, str(value))


# if __name__ == '__main__':
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     dial = ValueDial(minimum=1, maximum=11)
#     dial.setNotchesVisible(True)
#     dial.show()
#     sys.exit(app.exec_())


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(12, 42, 1200, 650)
        # self.showFullScreen()
        self.setWindowTitle("     AMERICAN UNIVERSITY OF MONTSERRAT  ONTARIO RESEARCH MEDICAL  COPYRIGHT")
        self.setWindowIcon(QIcon('burger.ico'))
        self.setStyleSheet('background-color:black; color:white;')# violet!, orange!, (gray)!, khaki!, lawngreen!, palegreen!, springgreen, skyblue!, saddlebrown!

        self.main()

    def main(self):
        self.username = 'Q N Software Services'
        self.userAge = '121212'
        self.user_id = str(random.randint(0, 1212121212))
        self.dateStamp = str(datetime.datetime.now())
        self.number = 1
        self.i = 0
        self.image = 'logo.png'

        self.radio_btns= []

        self.counter = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                   28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
                   53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
                   78, 79]

        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        #self.imagesTemplate = {'T2M1': {}, 'T2M2': {}, 'T2M3': {}, 'T2M4': {}, 'T2M5': {}, 'T2M6': {}, 'T2M7': {}, 'T2M8': {}, 'T2M9': {}, 'T2M10': {}, 'T2F1': {}, 'T2F2': {}, 'T2F3': {}, 'T2F4': {}, 'T2F5': {}, 'T2F6': {}, 'T2F7': {}, 'T2F8': {}, 'T2F9': {}, 'T2F10': {}, 'T3M1': {}, 'T3M2': {}, 'T3M3': {}, 'T3M4': {}, 'T3M5': {}, 'T3M6': {}, 'T3M7': {}, 'T3M8': {}, 'T3M9': {}, 'T3M10': {}, 'T3F1': {}, 'T3F2': {}, 'T3F3': {}, 'T3F4': {}, 'T3F5': {}, 'T3F6': {}, 'T3F7': {}, 'T3F8': {}, 'T3F9': {}, 'T3F10': {}, 'T4M1': {}, 'T4M2': {}, 'T4M3': {}, 'T4M4': {}, 'T4M5': {}, 'T4M6': {}, 'T4M7': {}, 'T4M8': {}, 'T4M9': {}, 'T4M10': {}, 'T4F1': {}, 'T4F2': {}, 'T4F3': {}, 'T4F4': {}, 'T4F5': {}, 'T4F6': {}, 'T4F7': {}, 'T4F8': {}, 'T4F9': {}, 'T4F10': {}, 'T5M1': {}, 'T5M2': {}, 'T5M3': {}, 'T5M4': {}, 'T5M5': {}, 'T5M6': {}, 'T5M7': {}, 'T5M8': {}, 'T5M9': {}, 'T5M10': {}, 'T5F1': {}, 'T5F2': {}, 'T5F3': {}, 'T5F4': {}, 'T5F5': {}, 'T5F6': {}, 'T5F7': {}, 'T5F8': {}, 'T5F9': {}, 'T5F10': {}}
        self.imagesTemplate = {'T2M1': '0', 'T2M2': '0', 'T2M3': '0', 'T2M4': '0', 'T2M5': '0', 'T2M6': '0', 'T2M7': '0', 'T2M8': '0', 'T2M9': '0', 'T2M10': '0', 'T2F1': '0', 'T2F2': '0', 'T2F3': '0', 'T2F4': '0', 'T2F5': '0', 'T2F6': '0', 'T2F7': '0', 'T2F8': '0', 'T2F9': '0', 'T2F10': '0', 'T3M1': '0', 'T3M2': '0', 'T3M3': '0', 'T3M4': '0', 'T3M5': '0', 'T3M6': '0', 'T3M7': '0', 'T3M8': '0', 'T3M9': '0', 'T3M10': '0', 'T3F1': '0', 'T3F2': '0', 'T3F3': '0', 'T3F4': '0', 'T3F5': '0', 'T3F6': '0', 'T3F7': '0', 'T3F8': '0', 'T3F9': '0', 'T3F10': '0', 'T4M1': '0', 'T4M2': '0', 'T4M3': '0', 'T4M4': '0', 'T4M5': '0', 'T4M6': '0', 'T4M7': '0', 'T4M8': '0', 'T4M9': '0', 'T4M10': '0', 'T4F1': '0', 'T4F2': '0', 'T4F3': '0', 'T4F4': '0', 'T4F5': '0', 'T4F6': '0', 'T4F7': '0', 'T4F8': '0', 'T4F9': '0', 'T4F10': '0', 'T5M1': '0', 'T5M2': '0', 'T5M3': '0', 'T5M4': '0', 'T5M5': '0', 'T5M6': '0', 'T5M7': '0', 'T5M8': '0', 'T5M9': '0', 'T5M10': '0', 'T5F1': '0', 'T5F2': '0', 'T5F3': '0', 'T5F4': '0', 'T5F5': '0', 'T5F6': '0', 'T5F7': '0', 'T5F8': '0', 'T5F9': '0', 'T5F10': '0'}

        self.categoryValue = {'T2M': 0, 'T2F': 0, 'T3M': 0, 'T3F': 0, 'T4M': 0, 'T4F': 0, 'T5M': 0, 'T5F': 0, }

        self.pixmap1212 = QPixmap('12.png')
        self.pixmap21212 = self.pixmap1212.scaled(1400, 180, Qt.KeepAspectRatio)
        self.label21212 = QLabel()
        self.label21212.setPixmap(self.pixmap21212)
        self.label21212.setStyleSheet("border-radius:5px;")
        self.label21212.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.label21212)

        self.label_2 = QLabel("AMERICAN UNIVERSITY OF MONTSERRAT")
        self.label_2.setAlignment(Qt.AlignHCenter)
        self.label_2.setFixedHeight(22)
        self.label_2.setStyleSheet("font-family:arial; font-size: 20px; border-radius: 36px; text-align:center; transform: rotate(90deg)")
        # vbox.addWidget(self.label_2)

        self.label_212 = QLabel("ONTARIO RESEARCH MEDICAL\nCOPYRIGHT")
        self.label_212.setAlignment(Qt.AlignHCenter)
        self.label_212.setFixedHeight(14)
        self.label_212.setStyleSheet("font-family:arial; font-size: 12px; border-radius: 36px; text-align:center; transform: rotate(90deg)")
        # vbox.addWidget(self.label_212)

        #n = 378  # 378% for 800 px width and 672% for 1400px
        #self.lcd.setStyleSheet(f"width: 100%;height: 0;background: #b4c0be;position: relative;border-top-left-radius: {n}% {n}%;border-top-right-radius: {n}% {n}%;")

        self.dial = ValueDial()
        self.dial.setStyleSheet('background-color: cyan; overflow: hidden;') #  width:100%; height:50%; max-width: 250px; padding-bottom: 50%;
        self.dial.setNotchesVisible(True)
        self.dial.autoFillBackground()
        self.dial.setFixedWidth(300)
        self.dial.setMaximum(5)
        self.dial.setMinimum(1)
        self.dial.valueChanged.connect(self.value)

        self.widget = QWidget()
        vbox.addWidget(self.widget)

        self.pixmap = QPixmap('black.png')
        self.pixmap2 = self.pixmap.scaled(400, 200)
        self.label2 = QLabel()
        self.label2.setPixmap(self.pixmap2)
        self.label2.setStyleSheet("border-radius:5px;")
        self.label2.setAlignment(Qt.AlignCenter)
        hbox1212 = QHBoxLayout()






        self.label = QLabel("    1    ")
        self.label.setFont(QFont("Helvetica", 36))
        self.label.setStyleSheet("font-family:times new roman; color:white; font-size: 36px; border-radius: 1cm; text-align:center;")
        self.label.setAlignment(Qt.AlignCenter)

        self.label6 = QLabel("Likeliness\n\tScale\t")
        self.label6.setFont(QFont("Helvetica", 29))
        self.label6.setStyleSheet("font-family:times new roman; color:black; font-size: 22px; border-radius: 1cm; border-color:black; border: 14px inset #1C6EA4; background-color:black; text-align:center;")
        self.label6.setAlignment(Qt.AlignCenter)
        # self.label6.setFixedWidth(245)

        self.btn1 = QPushButton()
        self.btn1.setIcon(QIcon('b4.PNG'))
        self.btn1.setIconSize(QSize(140, 70))
        # self.btn1.setStyleSheet("font-family:arial, cursive; color:black; font-size: 16px; border-radius: 1cm; border-color:white; border: 6px inset white; background-color:white; text-align:center;")
        self.btn1.clicked.connect(self.get_info)
        self.btn1.setFixedWidth(180)
        self.btn1.setFixedHeight(50)

        # self.btn1.setMaximumWidth(int(self.width() * 0.35))

        self.btn2 = QPushButton()
        self.btn2.setIcon(QIcon('b3.PNG'))
        self.btn2.setIconSize(QSize(140, 70))
        # self.btn2.setStyleSheet("font-family:arial, cursive; color:black; font-size: 16px; border-radius: 1cm; border-color:white; border: 6px inset white; background-color:white; text-align:center;")
        self.btn2.clicked.connect(self.getImageData)
        self.btn2.setFixedWidth(180)
        self.btn2.setFixedHeight(50)



        # self.btn2.setMaximumWidth(int(self.width() * 0.35))

        self.btn3 = QPushButton()
        self.btn3.setIcon(QIcon('b1.PNG'))
        self.btn3.setIconSize(QSize(140, 70))
        # self.btn3.setStyleSheet("font-family:arial, cursive; color:black; font-size: 16px; border-radius: 1cm; border-color:white; border: 6px inset white; background-color:white; text-align:center;")
        self.btn3.clicked.connect(self.start)
        self.btn3.setFixedWidth(180)
        self.btn3.setFixedHeight(50)

        # self.btn3.setMaximumWidth(int(self.width() * 0.35))

        self.btn4 = QPushButton("STOP")
        self.btn4.setStyleSheet("background-color:RED;")

        self.btn5 = QPushButton()
        self.btn5.setIcon(QIcon('b2.PNG'))
        self.btn5.setIconSize(QSize(140, 70))
        # self.btn5.setStyleSheet("font-family:arial, cursive; color:black; font-size: 16px; border-radius: 1cm; border-color:white; border: 6px inset white; background-color:white; text-align:center;")
        self.btn5.clicked.connect(self.newQuestion)
        self.btn5.setFixedWidth(180)
        self.btn5.setFixedHeight(50)

        # self.btn5.setMaximumWidth(int(self.width() * 0.35))

        label12 = QLabel()
        label12.setFixedWidth(122)



        hbox.setAlignment(Qt.AlignCenter)

        hbox2 = QHBoxLayout()

        vbox.addLayout(hbox)
        vbox12 = QVBoxLayout()
        vbox12.setAlignment(Qt.AlignBottom)
        vbox12.addWidget(self.btn3)
        vbox12.addWidget(self.btn5)
        vbox12.addWidget(self.btn2)
        vbox12.addWidget(self.btn1)
        # vbox.addWidget(self.btn4)
        vbox12.setAlignment(Qt.AlignBottom)
        # hbox2.addLayout(vbox12)

        hbox1212.addLayout(vbox12)
        hbox1212.addWidget(self.label2)
        vb1212 = QVBoxLayout()
        self.label.setStyleSheet('color:white;')
        self.dial.setFixedHeight(280)
        self.label12121212 = QLabel("\n3")
        self.label12121212.setAlignment(Qt.AlignCenter)
        self.label12121212.setFont(QFont("Helvetica", 22))
        # vb1212.addWidget(self.label12121212)
        vb1212.addWidget(self.dial)
        vb1212.setAlignment(Qt.AlignBottom)
        lb01 = QLabel("\n\n\n\n\n\n\t\t2\n\n\n\n\n\t\t1")
        lb01.setFont(QFont("Helvetica", 22))
        # hbox1212.addWidget(lb01)
        hbox1212.addLayout(vb1212)
        lb02 = QLabel("\n\n\n\n\n\n4\n\n\n\n\n5")
        lb02.setFont(QFont("Helvetica", 22))
        # hbox1212.addWidget(lb02)
        vbox.addLayout(hbox1212)

        hbox2.addWidget(self.label)

        self.pixmap12 = QPixmap('logo5.png')
        self.pixmap22 = self.pixmap12.scaled(160, 120, Qt.KeepAspectRatio)
        self.label1222 = QLabel()
        self.label1222.setPixmap(self.pixmap22)
        self.label1222.setStyleSheet("border-radius:5px;")
        self.label1222.setAlignment(Qt.AlignBottom)
        self.label1222.setFixedWidth(200)
        hbox2.addWidget(self.label1222)

        # vbox.addLayout(hbox2)

        self.setLayout(vbox)

    def start(self):
        self.btn1.setDisabled(True)
        self.btn2.setDisabled(True)
        self.btn3.setDisabled(True)
        self.btn5.setDisabled(True)

        # creating a timer object
        self.timer = QTimer()

        # adding action to timer
        self.timer.timeout.connect(self.changeImage)

        # update the timer every tenth second
        self.timer.start(5000)

        self.btn4.clicked.connect(lambda: self.timer.stop())
        self.btn4.clicked.connect(lambda: self.btn1.setEnabled(True))
        self.btn4.clicked.connect(lambda: self.btn2.setEnabled(True))

    def open(self):
        global image_link12
        path = QFileDialog.getOpenFileName(self, 'Open a file', '',
                                           'All Files (*.*)')
        if path != ('', ''):

            image_link12 = path[0]
        self.link.setText(image_link12)

    def value(self):
        value = self.dial.value()
        self.label.setText("    " + str(value) + '    ')


    def changeImage(self):
        global pics
        global i12
        global keys
        global key
        global answers_chosen
        global user_category_name
        global user_category_value
        global prescription

        value = self.dial.value()
        self.imagesTemplate[key] = value





        self.i = random.randint(0, len(self.counter) - 1)



        key = keys[self.counter[self.i]]

        self.pixmap = QPixmap(pics[key])
        self.pixmap2 = self.pixmap.scaled(550, 400)
        self.label2.setPixmap(self.pixmap2)
        a = self.counter.pop(self.i)




        if len(self.counter) <= 0:
            value = self.dial.value()
            self.imagesTemplate[key] = value

            self.timer.stop()
            self.btn1.setEnabled(True)
            self.btn2.setEnabled(True)
            self.btn3.setEnabled(True)
            self.btn5.setEnabled(True)

            user_category_name = ''
            user_category_value = 0

            for myKey in self.imagesTemplate:
                new = myKey[0:3]
                self.categoryValue[new] += self.imagesTemplate[myKey]
                self.imagesTemplate[myKey] = str(self.imagesTemplate[myKey])


            for key in self.categoryValue:
                if self.categoryValue[key] >= user_category_value:
                    user_category_name = key
                    user_category_value = self.categoryValue[key]

            now = datetime.datetime.now()


            self.questionaire()

            db_answers = []

            for myKey2 in answers_chosen:
                db_answers.append(myKey2 + '\t' + answers_chosen[myKey2])

            db_answers = '\n'.join(db_answers)


            cur.execute(
                'INSERT INTO userData (id, dateStamp, name, age, T2M1, T2M2, T2M3, T2M4, T2M5, T2M6, T2M7, T2M8, T2M9, T2M10, T2F1, T2F2, T2F3, T2F4, T2F5, T2F6, T2F7, T2F8, T2F9, T2F10, T3M1, T3M2, T3M3, T3M4, T3M5, T3M6, T3M7, T3M8, T3M9, T3M10, T3F1, T3F2, T3F3, T3F4, T3F5, T3F6, T3F7, T3F8, T3F9, T3F10, T4M1, T4M2, T4M3, T4M4, T4M5, T4M6, T4M7, T4M8, T4M9, T4M10, T4F1, T4F2, T4F3, T4F4, T4F5, T4F6, T4F7, T4F8, T4F9, T4F10, T5M1, T5M2, T5M3, T5M4, T5M5, T5M6, T5M7, T5M8, T5M9, T5M10, T5F1, T5F2, T5F3, T5F4, T5F5, T5F6, T5F7, T5F8, T5F9, T5F10, T2Mscore, T2Fscore, T3Mscore, T3Fscore, T4Mscore, T4Fscore, T5Mscore, T5Fscore, userCategory, answers, prescription) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                (self.user_id, str(now),self.username, self.userAge, self.imagesTemplate['T2M1'], self.imagesTemplate['T2M2'], self.imagesTemplate['T2M3'],
                 self.imagesTemplate['T2M4'], self.imagesTemplate['T2M5'], self.imagesTemplate['T2M6'],
                 self.imagesTemplate['T2M7'], self.imagesTemplate['T2M8'], self.imagesTemplate['T2M9'],
                 self.imagesTemplate['T2M10'], self.imagesTemplate['T2F1'], self.imagesTemplate['T2F2'],
                 self.imagesTemplate['T2F3'], self.imagesTemplate['T2F4'], self.imagesTemplate['T2F5'],
                 self.imagesTemplate['T2F6'], self.imagesTemplate['T2F7'], self.imagesTemplate['T2F8'],
                 self.imagesTemplate['T2F9'], self.imagesTemplate['T2F10'], self.imagesTemplate['T3M1'],
                 self.imagesTemplate['T3M2'], self.imagesTemplate['T3M3'], self.imagesTemplate['T3M4'],
                 self.imagesTemplate['T3M5'], self.imagesTemplate['T3M6'], self.imagesTemplate['T3M7'],
                 self.imagesTemplate['T3M8'], self.imagesTemplate['T3M9'], self.imagesTemplate['T3M10'],
                 self.imagesTemplate['T3F1'], self.imagesTemplate['T3F2'], self.imagesTemplate['T3F3'],
                 self.imagesTemplate['T3F4'], self.imagesTemplate['T3F5'], self.imagesTemplate['T3F6'],
                 self.imagesTemplate['T3F7'], self.imagesTemplate['T3F8'], self.imagesTemplate['T3F9'],
                 self.imagesTemplate['T3F10'], self.imagesTemplate['T4M1'], self.imagesTemplate['T4M2'],
                 self.imagesTemplate['T4M3'], self.imagesTemplate['T4M4'], self.imagesTemplate['T4M5'],
                 self.imagesTemplate['T4M6'], self.imagesTemplate['T4M7'], self.imagesTemplate['T4M8'],
                 self.imagesTemplate['T4M9'], self.imagesTemplate['T4M10'], self.imagesTemplate['T4F1'],
                 self.imagesTemplate['T4F2'], self.imagesTemplate['T4F3'], self.imagesTemplate['T4F4'],
                 self.imagesTemplate['T4F5'], self.imagesTemplate['T4F6'], self.imagesTemplate['T4F7'],
                 self.imagesTemplate['T4F8'], self.imagesTemplate['T4F9'], self.imagesTemplate['T4F10'],
                 self.imagesTemplate['T5M1'], self.imagesTemplate['T5M2'], self.imagesTemplate['T5M3'],
                 self.imagesTemplate['T5M4'], self.imagesTemplate['T5M5'], self.imagesTemplate['T5M6'],
                 self.imagesTemplate['T5M7'], self.imagesTemplate['T5M8'], self.imagesTemplate['T5M9'],
                 self.imagesTemplate['T5M10'], self.imagesTemplate['T5F1'], self.imagesTemplate['T5F2'],
                 self.imagesTemplate['T5F3'], self.imagesTemplate['T5F4'], self.imagesTemplate['T5F5'],
                 self.imagesTemplate['T5F6'], self.imagesTemplate['T5F7'], self.imagesTemplate['T5F8'],
                 self.imagesTemplate['T5F9'], self.imagesTemplate['T5F10'], self.categoryValue['T2M'], self.categoryValue['T2F'], self.categoryValue['T3M'], self.categoryValue['T3F'], self.categoryValue['T4M'], self.categoryValue['T4F'], self.categoryValue['T5M'], self.categoryValue['T5F'], user_category_name, db_answers, prescription))
            conn.commit()



            self.counter = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                            25, 26, 27,
                            28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
                            50, 51, 52,
                            53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
                            75, 76, 77,
                            78, 79]

            self.imagesTemplate = {'T2M1': '0', 'T2M2': '0', 'T2M3': '0', 'T2M4': '0', 'T2M5': '0', 'T2M6': '0',
                                   'T2M7': '0', 'T2M8': '0', 'T2M9': '0', 'T2M10': '0', 'T2F1': '0', 'T2F2': '0',
                                   'T2F3': '0', 'T2F4': '0', 'T2F5': '0', 'T2F6': '0', 'T2F7': '0', 'T2F8': '0',
                                   'T2F9': '0', 'T2F10': '0', 'T3M1': '0', 'T3M2': '0', 'T3M3': '0', 'T3M4': '0',
                                   'T3M5': '0', 'T3M6': '0', 'T3M7': '0', 'T3M8': '0', 'T3M9': '0', 'T3M10': '0',
                                   'T3F1': '0', 'T3F2': '0', 'T3F3': '0', 'T3F4': '0', 'T3F5': '0', 'T3F6': '0',
                                   'T3F7': '0', 'T3F8': '0', 'T3F9': '0', 'T3F10': '0', 'T4M1': '0', 'T4M2': '0',
                                   'T4M3': '0', 'T4M4': '0', 'T4M5': '0', 'T4M6': '0', 'T4M7': '0', 'T4M8': '0',
                                   'T4M9': '0', 'T4M10': '0', 'T4F1': '0', 'T4F2': '0', 'T4F3': '0', 'T4F4': '0',
                                   'T4F5': '0', 'T4F6': '0', 'T4F7': '0', 'T4F8': '0', 'T4F9': '0', 'T4F10': '0',
                                   'T5M1': '0', 'T5M2': '0', 'T5M3': '0', 'T5M4': '0', 'T5M5': '0', 'T5M6': '0',
                                   'T5M7': '0', 'T5M8': '0', 'T5M9': '0', 'T5M10': '0', 'T5F1': '0', 'T5F2': '0',
                                   'T5F3': '0', 'T5F4': '0', 'T5F5': '0', 'T5F6': '0', 'T5F7': '0', 'T5F8': '0',
                                   'T5F9': '0', 'T5F10': '0'}

            self.categoryValue = {'T2M': 0, 'T2F': 0, 'T3M': 0, 'T3F': 0, 'T4M': 0, 'T4F': 0, 'T5M': 0, 'T5F': 0}

            key = 'T2M1'


            answers_chosen = {}
            return

    def questionaire(self):


        self.settings_dialog = QDialog()
        self.settings_dialog.setModal(True)
        self.settings_dialog.setWindowTitle("Questionaire")
        self.settings_dialog.setWindowIcon(QIcon("burger.ico"))
        self.settings_dialog.setGeometry(363, 72, 630, 200)
        self.settings_dialog.setStyleSheet("background-color:#84eefa; border-radius: 1cm;")

        self.vbox11 = QVBoxLayout()

        self.label2012 = QLabel()
        self.label2012.setStyleSheet("background-color:white; border-color:black; border-radius: 12px;")
        self.label2012.setFont(QFont("Helvetica", 27))
        # self.label2012.setFixedHeight(36)
        # self.label.setFixedWidth(600)
        self.label2012.setAlignment(Qt.AlignCenter)
        self.vbox11.addWidget(self.label2012)


        hbox = QVBoxLayout()


        self.nextQuestion()

        btn_submit2 = QPushButton('Submit')
        btn_submit2.setStyleSheet("background-color:yellow; color: black;border-radius:20px;")
        btn_submit2.setFont(QFont("Helvetica", 16))
        btn_submit2.setFixedHeight(44)
        btn_submit2.clicked.connect(self.nextQuestion)
        # btn_submit2.released.connect(lambda: settings_dialog.close())

        vbox_master = QVBoxLayout()
        vbox_master.addLayout(self.vbox11)
        vbox_master.addWidget(btn_submit2)

        self.vbox11.setAlignment(Qt.AlignCenter)
        vbox_master.setAlignment(Qt.AlignCenter)

        self.settings_dialog.setLayout(vbox_master)
        self.settings_dialog.exec_()

        self.radio_btns = []

    def nextQuestion(self):
        global questions
        global question_index


        if question_index >= len(questions):
            self.settings_dialog.close()
            question_index = 0
            self.further_works()
            return

        question = questions[question_index]['text']

        self.label2012.setText(question)




        if len(self.radio_btns) >= 1:
            for radBtn in self.radio_btns:
                self.vbox11.removeWidget(radBtn)

        self.radio_btns = []




        for n, option in enumerate(questions[question_index]['options']):
            self.radio_btns.append(n)
            self.radio_btns[n] = QRadioButton()
            self.radio_btns[n].setText(option)
            self.radio_btns[n].setIcon(QIcon("burger.ico"))
            self.radio_btns[n].setIconSize(QSize(80, 80))
            self.radio_btns[n].setFont(QFont("Sanserif", 22))
            self.radio_btns[n].toggled.connect(self.on_selected)

        for radBtn in self.radio_btns:
            self.vbox11.addWidget(radBtn)

        question_index += 1



    def newQuestion(self):


        settings_dialog = QDialog()
        settings_dialog.setModal(True)
        settings_dialog.setStyleSheet("background-color:#84eefa; border-radius: 1cm;")
        settings_dialog.setWindowTitle("\t\t\tAdd New Question")
        settings_dialog.setWindowIcon(QIcon("burger.ico"))
        settings_dialog.setGeometry(327, 156, 700, 200)

        vbox_master = QVBoxLayout()
        vbox_master.setAlignment(Qt.AlignCenter)

        self.label4 = QLabel('QUESTION')
        self.label4.setStyleSheet(' color:black;')
        self.label4.setFont(QFont('times new roman', 27))
        vbox_master.addWidget(self.label4)

        self.QuestionText = QLineEdit()
        self.QuestionText.setFont(QFont('times new roman', 16))
        self.QuestionText.setStyleSheet('background-color:white; border-color:black; border-radius: 5px; color:black;')
        vbox_master.addWidget(self.QuestionText)

        label12 = QLabel()
        label12.setFixedHeight(12)
        vbox_master.addWidget(label12)

        self.label5 = QLabel('OPTIONS')
        self.label5.setStyleSheet(' color:black;')
        self.label5.setFont(QFont('times new roman', 27))
        vbox_master.addWidget(self.label5)

        self.textBox = QTextEdit()
        self.textBox.setStyleSheet('background-color:white; border-color:black; border-radius: 5px; color:black;')
        self.textBox.setFont(QFont('times new roman', 16))
        self.textBox.setFixedHeight(112)
        vbox_master.addWidget(self.textBox)

        label13 = QLabel()
        label13.setFixedHeight(12)
        vbox_master.addWidget(label13)

        btn_save = QPushButton('SAVE')
        btn_save.setStyleSheet("background-color:#0eeb37; border-radius:20px;")
        btn_save.setFont(QFont('times new roman', 27))
        btn_save.setFixedWidth(122)
        btn_save.clicked.connect(self.saveQuestion)
        btn_save.released.connect(lambda: settings_dialog.close())
        hbox = QHBoxLayout()
        hbox.addWidget(btn_save)

        vbox_master.addLayout(hbox)
        vbox_master.setAlignment(Qt.AlignCenter)

        settings_dialog.setLayout(vbox_master)
        settings_dialog.exec_()

    def further_works(self):
        self.show_message()
        self.doctor()

    def doctor(self):
        global answers_chosen
        settings_dialog = QDialog()
        settings_dialog.setModal(True)
        settings_dialog.setStyleSheet("background-color:magenta; border-radius: 1cm;")
        settings_dialog.setWindowTitle("Doctor's Prescription")
        settings_dialog.setWindowIcon(QIcon("burger.ico"))
        settings_dialog.setGeometry(100, 50, 1200, 650)

        vbox_master = QVBoxLayout()

        hbox = QHBoxLayout()
        labelList = []
        for i in range(8):
            labelList.append(QLabel())
            labelList[i].setFont(QFont('times new roman', 27))
            labelList[i].setStyleSheet('background-color:cyan; color:black; border-radius: 20px;')
            labelList[i].setAlignment(Qt.AlignCenter)
            hbox.addWidget(labelList[i])

        hbox2 = QHBoxLayout()
        labelList2 = []
        for i in range(8):
            labelList2.append(QLabel())
            labelList2[i].setFont(QFont('times new roman', 27))
            labelList2[i].setStyleSheet('background-color:cyan; color:black; border-radius: 20px;')
            labelList2[i].setAlignment(Qt.AlignCenter)
            hbox2.addWidget(labelList2[i])

        i = 0

        for key in self.categoryValue:

            labelList[i].setText(str(key))
            labelList2[i].setText(str(self.categoryValue[key]))
            i += 1

        vbox_master.addLayout(hbox)
        vbox_master.addLayout(hbox2)

        hbox3 = QHBoxLayout()

        label11 = QLabel(" Patient's Category : ")
        label11.setStyleSheet('background-color:cyan; color:black; border-radius: 20px;')
        label11.setFont(QFont('times new roman', 27))
        label11.setAlignment(Qt.AlignCenter)

        label12 = QLabel(user_category_name)
        label12.setStyleSheet('background-color:cyan; color:black; border-radius: 20px;')
        label12.setFont(QFont('times new roman', 27))
        label12.setAlignment(Qt.AlignCenter)

        hbox3.addWidget(label11)
        hbox3.addWidget(label12)

        vbox_master.addLayout(hbox3)

        mylist = QListWidget()
        mylist.setStyleSheet("font-family:times new roman; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset #1C6EA4; background-color:yellow; text-align:center; color:black;")

        i = 0
        for question in answers_chosen:
            a = QListWidgetItem()
            a.setText(question)
            a.setFont(QFont('times new roman', 27))
            a.setTextAlignment(Qt.AlignCenter)
            mylist.insertItem(i, a)
            i += 1
            a = QListWidgetItem()
            a.setText(answers_chosen[question])
            a.setFont(QFont('times new roman', 22))
            a.setTextAlignment(Qt.AlignCenter)
            mylist.insertItem(i, a)
            a = '   '
            i += 1
            mylist.insertItem(i, a)


            i += 1

        vbox_master.addWidget(mylist)

        self.textBox2 = QTextEdit()
        self.textBox2.setStyleSheet("font-family:times new roman; color:black; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset #1C6EA4; background-color:white; text-align:left;")
        self.textBox2.setFont(QFont('times new roman', 16))
        self.textBox2.setPlaceholderText("\n\tDoctor's Prescription (Dosage and Treatment)")

        vbox_master.addWidget(self.textBox2)

        btn12 = QPushButton('SUBMIT')
        btn12.setStyleSheet('background-color:lawngreen; color:black; border-radius: 18px; ')
        btn12.setFont(QFont('times new roman', 22))
        btn12.setFixedWidth(138)
        btn12.setFixedHeight(36)
        btn12.clicked.connect(self.doctorPrescription)
        btn12.released.connect(lambda: settings_dialog.close())

        hbox4 = QHBoxLayout()

        hbox4.addWidget(btn12)
        vbox_master.addLayout(hbox4)

        settings_dialog.setLayout(vbox_master)
        settings_dialog.exec_()

    def doctorPrescription(self):
        global prescription
        prescription = self.textBox2.toPlainText().lstrip().rstrip()

    def show_message(self):
        settings_dialog = QDialog()
        settings_dialog.setModal(True)
        settings_dialog.setStyleSheet("background-color:black; border-radius: 1cm;")
        settings_dialog.setWindowTitle("CONGRATULATIONS")
        settings_dialog.setWindowIcon(QIcon("burger.ico"))
        settings_dialog.setGeometry(336, 36, 700, 200)

        vbox_master = QVBoxLayout()

        self.img = QPixmap("message.png")
        self.img2 = self.img.scaled(700, 650, Qt.KeepAspectRatio)
        label = QLabel()
        label.setPixmap(self.img2)
        label.setAlignment(Qt.AlignCenter)

        vbox_master.addWidget(label)

        settings_dialog.setLayout(vbox_master)
        settings_dialog.exec_()

    def saveQuestion(self):
        global questions
        global answers_chosen

        newQuestion = self.QuestionText.text().lstrip().rstrip()
        newOptions = self.textBox.toPlainText().lstrip().rstrip()

        now = datetime.datetime.now()
        cur3.execute('INSERT INTO questions (dateStamp, question, options) VALUES (?, ?, ?)', (str(now), newQuestion, newOptions))
        conn3.commit()

        questions = []

        cur3.execute('''SELECT * FROM questions''')
        output2 = cur3.fetchall()
        answers_chosen = {}
        for data in output2:
            questions.append({'text': data[1], 'options': [item.lstrip().rstrip() for item in data[2].split('\n')]})
            answers_chosen[data[1]] = 'Nill'



    def on_selected(self):
        global questions
        global question_index
        global answers_chosen
        radio_button = self.sender()

        if radio_button.isChecked():

            answers_chosen[questions[question_index - 1]['text']] = radio_button.text()

    def get_info(self):
        print('successfully started')
        my_id = self.get_id()
        settings_dialog = QDialog()
        settings_dialog.setModal(True)
        settings_dialog.setStyleSheet("background-color:#84eefa; border-radius: 1cm;")
        settings_dialog.setWindowTitle("Primary Ad - Text Ad with Button")
        settings_dialog.setWindowIcon(QIcon("burger.ico"))
        settings_dialog.setGeometry(300, 175, 700, 200)

        vbox11 = QVBoxLayout()
        vbox12 = QVBoxLayout()
        hbox11 = QHBoxLayout()

        self.label201 = QLabel("Name")
        self.label201.setStyleSheet("background-color:white; color:black;")
        self.label201.setFont(QFont("Helvetica", 16))
        self.label201.setFixedHeight(36)
        # self.label.setFixedWidth(600)
        self.label201.setAlignment(Qt.AlignCenter)
        vbox11.addWidget(self.label201)

        self.name = QLineEdit()
        self.name.setStyleSheet("background-color:white; color:black;")
        self.name.setFont(QFont("Helvetica", 16))
        self.name.setFixedHeight(36)
        # self.label.setFixedWidth(600)
        self.name.setAlignment(Qt.AlignCenter)
        vbox12.addWidget(self.name)

        self.label202 = QLabel("Age")
        self.label202.setStyleSheet("background-color:white; color:black;")
        self.label202.setFont(QFont("Helvetica", 16))
        self.label202.setFixedHeight(36)
        # self.label.setFixedWidth(600)
        self.label202.setAlignment(Qt.AlignCenter)
        vbox11.addWidget(self.label202)

        self.age = QLineEdit()
        self.age.setStyleSheet("background-color:white; color:black;")
        self.age.setFont(QFont("Helvetica", 16))
        self.age.setFixedHeight(36)
        # self.label.setFixedWidth(600)
        self.age.setAlignment(Qt.AlignCenter)
        vbox12.addWidget(self.age)

        self.label203 = QLabel("ID ")
        self.label203.setStyleSheet("background-color:white; color:black;")
        self.label203.setFont(QFont("Helvetica", 16))
        self.label203.setFixedHeight(36)
        # self.label.setFixedWidth(600)
        self.label203.setAlignment(Qt.AlignCenter)
        vbox11.addWidget(self.label203)

        self.ID = QLabel(my_id)
        self.ID.setStyleSheet("background-color:white; color:black;")
        self.ID.setFont(QFont("Helvetica", 16))
        self.ID.setFixedHeight(36)
        # self.label.setFixedWidth(600)
        self.ID.setAlignment(Qt.AlignCenter)
        vbox12.addWidget(self.ID)

        self.label204 = QLabel("Date Stamp")
        self.label204.setStyleSheet("background-color:white; color:black;")
        self.label204.setFont(QFont("Helvetica", 16))
        self.label204.setFixedHeight(36)
        # self.label.setFixedWidth(600)
        self.label204.setAlignment(Qt.AlignCenter)
        vbox11.addWidget(self.label204)

        self.date = QLabel()
        self.date.setStyleSheet("background-color:white; color:black;")
        self.date.setFont(QFont("Helvetica", 16))
        self.date.setFixedHeight(36)
        # self.label.setFixedWidth(600)
        self.date.setAlignment(Qt.AlignCenter)
        vbox12.addWidget(self.date)

        date = datetime.datetime.now()
        self.date.setText(str(date))

        hbox11.addLayout(vbox11)
        hbox11.addLayout(vbox12)

        btn_submit = QPushButton('Submit')
        btn_submit.setStyleSheet("background-color:yellow; color: black;")
        btn_submit.setFont(QFont("Helvetica", 16))
        btn_submit.setFixedHeight(44)
        btn_submit.pressed.connect(self.submit1)
        btn_submit.released.connect(lambda: settings_dialog.close())

        vbox_master = QVBoxLayout()
        vbox_master.addLayout(hbox11)
        vbox_master.addWidget(btn_submit)

        settings_dialog.setLayout(vbox_master)
        settings_dialog.exec_()

    def submit1(self):
        self.username = self.name.text().upper().lstrip().rstrip()
        self.userAge = self.age.text().lstrip().rstrip()
        self.user_id = self.ID.text().lstrip().rstrip()
        self.dateStamp = self.date.text().lstrip().rstrip()






    def getImageData(self):
        global pics
        global image_link12
        settings_dialog = QDialog()
        settings_dialog.setModal(True)
        settings_dialog.setStyleSheet("background-color:#84eefa; border-radius: 1cm;")
        settings_dialog.setWindowTitle("Change Image")
        settings_dialog.setWindowIcon(QIcon("burger.ico"))
        settings_dialog.setGeometry(327, 156, 700, 200)

        vbox112 = QVBoxLayout()
        hbox12 = QHBoxLayout()
        hbox13 = QHBoxLayout()
        hbox14 = QHBoxLayout()
        hbox15 = QHBoxLayout()
        hbox11 = QHBoxLayout()

        self.cbox = QComboBox()
        self.cbox.currentIndexChanged.connect(self.hovered)
        self.cbox.setStyleSheet('outline: 5px inset #1C6EA4; outline-offset: 12px; color:black;')
        self.cbox.setFont(QFont('timesroman', 36))
        self.cbox.setFixedHeight(60)

        vbox112.addWidget(self.cbox)

        self.pixmap12 = QPixmap(self.image)
        self.pixmap22 = self.pixmap12.scaled(400, 300)
        self.label122 = QLabel()
        self.label122.setPixmap(self.pixmap2)
        self.label122.setAlignment(Qt.AlignCenter)
        vbox112.addWidget(self.label122)

        cur2.execute('''SELECT * FROM imageData''')
        #
        output = cur2.fetchall()
        #
        #
        c = 0
        for key12 in pics:
            pics[key12] = output[-1][c + 2]
            self.cbox.addItem(key12)
            c += 1

        self.label202 = QLabel("Image Link")
        self.label202.setStyleSheet("background-color:white; color:black;")
        self.label202.setFont(QFont("Helvetica", 16))
        self.label202.setFixedHeight(36)
        self.label202.setFixedWidth(200)
        self.label202.setAlignment(Qt.AlignCenter)
        hbox14.addWidget(self.label202)

        self.link = QPushButton(image_link12)
        self.link.setStyleSheet("background-color:khaki; color:black;")
        self.link.setFont(QFont("Helvetica", 16))
        self.link.setFixedHeight(36)
        # self.label.setFixedWidth(600)
        self.link.clicked.connect(self.open)
        hbox14.addWidget(self.link)


        self.label204 = QLabel("Date Stamp")
        self.label204.setStyleSheet("background-color:white; color:black;")
        self.label204.setFont(QFont("Helvetica", 16))
        self.label204.setFixedHeight(36)
        self.label204.setFixedWidth(200)
        self.label204.setAlignment(Qt.AlignCenter)
        hbox12.addWidget(self.label204)

        self.date = QLabel()
        self.date.setStyleSheet("background-color:white; color:black;")
        self.date.setFont(QFont("Helvetica", 16))
        self.date.setFixedHeight(36)
        # self.label.setFixedWidth(600)
        self.date.setAlignment(Qt.AlignCenter)
        hbox12.addWidget(self.date)
        mylabel2 = QLabel()
        mylabel2.setFixedHeight(22)

        vbox112.addWidget(mylabel2)
        vbox112.addLayout(hbox12)
        vbox112.addLayout(hbox14)

        date = datetime.datetime.now()
        self.date.setText(str(date))

        hbox11.addLayout(vbox112)
        # hbox11.addLayout(vbox12)

        btn_save = QPushButton('Save')
        btn_save.setStyleSheet(" border-radius:20px; background-color: cyan; color: white;")
        btn_save.setFont(QFont("Helvetica", 30))
        btn_save.setFixedHeight(44)
        btn_save.pressed.connect(self.save)
        # btn_save.released.connect(lambda: settings_dialog.close())
        hbox13.addWidget(btn_save)

        btn_submit = QPushButton('Submit')
        btn_submit.setStyleSheet(" border-radius:20px;background-color: #2af73b; color: black;")
        btn_submit.setFont(QFont("Helvetica", 27))
        btn_submit.setFixedHeight(44)
        btn_submit.pressed.connect(self.submit)
        btn_submit.released.connect(lambda: settings_dialog.close())
        hbox13.addWidget(btn_submit)

        mylabel = QLabel()
        mylabel.setFixedHeight(22)
        hbox15.addWidget(mylabel)

        mylabel3 = QLabel()
        mylabel3.setFixedHeight(12)


        vbox_master = QVBoxLayout()
        vbox_master.addLayout(hbox11)
        vbox_master.addLayout(hbox15)
        vbox_master.addLayout(hbox13)
        vbox_master.addWidget(mylabel3)

        settings_dialog.setLayout(vbox_master)
        settings_dialog.exec_()

    def hovered(self):
        global pics
        text = self.cbox.currentText()

        self.pixmap12 = QPixmap(pics[text])
        self.pixmap22 = self.pixmap12.scaled(200, 150, Qt.KeepAspectRatio)
        self.label122.setPixmap(self.pixmap22)

    def save(self):
        global pics

        text = self.cbox.currentText()
        link = self.link.text().lstrip().rstrip()
        x = '\\'
        y = '"'
        if x in link:
            link = link.split('\\')
            a = '/'
            link = a.join(link)

        if y in link:
            link = link.split('"')[1]

        print(text)
        print(link)

        pics[text] = link

    def submit(self):
        global pics

        text = self.cbox.currentText()
        link = self.link.text().lstrip().rstrip()
        x = '\\'
        y = '"'
        if x in link:
            link = link.split('\\')
            a = '/'
            link = a.join(link)

        if y in link:
            link = link.split('"')[1]
        date = self.date.text().lstrip().rstrip()
        cur2.execute('''SELECT * FROM imageData''')
        output = cur2.fetchall()
        id = str(int(output[-1][0]) + 1)

        #
        pics[text] = link


        try:
            cur2.execute(
                'INSERT INTO imageData (id, dateStamp, T2M1, T2M2, T2M3, T2M4, T2M5, T2M6, T2M7, T2M8, T2M9, T2M10, T2F1, T2F2, T2F3, T2F4, T2F5, T2F6, T2F7, T2F8, T2F9, T2F10, T3M1, T3M2, T3M3, T3M4, T3M5, T3M6, T3M7, T3M8, T3M9, T3M10, T3F1, T3F2, T3F3, T3F4, T3F5, T3F6, T3F7, T3F8, T3F9, T3F10, T4M1, T4M2, T4M3, T4M4, T4M5, T4M6, T4M7, T4M8, T4M9, T4M10, T4F1, T4F2, T4F3, T4F4, T4F5, T4F6, T4F7, T4F8, T4F9, T4F10, T5M1, T5M2, T5M3, T5M4, T5M5, T5M6, T5M7, T5M8, T5M9, T5M10, T5F1, T5F2, T5F3, T5F4, T5F5, T5F6, T5F7, T5F8, T5F9, T5F10) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                (id, str(date), pics['T2M1'], pics['T2M2'], pics['T2M3'],
                 pics['T2M4'], pics['T2M5'], pics['T2M6'],
                 pics['T2M7'], pics['T2M8'], pics['T2M9'],
                 pics['T2M10'], pics['T2F1'], pics['T2F2'],
                 pics['T2F3'], pics['T2F4'], pics['T2F5'],
                 pics['T2F6'], pics['T2F7'], pics['T2F8'],
                 pics['T2F9'], pics['T2F10'], pics['T3M1'],
                 pics['T3M2'], pics['T3M3'], pics['T3M4'],
                 pics['T3M5'], pics['T3M6'], pics['T3M7'],
                 pics['T3M8'], pics['T3M9'], pics['T3M10'],
                 pics['T3F1'], pics['T3F2'], pics['T3F3'],
                 pics['T3F4'], pics['T3F5'], pics['T3F6'],
                 pics['T3F7'], pics['T3F8'], pics['T3F9'],
                 pics['T3F10'], pics['T4M1'], pics['T4M2'],
                 pics['T4M3'], pics['T4M4'], pics['T4M5'],
                 pics['T4M6'], pics['T4M7'], pics['T4M8'],
                 pics['T4M9'], pics['T4M10'], pics['T4F1'],
                 pics['T4F2'], pics['T4F3'], pics['T4F4'],
                 pics['T4F5'], pics['T4F6'], pics['T4F7'],
                 pics['T4F8'], pics['T4F9'], pics['T4F10'],
                 pics['T5M1'], pics['T5M2'], pics['T5M3'],
                 pics['T5M4'], pics['T5M5'], pics['T5M6'],
                 pics['T5M7'], pics['T5M8'], pics['T5M9'],
                 pics['T5M10'], pics['T5F1'], pics['T5F2'],
                 pics['T5F3'], pics['T5F4'], pics['T5F5'],
                 pics['T5F6'], pics['T5F7'], pics['T5F8'],
                 pics['T5F9'], pics['T5F10']))

            conn2.commit()


        except:
            time.sleep(0.2)



    def get_id(self):
        global ids

        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        a = letters[random.randint(0, len(letters))]
        b = letters[random.randint(0, len(letters))]
        c = letters[random.randint(0, len(letters))]
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        num3 = random.randint(0, 9)
        num4 = random.randint(0, 9)

        id = a + b + str(num1) + str(num2) + str(num3) + str(num4)  + c

        while id in ids:
            a = letters[random.randint(0, len(letters))]
            b = letters[random.randint(0, len(letters))]
            c = letters[random.randint(0, len(letters))]
            num1 = random.randint(0, 9)
            num2 = random.randint(0, 9)
            num3 = random.randint(0, 9)
            num4 = random.randint(0, 9)

            id = a + b + str(num1) + str(num2) + str(num3) + str(num4) + c

        ids.append(id)
        return id















app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())

'''settings_dialog = QDialog()
        settings_dialog.setModal(True)
        settings_dialog.setStyleSheet("background-color:#84eefa; border-radius: 1cm;")
        settings_dialog.setWindowTitle("Change Image")
        settings_dialog.setWindowIcon(QIcon("burger.ico"))
        settings_dialog.setGeometry(327, 156, 700, 200)

        vbox_master = QVBoxLayout()

        settings_dialog.setLayout(vbox_master)
        settings_dialog.exec_()'''