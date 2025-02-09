from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QScrollArea
from PyQt6.QtCore import Qt, QPoint

class DraggableScrollArea(QScrollArea):
    def __init__(self):
        super().__init__()
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # Hide scrollbar

        self.container = QWidget()
        self.hbox = QHBoxLayout(self.container)
        self.hbox.setSpacing(10)

        # Add buttons as example widgets
        for i in range(1, 11):  # 10 buttons
            btn = QPushButton(f"Item {i}")
            self.hbox.addWidget(btn)

        self.container.setLayout(self.hbox)
        self.setWidget(self.container)

        # Variables for drag control
        self.is_dragging = False
        self.start_pos = QPoint()
        self.scroll_start = 0

    def mousePressEvent(self, event):
        """ Detect mouse press to start dragging """
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_dragging = True
            self.start_pos = event.pos()
            self.scroll_start = self.horizontalScrollBar().value()

    def mouseMoveEvent(self, event):
        """ Drag widgets by updating scroll position """
        if self.is_dragging:
            delta = event.pos().x() - self.start_pos.x()
            self.horizontalScrollBar().setValue(self.scroll_start - delta)

    def mouseReleaseEvent(self, event):
        """ Stop dragging on mouse release """
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_dragging = False

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Drag to Slide Widgets")
        self.setGeometry(100, 100, 500, 200)

        self.scroll_area = DraggableScrollArea()
        self.setCentralWidget(self.scroll_area)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
