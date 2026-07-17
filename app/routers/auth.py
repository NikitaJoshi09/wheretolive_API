from fastapi import APIRouter
router = APIRouter(prefix="/auth",tags=["auth"])

@router.post("/signup")
def signup():
    return {"message": f"signup successfully"}

@router.post("/login")
def login():
    return {"message": f"login successfully"}

@router.get("/profile")
def profile():
    return {"message": f"profile protected"}


