import json

from setup_db import db
from const import OFFERS_JSON, ORDER_JSON, USERS_JSON
from models import User, Order, Offer


class GetData:
    @staticmethod
    def load_data(filename):
        with open(filename, encoding="utf-8") as file:
            return json.load(file)

    def create_db(self):
        db.create_all()

        users = self.load_data(USERS_JSON)
        orders = self.load_data(ORDER_JSON)
        offers = self.load_data(OFFERS_JSON)
        self.add_data_to_db(users, User)
        self.add_data_to_db(orders, Order)
        self.add_data_to_db(offers, Offer)

        db.session.commit()
        db.session.close()

    def add_data_to_db(self, json_data, model):
        for item in json_data:
            unit = model(**item)
            db.session.add(unit)
