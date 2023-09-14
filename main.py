import fastapi as _fastapi
import sqlalchemy.orm as _orm
import services as _services, schemas as _schemas
from typing import List

app = _fastapi.FastAPI()

_services.create_database()

@app.post("/api/", response_model=_schemas.User)
def create_user(
    user: _schemas.UserCreate, db:_orm.Session=_fastapi.Depends(_services.get_db)
    ):
    db_user_email = _services.get_user_by_email(db=db, email=user.email)
    db_user_name = _services.get_user_by_name(db=db, name=user.name)
    if db_user_email:
        raise _fastapi.HTTPException(
            status_code=400, detail="Email already in use"
            )
    elif db_user_name:
        raise _fastapi.HTTPException(
            status_code=400, detail="Email already in use"
            )
    return _services.create_user(db=db, user=user)

@app.get("/api/", response_model=List[_schemas.User])
def read_users(
    skip: int=0, limit: int=10, db:_orm.Session=_fastapi.Depends(_services.get_db) 
):
    users = _services.get_users(db=db, skip=skip, limit=limit)
    return users

@app.get("/api/{user_name}", response_model=_schemas.User)
def read_user(user_name: str, db: _orm.Session=_fastapi.Depends(_services.get_db)):
    db_user = _services.get_user(user_name=user_name.lower(), db=db)
    if db_user is None:
        raise _fastapi.HTTPException(status_code=404, detail="User does not exist")
    
    return db_user

@app.delete("/api/{user_name}")
def delete_user(user_name: str, db: _orm.Session=_fastapi.Depends(_services.get_db)):
    db_user = _services.delete_user(db=db, user_name=user_name)
    if db_user is None:
        raise _fastapi.HTTPException(status_code=404, detail="User does not exist")
    return {"message": f"{user_name} detials has been successfully deleted"}

@app.put("/api/{user_name}")
def update_user(user_name: str, user: _schemas.UserCreate, db: _orm.Session=_fastapi.Depends(_services.get_db)):
    db_user = _services.update_user(db=db, user_name=user_name, user=user)
    if db_user is None:
        raise _fastapi.HTTPException(status_code=404, detail="User does not exist")
    return {"message": f"{user_name} details has been successfully updated"}