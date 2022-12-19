from fastapi import APIRouter
from models.motion import User 
from config.db import conn 
from schemas.motion import userEntity, usersEntity
from bson import ObjectId
from config.date import now

user = APIRouter()
db = conn.arduino.test

def last_date():
    query_date = {
        "date": now
    }
    date = db.find_one(query_date)
    return date

@user.get('/')
async def get_entire_docs():
    return usersEntity(db.find())


@user.post('/')
async def insert_or_update_docs(user: User):
    if last_date() == None:
        db.insert_one(user.dict())
        return usersEntity(db.find())
    else:
        update = {
            "$inc":user.dict(exclude={"date"})
        }
        db.update_one({"date": now}, update)
        return usersEntity(db.find())


@user.get('/now')
async def get_today_docs():
    query_date = {
        "date": now
    }
    return usersEntity(db.find(query_date))
    

@user.post('/now')
async def insert_or_update_today_docs(user: User):
    if last_date() == None:
        db.insert_one(user.dict())
        return usersEntity(db.find())
    else:
        update = {
            "$inc":user.dict(exclude={"date"})
        }
        query_date = {
        "date": now
        }
        db.update_one({"date": now}, update)
        return usersEntity(db.find(query_date))
