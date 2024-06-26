from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox
from models import User  # Assuming User model is defined in 'models.py'

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
        password = self.password_input.text()  # Remember to hash the password

        # Create a new user instance
        new_user = User(name=name, email=email, role=role, password=password)  # Assume hashing is done

        # Add the new user to the session and commit
        self.main_app.session.add(new_user)
        try:
            self.main_app.session.commit()
            print("User registered successfully.")
        except Exception as e:
            self.main_app.session.rollback()
            print("Failed to register user:", str(e))
            # Handle the error appropriately, e.g., show an error message box

