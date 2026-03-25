import pandas as pd
import numpy as np
import psycopg2
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# Charger variables .env
load_dotenv()

# -----------------------------
# 📂 LOAD DATA
# -----------------------------
def load_data():
    df = pd.read_csv("data/raw/ecommerce_dataset.csv")
    return df


# -----------------------------
# 🔄 TRANSFORMATION
# -----------------------------
def transform_data(df):
    # Nettoyage basique
    df = df.drop_duplicates()

    # Simulation de ventes 🔥
    df['quantity'] = np.random.randint(1, 5, size=len(df))
    df['order_date'] = pd.date_range(start="2023-01-01", periods=len(df))
    df['sales'] = df['final_price'] * df['quantity']

    return df


# -----------------------------
# 🗄️ CONNECTION DB
# -----------------------------
def get_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )
    return conn


# -----------------------------
# 📦 LOAD DIMENSIONS
# -----------------------------
def load_dimensions(conn, df):
    cur = conn.cursor()

    # 🔹 DIM PRODUCT
    dim_product = df[['product_id', 'title', 'category', 'final_price', 'rating']].drop_duplicates()

    for _, row in dim_product.iterrows():
        cur.execute("""
            INSERT INTO dim_product (product_id, title, category, final_price, rating)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (product_id) DO NOTHING
        """, (
            row['product_id'],
            row['title'],
            row['category'],
            row['final_price'],
            row['rating']
        ))

    # 🔹 DIM SELLER
    dim_seller = df[['seller_name', 'seller_information']].drop_duplicates()

    for _, row in dim_seller.iterrows():
        cur.execute("""
            INSERT INTO dim_seller (seller_name, seller_information)
            VALUES (%s, %s)
        """, (
            row['seller_name'],
            row['seller_information']
        ))

    # 🔹 DIM DATE
    dim_date = df[['order_date']].drop_duplicates()

    for _, row in dim_date.iterrows():
        cur.execute("""
            INSERT INTO dim_date (full_date, year, month, day)
            VALUES (%s, %s, %s, %s)
        """, (
            row['order_date'],
            row['order_date'].year,
            row['order_date'].month,
            row['order_date'].day
        ))

    conn.commit()
    cur.close()


# -----------------------------
# 📊 LOAD FACT TABLE
# -----------------------------
def load_fact_table(conn, df):
    cur = conn.cursor()

    for _, row in df.iterrows():

        # récupérer seller_id
        cur.execute("""
            SELECT seller_id FROM dim_seller
            WHERE seller_name = %s
            LIMIT 1
        """, (row['seller_name'],))
        seller_id = cur.fetchone()[0]

        # récupérer date_id
        cur.execute("""
            SELECT date_id FROM dim_date
            WHERE full_date = %s
            LIMIT 1
        """, (row['order_date'],))
        date_id = cur.fetchone()[0]

        # insertion fact
        cur.execute("""
            INSERT INTO fact_sales (product_id, seller_id, date_id, quantity, sales)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            row['product_id'],
            seller_id,
            date_id,
            row['quantity'],
            row['sales']
        ))

    conn.commit()
    cur.close()


# -----------------------------
# 🚀 MAIN
# -----------------------------
def main():
    print("🚀 Début du pipeline Data Warehouse...")

    df = load_data()
    df = transform_data(df)

    conn = get_connection()

    print("📦 Loading dimensions...")
    load_dimensions(conn, df)

    print("📊 Loading fact table...")
    load_fact_table(conn, df)

    conn.close()

    print("🎉 Data Warehouse rempli avec succès !")


if __name__ == "__main__":
    main()
