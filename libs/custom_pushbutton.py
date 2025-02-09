from PyQt6.QtWidgets import QPushButton, QToolTip
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize

class ImageButton(QPushButton):
    def __init__(self, image_path, tooltip, is_active, icon_size=(50, 50), parent=None):
        super().__init__(parent)
        self.setEnabled(is_active)
        
        # Set the button icon using the provided image path
        self.setIcon(QIcon(image_path))
        
        # Set the icon size
        self.setIconSize(QSize(*icon_size))
        
        # Adjust the button size to match the icon
        self.setFixedSize(QSize(*icon_size))
        
        # Set tooltip
        self.setToolTip(tooltip)

        # Style adjustments: Small tooltip font and click effect fix
        self.setStyleSheet("""
            QPushButton {
                border: none;
                background-color: transparent;
                font-size: 20px;
                outline: none; /* Removes focus border */
            }
            QPushButton:hover {
                background-color: #444444;
                border-radius: 5px;
            }
            QPushButton:pressed {  /* Corrected from :clicked to :pressed */
                background-color: #ff1111;
                border-radius: 5px;
            }
            QPushButton:disabled {
                background-color: transparent; /* Keep transparent background */
                opacity: 1;                    /* Prevent fading */
                color: #AAAAAA;                /* Optional: Adjust text/icon tint if needed */
            }
            QToolTip {
                font-size: 10px;  /* Small tooltip font */
                color: #FFFFFF;
                background-color: #333333;
                border: 1px solid #AAAAAA;
                padding: 3px;
            }
        """)
