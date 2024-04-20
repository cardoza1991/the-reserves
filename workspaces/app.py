from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
import sys
from welcome import WelcomeScreen
from login import LoginForm
from register import RegisterForm
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Example usage
logging.debug("This is a debug message")
logging.info("Application start")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")


class MainApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Reserves")
        self.stacked_widget = QStackedWidget()  # This will hold the different screens
        self.setCentralWidget(self.stacked_widget)

        # Initialize your screens
        self.welcome_screen = WelcomeScreen()
        self.login_form = LoginForm()
        self.register_form = RegisterForm()

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
