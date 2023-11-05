import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Keyboard Events Misoli")
        self.setGeometry(100, 100, 400, 300)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            print("Escape tugmasi bosildi. Dasturni yopamiz.")
        elif event.key() == Qt.Key_Space:
            print("Bo'sh joy tugmasi bosildi.")
        elif event.key() == Qt.Key_A and event.modifiers() == Qt.ControlModifier:
            print("Ctrl + A tugmalari bosildi.")
        else:
            print(f"Tugma {event.text()} bosildi.")

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
