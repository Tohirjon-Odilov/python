from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton,QCompleter
from PyQt5.Qt import Qt 
from css import *


class SearchWindow(Window):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search")
        self.__initUI()
        self.show()
    
    def __initUI(self):
        self.v_box = QVBoxLayout()
        
        self.h_box_search = QHBoxLayout()
        self.h_box_btns = QHBoxLayout()

        self.edit_search = Edit()
        self.edit_search.setPlaceholderText('Enter a word...')

        self.btn_search = FooterButton('search')
        self.btn_search.setFixedHeight(35)
        self.btn_search.clicked.connect(self.searched_word)

        self.qlw_search = QLW()

        self.btn_menu = FooterButton('Menu')
        self.btn_list = FooterButton('List of Words')
        self.btn_new_word = FooterButton('Add New Word')

        self.h_box_search.addWidget(self.edit_search)
        self.h_box_search.addWidget(self.btn_search)

        self.h_box_btns.addWidget(self.btn_menu)
        self.h_box_btns.addWidget(self.btn_list)
        self.h_box_btns.addWidget(self.btn_new_word)

        self.v_box.addLayout(self.h_box_search)
        self.v_box.addWidget(self.qlw_search)
        self.v_box.addLayout(self.h_box_btns)

        self.setLayout(self.v_box)
        
        with open("./data.json", "r") as file:
            self.data = file.read()
            self.data = loads(self.data)
            self.lst = list()
            for i in self.data.keys():
                self.lst.append(i)
            self.completer = QCompleter(self.lst)
        self.edit_search.setCompleter(self.completer)
        
        
    def searched_word(self):
        translator = Translator()
        english_word = self.edit_search.text()
        user = translator.translate(english_word, dest="uz")
        format_data = f"{english_word}  -->  {user.text} "
        self.qlw_search.addItem(format_data)
        with open("./data.json", "r+") as file:
            self.old_data = file.read()
            self.old_data = loads(self.old_data)
            file.seek(0)
            self.old_data[english_word]= user.text
            file.write(dumps(self.old_data, indent=4))
        
        # menu button
        self.btn_menu.clicked.connect(self.return_menu)
        
        # list button
        self.btn_list.clicked.connect(self.go_list_words)

        # search button
        self.btn_new_word.clicked.connect(self.go_new_word)
        
    def return_menu(self):
        self.close()
        self.menu = MenuWindow()
        
    def go_list_words(self):
        self.close()
        self.list_words = ListOfWordsWindow()
        
    def go_new_word(self):
        self.close()
        self.new_word = NewWordWindow()
        