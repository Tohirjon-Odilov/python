from json import dumps, loads
from googletrans import Translator
import sys

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton,QCompleter
from PyQt5.Qt import Qt 

from css import *


class MenuWindow(Window):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu")
        self.__initUI()
        self.show()
    
    def __initUI(self):
        self.v_box = QVBoxLayout()

        self.btn_add_new_word = Button('Add New Word')
        self.btn_list_of_words = Button('List of Words')
        self.btn_search_word = Button('Search Word')
        self.btn_exit = Button('Exit')

        self.v_box.setAlignment(Qt.AlignCenter)

        self.v_box.addStretch()
        self.v_box.addWidget(self.btn_add_new_word)
        self.v_box.addWidget(self.btn_list_of_words)
        self.v_box.addWidget(self.btn_search_word)
        self.v_box.addWidget(self.btn_exit)
        self.v_box.addStretch()

        self.setLayout(self.v_box)

        self.btn_add_new_word.clicked.connect(self.show_new_word)
        self.btn_list_of_words.clicked.connect(self.show_list)
        self.btn_search_word.clicked.connect(self.show_search)
        self.btn_exit.clicked.connect(self.exit_window)

    def show_new_word(self):
        self.close()
        self.new = NewWordWindow()
        self.new.show()

    def show_list(self):
        self.close()
        self.new = ListOfWordsWindow()
        self.new.show()

    def show_search(self):
        self.close()
        self.new = SearchWindow()
        self.new.show()

    def exit_window(self):
        self.close()

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
        