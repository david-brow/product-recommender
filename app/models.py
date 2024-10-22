from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ProductCatalog(Base):
    __tablename__ = 'product_catalog'
    product_id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    price = Column(Float)

class CustomerFeedback(Base):
    __tablename__ = 'customer_feedback'
    feedback_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product_catalog.product_id'))
    customer_id = Column(Integer)
    rating = Column(Integer)
    review = Column(Text)

class MarketingCampaign(Base):
    __tablename__ = 'marketing_campaign'
    campaign_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product_catalog.product_id'))
    campaign_name = Column(String)
    discount = Column(Float)
    start_date = Column(String)
    end_date = Column(String)
