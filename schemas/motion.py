from config.date import now

def userEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "left":item["left"],
        "center":item["center"],
        "right":item["right"],
        "date":item["date"]
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]