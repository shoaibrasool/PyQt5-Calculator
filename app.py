import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.input_display = QLineEdit(self)
        self.input_display.setReadOnly(True)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        grid_layout = QGridLayout()
        row, col = 0, 0
        for button_text in buttons:
            button = QPushButton(button_text, self)
            button.setFixedSize(50, 50)  # Set fixed size for buttons
            button.clicked.connect(self.button_click_handler(button_text))
            grid_layout.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.input_display)
        main_layout.addLayout(grid_layout)

        self.setGeometry(300, 300, 300, 400)
        self.setWindowTitle('CUTIE Calculator')
        self.show()

    def button_click_handler(self, button_text):
        def handler():
            self.on_button_click(button_text)
        return handler

    def on_button_click(self, button_text):
        current_text = self.input_display.text()

        if button_text == '=':
            try:
                result = str(eval(current_text))
                self.input_display.setText(result)
            except Exception as e:
                self.input_display.setText('Error')
        elif button_text == 'C':
            self.input_display.clear()
        else:
            new_text = current_text + str(button_text)
            self.input_display.setText(new_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorApp()
    sys.exit(app.exec_())
