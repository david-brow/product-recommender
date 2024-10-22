CREATE TABLE product_catalog (
    product_id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price REAL
);

CREATE TABLE customer_feedback (
    feedback_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    customer_id INTEGER,
    rating INTEGER,
    review TEXT,
    FOREIGN KEY (product_id) REFERENCES product_catalog(product_id)
);

CREATE TABLE marketing_campaign (
    campaign_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    campaign_name TEXT,
    discount REAL,
    start_date TEXT,
    end_date TEXT,
    FOREIGN KEY (product_id) REFERENCES product_catalog(product_id)
);
