# This Python file uses the following encoding: utf-8
from PyQt6.QtSql import QSqlQuery
from src.entity.city import City


class CityDAO:
    def __init__(self):
        pass

    def select(self, cityId):
        query = QSqlQuery()
        query.prepare("SELECT name, state_id FROM "
                      " city WHERE city_id = :cityId")
        query.bindValue(":cityId", cityId)
        query.exec()
        if query.next():
            return City(cityId,
                        query.value("name"),
                        query.value("state_id"))

    def count(self):
        count = 0
        query = QSqlQuery()
        query.prepare("SELECT COUNT(*) FROM city")
        query.exec()
        query.next()
        count = query.value(0)
        return count

    def insert(self, city):
        query = QSqlQuery()
        query.prepare("INSERT INTO city (name, "
                      "state_id) VALUES (:name,"
                      ":stateId)")
        query.bindValue(":name", city.name)
        query.bindValue(":stateId", city.stateId)
        query.exec()

    def update(self, city):
        query = QSqlQuery()
        query.prepare("UPDATE city SET name = :name "
                      "WHERE city_id = :cityId")
        query.bindValue(":cityId", city.id)
        query.exec()
