from pony.orm import Database, Required
from settings import DB_CONFIG

db = Database()
db.bind(**DB_CONFIG)


class Urls(db.Entity):
    """Url"""
    hashed_url = Required(str, unique=True)
    full_url = Required(str, unique=True)


db.generate_mapping(create_tables=True)
