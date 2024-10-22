
# eCommerce Data Integration and Personalization API

This project integrates product catalog, customer feedback, and marketing campaign data, providing AI-powered product recommendations through a FastAPI backend.

---

## **Project Overview**
This API serves:
- **Product Catalog:** List of products available on the platform.
- **Customer Feedback:** Reviews and ratings for products.
- **Marketing Campaigns:** Ongoing or past promotions for products.
- **AI Recommendations:** Personalized product recommendations using OpenAI API.

---

## **Endpoints**
- **GET /api/products**: Retrieve all enriched product data.
- **GET /api/recommendations/{customer_id}**: Get personalized recommendations for a customer.

---

## **Prerequisites**
- **Python 3.8+**
- **SQLite** (comes pre-installed with Python)
- **OpenAI API Key**: Get your API key from [OpenAI](https://beta.openai.com/signup/)

---

## **Installation**

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd ecommerce_project
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## **Database Setup**

1. **Create the SQLite database:**
   ```bash
   sqlite3 ecommerce.db < setup.sql
   ```

2. **Populate the database with sample data:**
   Run the seeder script to insert data from JSON files:
   ```bash
   python -m app.seeder
   ```
   If successful, you will see:
   ```
   Database seeded successfully!
   ```

---

## **Run the Application**

1. **Start the FastAPI server:**
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Access the API:**
   - **Products Endpoint:** [http://localhost:8000/api/products](http://localhost:8000/api/products)
   - **Recommendations Endpoint:** [http://localhost:8000/api/recommendations/{customer_id}](http://localhost:8000/api/recommendations/{customer_id})

---

## **Scalability Considerations**

1. **Caching:** Use Redis to cache frequent queries and improve response times.
2. **Asynchronous Processing:** Integrate Celery for background jobs like sending AI requests.
3. **Database Optimization:** Add indexes to commonly queried fields (e.g., `product_id`) to improve performance.
4. **Load Balancing:** Use Nginx or another load balancer to distribute traffic across multiple instances.

---

## **Project Structure**
```
ecommerce_project/
│
├── app/
│   ├── __init__.py
│   ├── main.py              # Entry point for FastAPI
│   ├── database.py          # SQLite connection and setup
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic models for validation
│   ├── crud.py              # CRUD operations
│   ├── ai.py                # AI integration
│   └── routers/             # API routes
│       ├── __init__.py
│       ├── products.py      # Product-related endpoints
│       └── recommendations.py  # Recommendation-related endpoints
│
├── data/                    # Sample data JSON files
│   ├── products.json
│   ├── feedback.json
│   └── campaigns.json
│
├── setup.sql                # SQL script to create tables
├── requirements.txt         # Project dependencies
├── README.md                # Documentation
└── app/seeder.py            # Seeder script to populate the database
```

---

## **Usage Example**

- **Retrieve Products:**
  ```bash
  curl -X GET http://localhost:8000/api/products
  ```

- **Get Recommendations for a Customer:**
  ```bash
  curl -X GET http://localhost:8000/api/recommendations/101
  ```

---

## **Acknowledgments**
- **OpenAI API** for generating personalized recommendations.
- **FastAPI** for providing an easy-to-use backend framework.
