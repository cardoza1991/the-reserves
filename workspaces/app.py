from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
import sys
from welcome import WelcomeScreen
from login import LoginForm
from register import RegisterForm


class MainApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Reserves")
        self.stacked_widget = QStackedWidget()  # This will hold the different screens
        self.setCentralWidget(self.stacked_widget)

        # Initialize your screens
        self.welcome_screen = WelcomeScreen(self)
        self.login_form = LoginForm(self)
        self.register_form = RegisterForm(self)

        # Add screens to the stacked widget
        self.stacked_widget.addWidget(self.welcome_screen)
        self.stacked_widget.addWidget(self.login_form)
        self.stacked_widget.addWidget(self.register_form)

        # Set the welcome screen as the first screen
        self.stacked_widget.setCurrentWidget(self.welcome_screen)


def main():
    app = QApplication(sys.argv)
    main_window = MainApplication()
    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

