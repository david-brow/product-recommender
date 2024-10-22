import json
from sqlalchemy.orm import Session
from .database import SessionLocal, init_db
from .models import ProductCatalog, CustomerFeedback, MarketingCampaign

def load_json_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def seed_data():
    db: Session = SessionLocal()
    try:
        # Load sample data from JSON files
        products = load_json_data('data/products.json')
        feedbacks = load_json_data('data/feedback.json')
        campaigns = load_json_data('data/campaigns.json')

        # Insert data into the database
        for product in products:
            db.add(ProductCatalog(**product))

        for feedback in feedbacks:
            db.add(CustomerFeedback(**feedback))

        for campaign in campaigns:
            db.add(MarketingCampaign(**campaign))

        db.commit()
        print("Database seeded successfully!")
    except Exception as e:
        db.rollback()
        print(f"Error seeding database: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    init_db()
    seed_data()
