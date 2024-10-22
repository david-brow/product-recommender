from sqlalchemy.orm import Session
from .models import ProductCatalog, CustomerFeedback, MarketingCampaign

def get_products(db: Session):
    return db.query(ProductCatalog).all()

def get_feedback_for_product(db: Session, product_id: int):
    return db.query(CustomerFeedback).filter(CustomerFeedback.product_id == product_id).all()

def get_campaign_for_product(db: Session, product_id: int):
    return db.query(MarketingCampaign).filter(MarketingCampaign.product_id == product_id).first()
