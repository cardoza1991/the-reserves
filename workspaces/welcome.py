from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class WelcomeScreen(QWidget):
    # Include the 'main_app' reference as a parameter in the initializer
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app  # Save the reference to the main application

        layout = QVBoxLayout()

        welcome_label = QLabel("Welcome to The Reserves Workspaces")
        login_button = QPushButton("Login")
        register_button = QPushButton("Register")

        # Connect buttons to the function that switches the stacked widget index
        login_button.clicked.connect(self.show_login)
        register_button.clicked.connect(self.show_register)

        layout.addWidget(welcome_label)
        layout.addWidget(login_button)
        layout.addWidget(register_button)

        self.setLayout(layout)
        
    # Method to show the login form
    def show_login(self):
        self.main_app.stacked_widget.setCurrentWidget(self.main_app.login_form)

    # Method to show the registration form
    def show_register(self):
        self.main_app.stacked_widget.setCurrentWidget(self.main_app.register_form)

