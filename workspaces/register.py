from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox

class RegisterForm(QWidget):
    def __init__(self, main_app):  # Add 'main_app' parameter
        super().__init__()
        self.main_app = main_app  # Store reference to main application
        layout = QVBoxLayout()

        # Create fields for name, role, email, and password
        name_label = QLabel("Name")
        self.name_input = QLineEdit()

        role_label = QLabel("Role")
        self.role_input = QComboBox()
        self.role_input.addItems(["User", "Administrator"])  # Add roles as needed

        email_label = QLabel("Email")
        self.email_input = QLineEdit()

        password_label = QLabel("Password")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        register_button = QPushButton("Register")
        register_button.clicked.connect(self.attempt_register)

        # Add widgets to the layout
        layout.addWidget(name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(role_label)
        layout.addWidget(self.role_input)
        layout.addWidget(email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(register_button)

        self.setLayout(layout)

    def attempt_register(self):
        # Gather the input data from the form fields
        name = self.name_input.text()
        role = self.role_input.currentText()
        email = self.email_input.text()
        password = self.password_input.text()

        # Here you would implement validation and registration logic
        # If successful, switch to the main part of your application or show a success message

