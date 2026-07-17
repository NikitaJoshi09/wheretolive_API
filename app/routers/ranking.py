from fastapi import APIRouter

router = APIRouter(prefix="/ranking",tags=["ranking"])


@router.get("/")
def overall_ranking():
    return{"message":f"overall_ranking"}

@router.get("/state/{state}")
def state_ranking(state:str):
    return{"message":f"State Ranking{state}"}

@router.get("/compares")
def compares_cities(city1:str,city2:str):
    return{"message":f"{city1} vs {city2}"}