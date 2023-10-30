from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton,QCompleter
from PyQt5.Qt import Qt 
from css import *

class ListOfWordsWindow(Window):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("List of Words")
        self.__initUI()
        self.show()
    
    def __initUI(self):
        self.v_box = QVBoxLayout()
        self.v_box_eng = QVBoxLayout()
        self.v_box_uzb = QVBoxLayout()
        
        self.h_box_lang = QHBoxLayout()
        self.h_box_btns = QHBoxLayout()

        self.label_eng = Label('English')
        self.label_uzb = Label('Uzbek')

        self.qlw_eng = QLW()
        self.qlw_uzb = QLW()

        self.btn_menu = FooterButton('Menu')
        self.btn_new_word = FooterButton('Add New Word')
        self.btn_search = FooterButton('Search')

        self.v_box_eng.addWidget(self.label_eng)
        self.v_box_eng.addWidget(self.qlw_eng)

        self.v_box_uzb.addWidget(self.label_uzb)
        self.v_box_uzb.addWidget(self.qlw_uzb)

        self.h_box_lang.addLayout(self.v_box_eng)
        self.h_box_lang.addLayout(self.v_box_uzb)

        self.h_box_btns.addWidget(self.btn_menu)
        self.h_box_btns.addWidget(self.btn_new_word)
        self.h_box_btns.addWidget(self.btn_search)

        self.v_box.addLayout(self.h_box_lang)
        self.v_box.addLayout(self.h_box_btns)

        self.setLayout(self.v_box)

        with open("./data.json", "r") as file:
            self.data = file.read()
            self.data = loads(self.data)
            for key, elem in self.data.items():
                self.qlw_eng.addItem(key)
                self.qlw_uzb.addItem(elem)
    
    
        # menu button
        self.btn_menu.clicked.connect(self.return_menu)
        
        # list button
        self.btn_new_word.clicked.connect(self.go_new_word)

        # search button
        self.btn_search.clicked.connect(self.go_search)
        
    def return_menu(self):
        self.close()
        self.menu = MenuWindow()
        
    def go_new_word(self):
        self.close()
        self.add_new_words = NewWordWindow()
        
    def go_search(self):
        self.close()
        self.search = SearchWindow()
      