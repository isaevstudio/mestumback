from fastapi import FastAPI, Depends, Request
# from app.model import PostSchema, UserSchema, UserLoginSchema
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import decodeJWT
from sqlalchemy import create_engine
from app.model import UserPlayer


users = []

app = FastAPI()


@app.get("/", tags=["test"], dependencies=[Depends(JWTBearer())])
async def greet(request: Request):

    token =  request.headers.get("Authorization")
    # {"Authorization" : "Bearer ioapdsfujpaosd;ifjadsfoiasdfd"}
    token = token.split(" ")[1]
    data = decodeJWT(token)

    if data == None:
        return {"error": "Invalid token"}, 401

    print(data)
    try:    
        _uid = data['uid']
        _is_active = data['is_active']
    except:
        return {'msg':'Missing value'}

    UserPlayer.create(
        uid=_uid,
        is_active = _is_active
    )
    

    return {"UserID": data["uid"], 'Status': data['is_active']}

