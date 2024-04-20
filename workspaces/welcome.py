from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class WelcomeScreen(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app

        layout = QVBoxLayout()

        welcome_label = QLabel("Welcome to The Reserves Workspaces")
        login_button = QPushButton("Login")
        register_button = QPushButton("Register")

        # Connect buttons to the functions that switch the stacked widget index
        login_button.clicked.connect(self.show_login)
        register_button.clicked.connect(self.show_register)

        layout.addWidget(welcome_label)
        layout.addWidget(login_button)
        layout.addWidget(register_button)

        self.setLayout(layout)

    def show_login(self):
        self.main_app.stacked_widget.setCurrentWidget(self.main_app.login_form)

    def show_register(self):
        self.main_app.stacked_widget.setCurrentWidget(self.main_app.register_form)

