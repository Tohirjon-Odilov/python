from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton,QCompleter
from PyQt5.Qt import Qt 

from css import *


class NewWordWindow(Window):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add New Word")
        self.__initUI()
        self.show()
    
    def __initUI(self):
        self.v_box = QVBoxLayout()
        self.v_box_lang = QVBoxLayout()
        
        self.h_box_lang = QHBoxLayout()
        self.h_box_btns = QHBoxLayout()

        self.edit_eng = Edit()
        self.edit_eng.setPlaceholderText('English...')

        self.edit_uzb = Edit()
        self.edit_uzb.setPlaceholderText('Uzbek...')

        self.btn_save = QPushButton('Save')
        self.btn_save.setFixedSize(100, 60)
        self.btn_save.setStyleSheet("""background: #79AC78; 
                           border: 2px solid; 
                           border-radius: 20px;
                           font-size: 16px;
                           """)
        

        self.btn_menu = FooterButton('Menu')
        self.btn_list = FooterButton('List of Words')
        self.btn_search = FooterButton('Search')

        self.v_box_lang.addWidget(self.edit_eng)
        self.v_box_lang.addWidget(self.edit_uzb)

        self.h_box_lang.addLayout(self.v_box_lang)
        self.h_box_lang.addWidget(self.btn_save)

        self.h_box_btns.addWidget(self.btn_menu)
        self.h_box_btns.addWidget(self.btn_list)
        self.h_box_btns.addWidget(self.btn_search)

        self.v_box.addLayout(self.h_box_lang)
        self.v_box.addStretch()
        self.v_box.addLayout(self.h_box_btns)

        self.setLayout(self.v_box)
    
        # connect function to button
        self.btn_save.clicked.connect(self.write_word_file)
        
        # menu button
        self.btn_menu.clicked.connect(self.return_menu)
        
        # list button
        self.btn_list.clicked.connect(self.go_list_words)

        # search button
        self.btn_search.clicked.connect(self.go_search)
        
    def write_word_file(self):
        with open("data.json", "r+") as file:
            self.data = file.read()
            self.data = loads(self.data)
            file.seek(0)
            self.data[self.edit_eng.text()]= self.edit_uzb.text()
            file.write(dumps(self.data, indent=4))
            self.edit_eng.clear()
            self.edit_uzb.clear()

    def return_menu(self):
        self.close()
        self.menu = MenuWindow()
        
    def go_list_words(self):
        self.close()
        self.list_words = ListOfWordsWindow()
        
    def go_search(self):
        self.close()
        self.search = SearchWindow()
  