import database as _database, models as _models, schemas as _schemas
import sqlalchemy.orm as _orm
import datetime as _dt


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally: 
        db.close()

def get_user_by_email(db: _orm.Session, email: str):
    return db.query(_models.User).filter(_models.User.email == email).first()

def get_user_by_name(db: _orm.Session, name: str):
    return db.query(_models.User).filter(_models.User.name == name).first()

def create_user(db: _orm.Session, user: _schemas.UserCreate):
    fake_hashed_password = user.password + 'thisisnotsecure'
    # converting name to lowercase
    user.name = user.name.lower()
    db_user = _models.User(name=user.name,gender=user.gender,track=user.track,email=user.email,github_profile=user.github_profile,hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: _orm.Session, skip:int, limit:int):
    return db.query(_models.User).offset(skip).limit(limit).all()

def get_user(db: _orm.Session, user_name: str):
    return db.query(_models.User).filter(_models.User.name == user_name).first()

def delete_user(db: _orm.Session, user_name: str):
    db.query(_models.User).filter(_models.User.name == user_name).delete()
    db.commit()

def update_user(db: _orm.Session, user: _schemas.UserCreate, user_name: str):
    db_user = get_user(db=db, user_name=user_name.lower())
    db_user.name = user.name.lower()
    db_user.email = user.email
    db_user.gender = user.gender
    db_user.github_profile = user.github_profile
    db_user.password = user.password
    db_user.date_last_updated = _dt.datetime.now()
    db.commit()
    db.refresh(db_user)
    return db_user