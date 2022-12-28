"""
model
"""

# pylint: disable=R0903

import os
from peewee import Model, CharField, DateTimeField, ForeignKeyField


from playhouse.db_url import connect

db = connect(os.environ.get("DATABASE_URL", "sqlite:///my_database.db"))


class User(Model):
    """
    User
    """
    name = CharField(max_length=255, unique=True)
    password = CharField(max_length=255)

    class Meta:
        """
        Meta
        """
        database = db


class Task(Model):
    """
    Task
    """
    name = CharField(max_length=255)
    performed = DateTimeField(null=True)
    performed_by = ForeignKeyField(model=User, null=True)

    class Meta:
        """
        Meta
        """
        database = db
