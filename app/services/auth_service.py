from passlib.context import CryptContext

pwd_conntext = CryptContext(schemes=["bcrypt"],deprecated = "auto")
ALGORITHM = "HS256"

def hash_password(password:str):
     return pwd_conntext.hash(password)