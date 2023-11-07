from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QProgressBar, QMessageBox
import time

# Handling button clicks
def search_weather():
    import time

    # Create main line
    search_mode()

    # Cheate message box
    msgBox = QMessageBox()
    msgBox.setWindowTitle('Результат')
    msgBox.setText('Хз, посмотри на улицу :/')
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.setFixedSize(WW, WH)

    msgBox.show()
    return_value = msgBox.exec()

    if return_value == QMessageBox.Ok:
        standart_mode()

def standart_mode():
    # Window settings
    WW, WH = 252, 150

    # Create app
    app = QApplication([])

    # Create the window
    window = QWidget()
    window.setFixedSize(WW, WH)
    window.setWindowTitle('Погода')

    # Create widgets
    text1 = QLabel('<h1>Погода от Shaertiar.</h1>')
    text2 = QLabel('<h3>Введите <b>ваш</b> регион</h3>')

    line_input = QLineEdit('Москва')

    button = QPushButton('Поиск')

    # Create main line
    line1 = QVBoxLayout()
    line2 = QHBoxLayout()

    # Past widgets to lines
    line2.addWidget(line_input, 50, Qt.AlignCenter)
    line2.addWidget(button, 20, Qt.AlignCenter)

    line1.addStretch(1)
    line1.addWidget(text1, alignment=Qt.AlignCenter)
    line1.addWidget(text2, alignment=Qt.AlignCenter)
    line1.addStretch(1)
    line1.addLayout(line2)
    line1.addStretch(1)

    button.clicked.connect(search_weather)

    # Past line to window
    window.setLayout(line1)

    # Show app
    window.show()
    app.exec()

def search_mode():
    # Window settings
    WW, WH = 252, 150

    # Create app
    app = QApplication([])

    # Create the window
    window = QWidget()
    window.setFixedSize(WW, WH)
    window.setWindowTitle('Обработка...')

    # Create widgets
    text = QLabel('<h1>Загрузка...</h1>')

    # Create main line
    line = QVBoxLayout()

    line.addWidget(text, alignment=Qt.AlignCenter)

    # Past line to window
    window.setLayout(line)

    standart_mode()

    # Show app
    window.show()

standart_mode()