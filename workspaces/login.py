from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class LoginForm(QWidget):
    def __init__(self, main_app):  # Add 'main_app' parameter
        super().__init__()
        self.main_app = main_app  # Store reference to main application
        layout = QVBoxLayout()

        # Create fields for email and password
        email_label = QLabel("Email")
        self.email_input = QLineEdit()

        password_label = QLabel("Password")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        login_button = QPushButton("Login")
        login_button.clicked.connect(self.attempt_login)

        layout.addWidget(email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(login_button)

        self.setLayout(layout)

    def attempt_login(self):
        email = self.email_input.text()
        password = self.password_input.text()
        # Here you would implement validation and authentication logic
        # If successful, switch to the main part of your application
