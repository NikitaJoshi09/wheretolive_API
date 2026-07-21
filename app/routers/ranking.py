from fastapi import APIRouter,Depends
from sqlmodel import Session
from app.database import get_session
from app.services.ranking_service import get_overall_rating

router = APIRouter(prefix="/ranking",tags=["ranking"])


@router.get("/")
def overall_ranking(session:Session = Depends(get_session)):
    return get_overall_rating(session)
   

@router.get("/state/{state}")
def state_ranking(state:str):
    return{"message":f"State Ranking{state}"}

@router.get("/compares")
def compares_cities(city1:str,city2:str):
    return{"message":f"{city1} vs {city2}"}