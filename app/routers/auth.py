from fastapi import APIRouter,Depends,HTTPException
from sqlmodel import Session,select
from app.database import get_session
from app.models.user import User
from app.services.auth_service import hash_password

router = APIRouter(prefix="/auth",tags=["Auth"])

@router.post("/signup")
def signup(name:str,email:str,password:str,session:Session=Depends(get_session)):
    existing = session.exec(select(User).where(User.email == email)).first()
    if existing:
        raise HTTPException(status_code=400,detail="User already registered")
    user = User(name=name, email=email, password=hash_password(password))
    session.add(user)
    session.commit()
    return {"message": f"signup successfully"}

@router.post("/login")
def login():
    return {"message": f"login successfully"}

@router.get("/profile")
def profile():
    return {"message": f"profile protected"}


