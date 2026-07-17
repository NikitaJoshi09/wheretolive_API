from fastapi import APIRouter
router = APIRouter(prefix="/ai",tags=["AI"])

@router.get("/summary")
def ai_summary():
    return{"message": "AI summary"}

@router.get("/recommendation")
def ai_recommendation():
    return{"message":"AI Recommendation"}