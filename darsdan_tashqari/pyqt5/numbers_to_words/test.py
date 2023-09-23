from PyQt5 import QtWidgets

# Create a PyQt5 application and main window
app = QtWidgets.QApplication([])
window = QtWidgets.QWidget()
window.setGeometry(100, 100, 400, 200)

# Create a QLineEdit widget and set its placeholder text
line_edit = QtWidgets.QLineEdit()
line_edit.setPlaceholderText("Enter text here")

# Apply the CSS style to the placeholder text
line_edit.setStyleSheet("QLineEdit::placeholder { color: yellow; }")

# Create a layout and add the QLineEdit widget to the main window
layout = QtWidgets.QVBoxLayout()
layout.addWidget(line_edit)
window.setLayout(layout)

# Show the main window
window.show()

# Run the application's event loop
app.exec_()
