# ecommerce-data-warehouse

Ce projet implémente une architecture Data Warehouse complète pour des données e-commerce.

- ETL pipeline built with Python
- Star schema data modeling
- Data marts for analytics
- PostgreSQL as storage
- Streamlit dashboard for visualization


## 🚀 🧭 LANCER LE PROJET DE A → Z

### 🧱 🟢 0. PRÉREQUIS

Tu dois avoir :
- PostgreSQL installé ✅
- Python + venv ✅
- Projet structuré ✅

### 🧱 🟢 1. Activer ton environnement
```bash
cd ecommerce-data-warehouse
source .venv/bin/activate
```

### 🧱 🟢 2. Installer dépendances
```bash
pip install -r requirements.txt
```

### 🧱 🟢 3. Configurer .env

Exemple de .env :
```
DB_HOST=localhost
DB_NAME=ecommerce-db
DB_USER=data_analyst
DB_PASSWORD=motdepasse
DB_PORT=5432
```

### 🧱 🟢 4. Créer la base PostgreSQL
```bash
sudo -u postgres psql
```
Puis dans psql :
```
CREATE DATABASE "ecommerce-db";
CREATE USER data_analyst WITH PASSWORD 'motdepasse';
GRANT ALL PRIVILEGES ON DATABASE "ecommerce-db" TO data_analyst;
```

### 🧱 🟢 5. Créer les tables (Data Warehouse)
```bash
psql -U data_analyst -d ecommerce-db -h localhost -f sql/create_tables.sql
```

### 🧱 🟢 6. Charger les données (ETL)
```bash
python3 scripts/transform_and_load.py
```
Cela remplit : dim_product, dim_seller, dim_date, fact_sales

### 🧱 🟢 7. Créer les Data Marts
```bash
psql -U data_analyst -d ecommerce-db -h localhost -f sql/create_data_marts.sql
```
Cela crée : product_mart, seller_mart, category_mart, time_mart

### 🧱 🟢 8. Vérifier les données
```bash
psql -U data_analyst -d ecommerce-db -h localhost
```
Puis :
```
SELECT * FROM product_mart LIMIT 10;
SELECT * FROM seller_mart LIMIT 10;
SELECT * FROM category_mart;
SELECT * FROM time_mart;
```

### 🧱 🟢 9. (OPTIONNEL) Dashboard Streamlit
```bash
streamlit run app/dashboard.py
```
Ouvre : http://localhost:8501

---

💥 🔁 PIPELINE COMPLET
CSV → Python ETL → PostgreSQL (Data Warehouse)
	→ Data Marts → Dashboard

---

## Résumé ultra simple

Pour lancer ton projet :
1. psql → créer DB
2. create_tables.sql
3. python transform_and_load.py
4. create_data_marts.sql
5. (optionnel) streamlit

---

## How to run the project (EN)
1. Set up PostgreSQL database
2. Run SQL scripts to create tables
3. Execute ETL pipeline
4. Generate data marts
5. Launch dashboard


Structure du projet :

```
ecommerce-data-warehouse/
│
├── data/
│   ├── raw/
│   │   └── ecommerce_dataset.csv
│   ├── processed/
│
├── scripts/
│   └── transform_and_load.py
│
├── sql/
│   ├── create_tables.sql
│   ├── create_data_marts.sql
│   ├── queries.sql
│
├── notebooks/
│   └── exploration.ipynb
│
├── app/
│   └── dashboard.py   # (Streamlit)
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Pipeline

CSV → Cleaning → Transformation → PostgreSQL → Data Warehouse → Data Marts → Dashboard

## Star Schema

- **Fact Table**: fact_sales (product_id, date_id, quantity, sales)
- **Dimensions**: dim_product, dim_seller, dim_date, dim_category

## Data Marts

1. Product Performance Mart
2. Seller Performance Mart
3. Category Analysis Mart

---

This structure is scalable, analytics-ready, and BI friendly.
