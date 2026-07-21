from sqlmodel import Session,select,func
from app.models.city import City,CityMetrics

def get_overall_rating(session:Session):
    statement = (
        select(
            City.name,
            func.avg(CityMetrics.cost_of_living_index).label("cost"),
            func.avg(CityMetrics.air_quality_index).label("air"),
            func.avg(CityMetrics.safety_score).label("safety"),
            func.avg(CityMetrics.healthcare_score).label("healthcare"),
        )
        .join(CityMetrics,City.id == CityMetrics.city_id)
        .group_by(City.name)
    )
    results = session.exec(statement).all()
    ranked = []
    for name,cost,air,safety,healthcare in results:
        score = (safety * 0.35)+ (air*0.25)+(healthcare * 0.25) - (cost/100* 0.15)
        ranked.append({"city":name,"livability_score":round(score,2)})
    ranked.sort(key = lambda x:x["livability_score"],reverse = True)
    return ranked    