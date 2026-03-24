-- =========================
-- DIMENSION TABLES
-- =========================

-- 📦 DIM PRODUCT
CREATE TABLE IF NOT EXISTS dim_product (
    product_id INT PRIMARY KEY,
    title TEXT,
    category TEXT,
    final_price FLOAT,
    rating FLOAT
);

-- 👤 DIM SELLER
CREATE TABLE IF NOT EXISTS dim_seller (
    seller_id SERIAL PRIMARY KEY,
    seller_name TEXT,
    seller_information TEXT
);

-- 📅 DIM DATE
CREATE TABLE IF NOT EXISTS dim_date (
    date_id SERIAL PRIMARY KEY,
    full_date DATE,
    year INT,
    month INT,
    day INT
);

-- 🏷️ DIM CATEGORY
CREATE TABLE IF NOT EXISTS dim_category (
    category_id SERIAL PRIMARY KEY,
    category TEXT
);

-- =========================
-- FACT TABLE
-- =========================

-- 📊 FACT SALES
CREATE TABLE IF NOT EXISTS fact_sales (
    id SERIAL PRIMARY KEY,
    product_id INT,
    seller_id INT,
    date_id INT,
    quantity INT,
    sales FLOAT,

    FOREIGN KEY (product_id) REFERENCES dim_product(product_id),
    FOREIGN KEY (seller_id) REFERENCES dim_seller(seller_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);
