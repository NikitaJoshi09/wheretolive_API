from fastapi import APIRouter

router = APIRouter(prefix="/comparisons",tags=["comparisons"])


@router.post("/")
def save_comparisons():
    return{"message":f"save_comparisons"}

@router.get("/mine")
def my_comparisons():
    return{"message":f"my saved comparisons"}

