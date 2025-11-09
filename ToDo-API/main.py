from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class information(BaseModel):
    id:int
    name:str
    password:str
    email:str

@app.post("/register")
async def signup(user:information, ):

    
