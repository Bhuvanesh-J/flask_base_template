import uuid

from registrations.create_app import db
from sqlalchemy import Column, String, DateTime, \
    VARCHAR

class Student(db.Model):
    __tablename__ = 'student'
    _id = db.Column(db.String(40), default=str(uuid.uuid4()), primary_key=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    email = Column(String(20))
    hashed_password = Column(VARCHAR(20))
    gender = Column(String(10))
    dob = Column(DateTime())