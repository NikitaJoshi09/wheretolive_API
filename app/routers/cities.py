from fastapi import APIRouter,Depends,HTTPException
from sqlmodel import SQLModel,Session,select
from app.database import get_session
from app.models.city import City,CityMetrics

router = APIRouter(prefix="/Cities",tags=["cities"])


@router.get("/")
def list_cities(session:Session =Depends(get_session)):
    return session.exec(select(City)).all()

@router.get("/{city_id}")
def list(city_id:int,session:Session = Depends(get_session)):
    city = session.get(City,city_id)
    if not City:
        raise HTTPException(status_code=404,detail="city not found")
    return city


  
@router.post("/{city_id}")
def add_city():
    return{"message":f"New city Created"}


@router.put("/{city_id}")
def update_city(city_id:int):
    return{"message":f"city Id updated{city_id}"}

@router.get("/{city_id}")
def history_city(city_id:int,session:Session= Depends(get_session)):
    statement = select(CityMetrics).where(CityMetrics.city_id == city_id)
    return session.exec(statement).all()
    