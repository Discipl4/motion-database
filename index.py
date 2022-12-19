from fastapi import FastAPI
from routes.motion import user 

app = FastAPI()
app.include_router(user)
