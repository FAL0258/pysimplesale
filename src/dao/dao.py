# This Python file uses the following encoding: utf-8

from PyQt6.QtSql import QSqlQuery, QSqlError

class DAO:
    def __init__(self):
        self.lastError = QSqlError()
