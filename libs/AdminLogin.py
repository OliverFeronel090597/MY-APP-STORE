from PyQt6.QtWidgets        import QDialog, QLineEdit, QFormLayout, QDialogButtonBox
from PyQt6.QtCore           import Qt
from PyQt6.QtGui            import QIcon

# Login Popup Class
class AdminLogin(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Form")
        self.setWindowIcon(QIcon(':/icon/queen_app_store.jpg'))
        self.setFixedSize(300, 150)
        self.setModal(True)  # This makes the dialog modal (disables main UI)

        self.setWindowFlags(
            self.windowFlags() & ~Qt.WindowType.WindowMaximizeButtonHint & ~Qt.WindowType.WindowMinimizeButtonHint
        )
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        # Form Layout
        form_layout = QFormLayout()
        
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        
        # Buttons (OK & Cancel)
        self.button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        
        # Add Widgets to Form
        form_layout.addRow("Username:", self.username_input)
        form_layout.addRow("Password:", self.password_input)
        form_layout.addRow(self.button_box)
        
        self.setLayout(form_layout)

    def get_credentials(self):
        return self.username_input.text(), self.password_input.text()
