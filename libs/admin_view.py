from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QPainter, QIcon
from libs.global_var import admin_logined
from libs.get_pc_details import get_user_login

class AdminView(QWidget):
    def __init__(self):
        super().__init__()

        # Set the layout and apply styles
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.setStyleSheet('border: 2px solid #ffffff; border-radius: 5px; padding: 10px;')

        # Set background image
        self.background_image = QPixmap(':/icon/queen_app_store.jpg')  # Set the image path here
        self.windowOpacity = 0.1  # Opacity value (0.0 to 1.0)

        # Add the admin panel UI
        self.admin_panel_ui()
        self.apply_theme()

    def paintEvent(self, event):
        # Call the parent class paintEvent to handle widget rendering
        super().paintEvent(event)

        # Create a painter to draw the background image with low opacity
        painter = QPainter(self)
        painter.setOpacity(self.windowOpacity)  # Set the opacity level for the image
        painter.drawPixmap(self.rect(), self.background_image)  # Draw the background image
        painter.end()

    def apply_theme(self):
        # Apply style sheet for QWidget and the button
        self.setStyleSheet("""
            QWidget { background-color: #2E2E2E; color: #FFFFFF; border-radius: 10px; }
            QLabel { font-size: 20px; color: #FFFFFF; border: 2px solid #ff1111; }
            QPushButton { background-color: #2E2E2E; color: #FFFFFF; border: 2px solid #ff1111; font-size: 20px; }
        """)

    def admin_panel_ui(self):
        global admin_logined
        # Layout for the header
        header_layout  = QHBoxLayout()
        header_layout.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)
        self.main_layout.addLayout(header_layout)

        # Add admin details label
        self.admin_details = QLabel(f'Welcome Admin: {get_user_login()}')
        header_layout.addWidget(self.admin_details)

        # Create the logout button with an icon
        self.logout_button = QPushButton()
        logout_icon = QIcon(r':/icon/logout.png')
        self.logout_button.setIcon(logout_icon)  # Set the icon on the button
        self.logout_button.setFixedSize(50, 50)  # Set a fixed size for the button
        header_layout.addWidget(self.logout_button)
