import datetime as _dt

import passlib.hash as _hash
import sqlalchemy as _sql

import main.database as _database


class User(_database.Base):
    __tablename__ = "users"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    email = _sql.Column(_sql.String, unique=True, index=True)
    hashed_password = _sql.Column(_sql.String)
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)

    def verify_password(self, password: str):
        return _hash.bcrypt.verify(password, self.hashed_password)
