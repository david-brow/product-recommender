from fastapi import APIRouter, HTTPException
from ..ai import generate_recommendations

router = APIRouter()

@router.get("/recommendations/{customer_id}")
def get_recommendations(customer_id: int):
    prompt = f"Generate recommendations for customer {customer_id}."
    recommendations = generate_recommendations(prompt)
    if not recommendations:
        raise HTTPException(status_code=404, detail="No recommendations found")
    return {"recommendations": recommendations}
