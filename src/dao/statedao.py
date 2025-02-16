# This Python file uses the following encoding: utf-8
from PyQt6.QtSql import QSqlQuery, QSqlError
from src.entity.state import State


class StateDAO:
    def __init__(self):
        self.lastError = QSqlError()

    def select(self, stateId):
        query = QSqlQuery()
        query.prepare("SELECT name, code, country_id "
                      "FROM state "
                      "WHERE state_id = :stateId")
        query.bindValue(":stateId", stateId)
        query.exec()
        if query.next():
            return State(stateId,
                         query.value("name"),
                         query.value("code"),
                         query.value("country_id"))

    def delete(self, state):
        stateId = 0
        if type(state) == State:
            stateId = state.id
        else:
            stateId = state
        query = QSqlQuery()
        query.prepare("DELETE FROM state WHERE state_id = :stateId")
        query.bindValue("stateId", stateId)
        success = query.exec()
        self.lastError = query.lastError()
        return success

    def count(self):
        count = 0
        query = QSqlQuery()
        query.prepare("SELECT COUNT(*) FROM state")
        query.exec()
        query.next()
        count = query.value(0)
        return count

    def insert(self, state):
        query = QSqlQuery()
        query.prepare("INSERT INTO state (name, code, country_id) "
                      "VALUES (:name, :code, :countryId)")
        query.bindValue(":name", state.name)
        query.bindValue(":code", state.code)
        query.bindValue(":countryId", state.countryId)
        success = query.exec()
        self.lastError = query.lastError()
        return success
