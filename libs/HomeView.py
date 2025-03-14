from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QPainter

from libs.DeviceDetails import get_hostname, get_user_login
from libs.IconResource import *

class HomeView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(layout)

        self.placeholder_image = QPixmap(':/icon/queen_app_store.jpg')  # Replace with your image path
        self.image_opacity = 0.1  # Set the opacity level (0.0 to 1.0)

        # Create a QWidget to hold the user details
        self.details_widget = QWidget()
        self.details_layout = QVBoxLayout()
        self.details_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.details_widget.setLayout(self.details_layout)

        # Add the details_widget to the main layout
        layout.addWidget(self.details_widget)

        # Call user_details to display the labels
        self.user_details()
        self.apply_theme()

        # Make the HomeView widget expand to fill the available space
        self.setSizePolicy(self.sizePolicy().horizontalPolicy(), self.sizePolicy().verticalPolicy())

    def paintEvent(self, event):
        # Call the parent class paintEvent to handle text rendering
        super().paintEvent(event)

        # Create QPainter instance
        painter = QPainter(self)

        # Set opacity and draw the background image
        painter.setOpacity(self.image_opacity)
        painter.drawPixmap(self.rect(), self.placeholder_image)

        painter.end()

    def apply_theme(self):
        self.setStyleSheet("""
            QWidget { background-color: #2E2E2E; color: #FFFFFF; border-radius: 10px; }
            QLabel  { background-color: #2E2E2E; color: #FFFFFF; border: 2px solid #ff1111; font-size: 20px; }
        """)

    def user_details(self):
        # Set user login and hostname text
        self.login_user = QLabel(get_user_login())
        self.login_user.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.pc_host_name = QLabel(get_hostname())
        self.pc_host_name.setAlignment(Qt.AlignmentFlag.AlignRight)

        # Add both labels to the details_widget's layout
        self.details_layout.addWidget(self.login_user)
        self.details_layout.addWidget(self.pc_host_name)

        # Ensure the widget resizes automatically based on content
        self.details_widget.setSizePolicy(
            self.details_widget.sizePolicy().horizontalPolicy(),
            self.details_widget.sizePolicy().verticalPolicy()
        )
        self.details_widget.adjustSize()  # Adjust size to fit content
