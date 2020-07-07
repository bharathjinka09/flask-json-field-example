from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost:5432/blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class Example(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    json_column = db.Column(JSON)


# create Example table in blog db
# db.create_all()

def insert_data():
    # example1 = Example(json_column={"key": "value", "myarray": [
                       # 39, 323, 83, 382, 102], "objects": {"name": "Anthony"}})
    # db.session.add(example1)
    example2 = Example(json_column={"key": "newvalue", "myarray": [23, 676, 45, 88, 99], "objects": {"name": "Brian"}})
    db.session.add(example2)
    db.session.commit()

# insert_data()


def query():
    # example1 = Example.query.first()
    # print(example1)
    # print(example1.json_column)
    # print(example1.json_column['myarray'][4])
    # print(type(example1.json_column))
    # example = Example.query.filter(Example.json_column['objects']['name'].astext == 'Brian').first()
    # print(example)
    results = Example.query.filter(
        Example.json_column['objects']['name'].astext == 'Brian').all()
    print(results)

    all_records = Example.query.all()
    for record in all_records:
        print(record)


query()
