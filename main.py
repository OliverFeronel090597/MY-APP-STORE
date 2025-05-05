from PyQt6.QtWidgets        import (
    QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
    QStackedWidget, QDialog
)
from PyQt6.QtCore           import Qt
from PyQt6.QtGui            import QIcon   
import sys

from libs.HomeView         import HomeView
from libs.AppView          import AppView
from libs.AdminView        import AdminView
from libs.NotificationPannel  import TrayIcon
from libs.CustomPushbutton import ImageButton
from libs.AdminLogin       import AdminLogin
from libs.DatabaseConnection          import SQLite
from libs.DeviceDetails    import get_user_login
from libs.IconResource         import *
from libs.GlobalVar        import admin_logined, admin_privilege

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Queen App Store")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon(':/icon/queen_app_store.jpg'))

        self.database = SQLite()
        self.database.create_tables_if_not_exist()
        user_login = get_user_login()
        self.is_admin = self.database.get_user_stats(user_login)

        main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        main_widget.setLayout(self.main_layout)
        self.setCentralWidget(main_widget)

        self.content_layout = QHBoxLayout()
        self.main_layout.addLayout(self.content_layout)

        self.control_buttons_ui()

        self.stacked_widget = QStackedWidget()
        self.content_layout.addWidget(self.stacked_widget)

        self.home_view = HomeView()
        self.app_view = AppView()
        self.admin_view = AdminView()
        self.tray_message = TrayIcon()

        self.stacked_widget.addWidget(self.home_view)
        self.stacked_widget.addWidget(self.app_view)
        self.stacked_widget.addWidget(self.admin_view)

    def control_buttons_ui(self):
        self.function_buttons = QVBoxLayout()
        self.function_buttons.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.button_widget = QWidget()
        # self.button_widget.setStyleSheet('border: 2px solid #ffffff; border-radius: 5px; padding: 10px;')
        self.function_buttons.addWidget(self.button_widget)

        button_layout = QVBoxLayout()
        self.button_widget.setLayout(button_layout)

        self.login_admin = ImageButton(':/icon/login.png', 'Admin Login', 1)
        # self.login_admin.setToolTip('Admin Login')
        self.login_admin.setFixedSize(250, 50)
        self.login_admin.setStyleSheet('font-weight: bold; font-size: 20px;')
        self.login_admin.clicked.connect(self.show_login_form)

        self.home_button = ImageButton(':/icon/home.png', 'Home', 1)
        # self.home_button.setToolTip('Home')
        self.home_button.setFixedSize(250, 50)
        self.home_button.setStyleSheet('font-weight: bold; font-size: 20px;')
        self.home_button.clicked.connect(self.show_home_view)

        self.app_button = ImageButton(':/icon/app.png', 'Download Apps', 1)
        # self.app_button.setToolTip('Download Apps')
        self.app_button.setFixedSize(250, 50)
        self.app_button.setStyleSheet('font-weight: bold; font-size: 20px;')
        self.app_button.clicked.connect(self.show_app_view)

        self.admin_button = ImageButton(':/icon/admin.png', 'Admin Pannel', 1)
        # self.admin_button.setToolTip('Admin Pannel')
        self.admin_button.setFixedSize(250, 50)
        self.admin_button.setStyleSheet('font-weight: bold; font-size: 20px;')
        self.admin_button.setShortcut('CTRL+A')
        # self.admin_button.setEnabled( self.is_admin)
        self.admin_button.clicked.connect(self.show_admin_view)

        button_layout.addWidget(self.login_admin)
        button_layout.addWidget(self.home_button)
        button_layout.addWidget(self.app_button)
        button_layout.addWidget(self.admin_button)
        self.content_layout.addLayout(self.function_buttons)

    def show_home_view(self):
        self.stacked_widget.setCurrentWidget(self.home_view)
        # self.tray_message.show_message('Queen App Store Notification', 'Change view executed')
    def show_app_view(self):
        self.stacked_widget.setCurrentWidget(self.app_view)
        
    def show_admin_view(self):
        self.stacked_widget.setCurrentWidget(self.admin_view)
        
    def show_login_form(self):
        login_dialog = AdminLogin()  # Create the login dialog
        
        # Show the dialog and check if the user pressed OK
        if login_dialog.exec() == QDialog.DialogCode.Accepted:
            username, password = login_dialog.get_credentials()
        #     self.status_label.setText(f"Status: Logged in as {username}")
        # else:
        #     self.status_label.setText("Status: Login Cancelled")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())