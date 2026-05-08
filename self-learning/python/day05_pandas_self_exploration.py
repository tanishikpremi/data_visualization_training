# self learning - exploring pandas more on my own
# using a made-up ecommerce dataset to practice
# trying things i haven't done in class yet

import pandas as pd
import numpy as np

# making my own dataset to practice on
np.random.seed(42)

data = {
    "order_id":   range(1001, 1051),
    "customer":   np.random.choice(["Anita","Raj","Priya","Dev","Meena"], 50),
    "product":    np.random.choice(["Laptop","Phone","Tablet","Earbuds","Charger"], 50),
    "category":   np.random.choice(["Electronics","Accessories"], 50),
    "quantity":   np.random.randint(1, 6, 50),
    "price":      np.random.choice([999, 1499, 2999, 499, 149], 50),
    "city":       np.random.choice(["Mumbai","Delhi","Bangalore","Pune","Hyderabad"], 50),
    "order_date": pd.date_range("2024-01-01", periods=50, freq="W")
}

df = pd.DataFrame(data)
df["total_amount"] = df["quantity"] * df["price"]

print("Shape:", df.shape)
print(df.head())

# ── trying groupby chains ──────────────────────
# found this pattern in a tutorial - really useful

city_sales = (
    df.groupby("city")["total_amount"]
    .agg(["sum","mean","count"])
    .round(2)
    .rename(columns={"sum":"total","mean":"avg_order","count":"orders"})
    .sort_values("total", ascending=False)
)
print("\nCity Sales:\n", city_sales)

# ── pivot table - practicing this more ────────

pivot = df.pivot_table(
    values="total_amount",
    index="category",
    columns="city",
    aggfunc="sum",
    fill_value=0
)
print("\nPivot Table:\n", pivot)

# ── resample by month - didn't know this existed ──

df.set_index("order_date", inplace=True)
monthly = df["total_amount"].resample("ME").sum()
print("\nMonthly Revenue:\n", monthly)

# ── string operations on a column ─────────────

df.reset_index(inplace=True)
df["customer_upper"] = df["customer"].str.upper()
df["product_short"]  = df["product"].str[:3]   # first 3 chars
print("\nString ops:\n", df[["customer","customer_upper","product","product_short"]].head())

# ── applying custom logic with apply ──────────

def order_size(qty):
    if qty >= 4:
        return "Large"
    elif qty >= 2:
        return "Medium"
    return "Small"

df["order_size"] = df["quantity"].apply(order_size)
print("\nOrder Sizes:\n", df["order_size"].value_counts())

# ── exporting to CSV ───────────────────────────
# good habit to save cleaned/processed data

df.to_csv("ecommerce_practice.csv", index=False)
print("\nSaved to ecommerce_practice.csv")

# NOTE TO SELF: look into pd.cut() for binning
# and pd.get_dummies() for encoding
