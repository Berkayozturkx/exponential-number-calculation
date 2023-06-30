#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Üslü Sayı Hesaplama")
        
        grid = QGridLayout()
        
        grid.addWidget(QLabel("Taban(a):"),1,1)
        self.taban = QLineEdit()
        grid.addWidget(self.taban,1,2,1,3)
        
        grid.addWidget(QLabel("Kuvvet(n):"),2,1)
        self.kuvvet = QLineEdit()
        grid.addWidget(self.kuvvet,2,2,1,3)
        
        self.buton = QPushButton("Hesapla")
        self.buton.clicked.connect(self.hesapla)
        grid.addWidget(self.buton,3,4,1,1)
        
        self.sonuc = QLabel("")
        grid.addWidget(self.sonuc,4,2)
        
        v_box = QVBoxLayout()
        v_box.addStretch()
        v_box.addLayout(grid)
        v_box.addStretch()
        
        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        
        self.resize(300,175)
        self.setLayout(h_box)
        self.show()
        
    def hesapla(self):
        taban = 0
        try: taban = int(self.taban.text())
        except: pass
        
        kuvvet = 0
        try: kuvvet = int(self.kuvvet.text())
        except: pass
        
        sonuc = 1
        i = 1
        
        if(taban == 0 and kuvvet == 0):
            self.sonuc.setText("Tanımsız.")
        elif(taban < 0 and kuvvet > 0):
            while(i <= kuvvet):
                sonuc *= taban
                i += 1
            self.sonuc.setText("Sonuç: {}".format(sonuc))
        elif(taban > 0 and kuvvet > 0):
            while(i <= kuvvet):
                sonuc *= taban
                i += 1
            self.sonuc.setText("Sonuç: {}".format(sonuc))
        elif(taban < 0 and kuvvet < 0):
            self.sonuc.setText("Lütfen geçerli bir kuvvet giriniz.")
        
uygulama = QApplication(sys.argv)
pencere = MainWindow()
sys.exit(uygulama.exec_())


# In[ ]:




