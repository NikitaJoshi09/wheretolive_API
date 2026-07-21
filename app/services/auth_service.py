from passlib.context import CryptContext
from jose import jwt
from datetime import datetime,timedelta
import os
from dotenv import load_dotenv
load_dotenv()

pwd_context = CryptContext(schemes=["bcrypt"],deprecated = "auto")
SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"

def hash_password(password:str):
     return pwd_context.hash(password)

def verify_pasword(plain,hashed):
     return pwd_context.verify(plain,hashed)

def create_access_token(data:dict,expires_minutes: int=60):
     to_encoded = data.copy()
     expire = datetime.utcnow()+ timedelta(minutes=expires_minutes)
     to_encoded.update({"exp":expire})
     return jwt.encode(to_encoded,SECRET_KEY,algorithm=ALGORITHM)