from PyQt5.QtWidgets import QPushButton

class MainButton(QPushButton):
    def __init__(self, text) -> None:
        super().__init__(text)
        
        self.setStyleSheet("""
            background-color: crimson; 
            color: white; 
            border-radius: 5px; 
            font-size: 20px; 
            padding: 15px 50px;
            
        """)
