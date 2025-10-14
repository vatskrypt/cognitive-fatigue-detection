from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient
import jwt
from jwt import encode as jwt_encode
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException
from bson import ObjectId

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"],
    allow_credentials = True,
    allow_methods= ["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    username: str = None # Username field optional
    email: str
    password: str


#MongoDB Connection

client = MongoClient("mongodb://localhost:27017")
db = client["mydatabase"]
users_collection = db["users"]

#secret key for signing the token

SECRET_KEY = "your-secret-key-goes-here"
security = HTTPBearer()

@app.get("/")
def homepage():
    return {"message":"Welcome to the homepage"}

@app.post("/login")
def login(user : User):
    #check if user exists in the db
    user_data = users_collection.find_one(
        {"email":user.email,
         "password":user.password}
    )
    if user_data:
        #Generate a token
        token = generate_token(user.email)
        #convert onjectID to string
        user_data["_id"] = str(user_data["_id"])
        #Store user details and token in local storage
        user_data["token"] = token
        return user_data
    return {
        "message":"Invalid email or password"
    }

@app.post("/register")
def register(user: User):
    #check if user exists in the db
    existing_user = users_collection.find_one(
        {"email":user.email}
    )
    if existing_user:
        return {"message":"User already exists"}
    #insert new user into DB
    user_dict = user.model_dump()
    users_collection.insert_one(user_dict)
    #Generate a token
    token = generate_token(user.email)
    #convert objectID to string
    user_dict["_id"]=str(user_dict["_id"])
    #store user details and token in local storage
    user_dict["token"]=token
    return user_dict

@app.get("/api/user")
def get_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    #extract token from the authorization header
    token = credentials.credentials
    # Authenticate and retrieve the user data from the database based on the token
    # Here, you would implement the authentication logic and fetch user details
    # based on the token from the database or any other authentication mechanism
    # For demonstration purposes, assuming the user data is stored in local storage
    # Note: Local storage is not accessible from server-side code
    # This is just a placeholder to demonstrate the concept
    user_data = {
        "username":"John Doe",
        "email":"johndoe@example.com"
    }
    if user_data["username"] and user_data["email"]:
        return user_data
    raise HTTPException(status_code=401, detail="Invalid token")

def generate_token(email:str) -> str:
    payload = {"email":email}
    token = jwt_encode(payload, SECRET_KEY, algorithm="HS256")
    return token

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="0.0.0.0",port=8000)