class FactoryModels:
    def init_person(self, db):
        class Person(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            first_name = db.Column(db.Text)
            last_name = db.Column(db.Text)

            db.create_all()

        return Person
