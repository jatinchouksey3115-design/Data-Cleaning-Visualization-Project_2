import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

RAW_FILE = "data/raw_sales_data.csv"
CLEAN_FILE = "data/cleaned_sales_data.csv"

df = pd.read_csv(RAW_FILE)

# 1. Remove duplicates
df = df.drop_duplicates().copy()

# 2. Standardize text
df["Product"] = df["Product"].replace({"smart phone": "Smartphone", "Smart Phone": "Smartphone"})
df["Category"] = df["Category"].astype("string").str.strip().str.title()
df["Region"] = df["Region"].astype("string").str.strip().str.title()
df["Product"] = df["Product"].astype("string").str.strip()

# 3. Convert data types
for col in ["Quantity", "Unit_Price", "Discount", "Total_Amount"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

# 4. Handle invalid values
df.loc[df["Quantity"] <= 0, "Quantity"] = np.nan
df.loc[df["Unit_Price"] <= 0, "Unit_Price"] = np.nan
df.loc[(df["Discount"] < 0) | (df["Discount"] > 1), "Discount"] = np.nan
df.loc[df["Total_Amount"] < 0, "Total_Amount"] = np.nan

# 5. Fill missing values
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median()).round().astype(int)
df["Unit_Price"] = df["Unit_Price"].fillna(df["Unit_Price"].median())
df["Discount"] = df["Discount"].fillna(df["Discount"].median())
df["Region"] = df["Region"].fillna(df["Region"].mode()[0])
df["Product"] = df["Product"].fillna(df["Product"].mode()[0])
df["Category"] = df["Category"].fillna(df["Category"].mode()[0])
df["Order_Date"] = df["Order_Date"].fillna(df["Order_Date"].median())

# 6. Recalculate sales
df["Total_Amount"] = df["Quantity"] * df["Unit_Price"] * (1 - df["Discount"])

# 7. IQR outlier capping
for col in ["Quantity", "Unit_Price", "Total_Amount"]:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    df[col] = df[col].clip(lower, upper)

df["Quantity"] = df["Quantity"].round().astype(int)
df["Total_Amount"] = (df["Quantity"] * df["Unit_Price"] * (1 - df["Discount"])).round(2)

df.to_csv(CLEAN_FILE, index=False)

# 8. Visualizations
plt.figure()
df.groupby("Product")["Total_Amount"].sum().sort_values(ascending=False).plot(kind="bar")
plt.title("Total Sales by Product")
plt.tight_layout()
plt.savefig("outputs/sales_by_product.png", dpi=160)
plt.close()

plt.figure()
df.groupby("Region")["Total_Amount"].sum().sort_values(ascending=False).plot(kind="bar")
plt.title("Total Sales by Region")
plt.tight_layout()
plt.savefig("outputs/sales_by_region.png", dpi=160)
plt.close()

plt.figure()
df.set_index("Order_Date").resample("ME")["Total_Amount"].sum().plot(marker="o")
plt.title("Monthly Sales Trend")
plt.tight_layout()
plt.savefig("outputs/monthly_sales_trend.png", dpi=160)
plt.close()

plt.figure()
plt.hist(df["Quantity"], bins=10)
plt.title("Distribution of Order Quantity")
plt.tight_layout()
plt.savefig("outputs/quantity_distribution.png", dpi=160)
plt.close()

plt.figure()
df.groupby("Category")["Total_Amount"].sum().sort_values(ascending=False).plot(kind="bar")
plt.title("Total Sales by Category")
plt.tight_layout()
plt.savefig("outputs/sales_by_category.png", dpi=160)
plt.close()

print("Cleaning and visualization completed successfully.")
