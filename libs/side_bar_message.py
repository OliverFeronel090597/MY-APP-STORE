from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt6.QtGui import QIcon, QAction
from libs.resources import *


class TrayIcon(QSystemTrayIcon):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setIcon(QIcon(':/icon/queen_app_store.jpg'))
        self.setVisible(True)
        
        # Create context menu
        tray_menu = QMenu(parent)
        exit_action = QAction("Exit", parent)
        exit_action.triggered.connect(self.exit_application)
        tray_menu.addAction(exit_action)
        
        self.setContextMenu(tray_menu)

    def show_message(self, title, message):
        self.showMessage(
            title, message, QSystemTrayIcon.MessageIcon.Information, 3000
        )

    def exit_application(self):
        QApplication.quit()
