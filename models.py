import datetime as _dt
import sqlalchemy as _sql
import sqlalchemy.orm as _orm

import database as _database

class User(_database.Base):
    __tablename__ = 'users'
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String, unique=True, index=True)
    email =  _sql.Column(_sql.String, unique=True, index=True)
    track = _sql.Column(_sql.String, index=True)
    gender = _sql.Column(_sql.String, index=True)
    github_profile = _sql.Column(_sql.String, index=True)
    hashed_password = _sql.Column(_sql.String)
    is_active = _sql.Column(_sql.Boolean, default=True)
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    date_last_updated = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow) 