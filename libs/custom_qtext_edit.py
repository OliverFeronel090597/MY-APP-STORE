from PyQt6.QtWidgets        import QTextEdit
from PyQt6.QtGui            import QFont, QPainter, QPixmap
from PyQt6.QtCore           import Qt
from libs.resources         import *

class CustomQTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.font_size = 10
        self.setFont(QFont('Arial', self.font_size))
        self.placeholder_image = QPixmap(':/icon/queen_app_store.jpg')  # Replace with your image path
        self.image_opacity = 0.1  # Set the opacity level (0.0 to 1.0)

    def paintEvent(self, event):
        # Call the parent class paintEvent to handle text rendering
        super().paintEvent(event)

        # Draw the background image with the specified opacity
        painter = QPainter(self.viewport())
        painter.setOpacity(self.image_opacity)
        painter.drawPixmap(self.rect(), self.placeholder_image)
        painter.end()

    # def wheelEvent(self, event):
    #     if not self.toPlainText().strip():
    #         return  # Do not allow font change if no data
    #     if event.modifiers() == Qt.KeyboardModifier.ControlModifier:
    #         if event.angleDelta().y() > 0:
    #             self.font_size = min(self.font_size + 1, 20)  # Max font size 20
    #         else:
    #             self.font_size = max(self.font_size - 1, 10)  # Min font size 10
    #         self.setFont(QFont('Arial', self.font_size))
    #     else:
    #         super().wheelEvent(event)


