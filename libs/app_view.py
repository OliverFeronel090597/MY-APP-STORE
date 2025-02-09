from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QPainter

class AppView(QWidget):
    def __init__(self):
        super().__init__()

        # Set the layout and apply styles
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setStyleSheet('border: 2px solid #ffffff; border-radius: 5px; padding: 10px;')

        # Set background image
        self.background_image = QPixmap(':/icon/queen_app_store.jpg')  # Set the image path here
        self.windowOpacity = 0.1  # Opacity value (0.0 to 1.0)

        # Add a label to display text
        app_label = QLabel("Welcome to the App View!")
        app_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        app_label.setStyleSheet('font-size: 24px; font-weight: bold;')
        layout.addWidget(app_label)

    def paintEvent(self, event):
        # Call the parent class paintEvent to handle widget rendering
        super().paintEvent(event)

        # Create a painter to draw the background image with low opacity
        painter = QPainter(self)
        painter.setOpacity(self.windowOpacity)  # Set the opacity level for the image
        painter.drawPixmap(self.rect(), self.background_image)  # Draw the background image
        painter.end()
