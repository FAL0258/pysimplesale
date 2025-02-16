# This Python file uses the following encoding: utf-8
from src.mainwindow import MainWindow
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
import sys

if __name__ == "__main__":
    app = QApplication([])
    app.setOrganizationName("PySimpleSale")
    app.setApplicationName("PySimpleSale")
    app.setApplicationDisplayName("PySimpleSale")
    widget = MainWindow()
    widget.setWindowIcon(QIcon("data/icons/logo.svg"))
    sys.exit(app.exec())
