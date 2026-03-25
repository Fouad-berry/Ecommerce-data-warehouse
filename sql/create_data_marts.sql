
-- =========================
-- 1. PRODUCT PERFORMANCE MART
-- =========================
CREATE TABLE IF NOT EXISTS product_mart AS
SELECT 
	p.product_id,
	p.title,
	p.category,
	AVG(p.rating) AS avg_rating,
	AVG(p.final_price) AS avg_price,
	SUM(f.quantity) AS total_quantity,
	SUM(f.sales) AS total_sales
FROM fact_sales f
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.product_id, p.title, p.category;

-- =========================
-- 2. SELLER PERFORMANCE MART
-- =========================
CREATE TABLE IF NOT EXISTS seller_mart AS
SELECT 
	s.seller_id,
	s.seller_name,
	COUNT(f.id) AS total_orders,
	SUM(f.sales) AS total_sales,
	AVG(f.sales) AS avg_order_value
FROM fact_sales f
JOIN dim_seller s ON f.seller_id = s.seller_id
GROUP BY s.seller_id, s.seller_name;

-- =========================
-- 3. CATEGORY ANALYSIS MART
-- =========================
CREATE TABLE IF NOT EXISTS category_mart AS
SELECT 
	p.category,
	COUNT(DISTINCT p.product_id) AS total_products,
	SUM(f.sales) AS total_sales,
	AVG(p.rating) AS avg_rating,
	AVG(p.final_price) AS avg_price
FROM fact_sales f
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.category;

-- =========================
-- 4. TIME ANALYSIS MART
-- =========================
CREATE TABLE IF NOT EXISTS time_mart AS
SELECT 
	d.year,
	d.month,
	COUNT(f.id) AS total_orders,
	SUM(f.sales) AS total_sales,
	SUM(f.quantity) AS total_quantity
FROM fact_sales f
JOIN dim_date d ON f.date_id = d.date_id
GROUP BY d.year, d.month
ORDER BY d.year, d.month;
