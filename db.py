from orator import DatabaseManager, Schema, Model

DATABASES = {
    "postgres": {
        "driver": "postgres",
        "host": "localhost",
        "database": "fastapigraph",
        "user": "mac",
        "password": "",
        "prefix": "",
        "port": 5432
    }
}

db = DatabaseManager(DATABASES)
schema = Schema(db)
Model.set_connection_resolver(db)