# ecommerce-data-warehouse


**Recommandation : utilisez un environnement virtuel Python pour isoler les dépendances.**

```bash
# Création et activation d'un environnement virtuel (Linux/Mac)
python3 -m venv .venv
source .venv/bin/activate

# Installation des dépendances
pip install -r requirements.txt
```

Ce projet implémente une architecture Data Warehouse complète pour des données e-commerce.

- ETL pipeline built with Python
- Star schema data modeling
- Data marts for analytics
- PostgreSQL as storage
- Streamlit dashboard for visualization


## Project Structure

Avant toute chose, créez et activez un environnement virtuel Python, puis installez les dépendances :

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

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
│   ├── data_cleaning.py
│   ├── transform_data.py
│   ├── load_data.py
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
