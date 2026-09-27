# Data Cleaning & Visualization Project

## Objective
Clean a raw retail-sales dataset, handle missing values, duplicates, inconsistent data, invalid values and outliers, then visualize the cleaned data to extract useful insights.

## Dataset
- Records before cleaning: 265
- Records after removing duplicates: 260
- Final cleaned records: 260
- Duplicate rows removed: 5
- Missing cells in raw data: 6
- Missing cells after cleaning: 0

## Cleaning Steps
1. Removed duplicate rows.
2. Standardized text values such as region/category names.
3. Corrected inconsistent product naming.
4. Converted dates and numeric columns to appropriate data types.
5. Replaced invalid quantities, prices, discounts and negative sales values.
6. Filled missing numeric values using median-based imputation and missing categorical values using the mode.
7. Recalculated Total_Amount using Quantity × Unit_Price × (1 − Discount).
8. Detected extreme values using the IQR method and capped outliers.
9. Saved the cleaned dataset for analysis.

## Visualizations
The project includes:
- Total sales by product
- Total sales by region
- Monthly sales trend
- Quantity distribution
- Total sales by category

## Key Findings
- The product with the highest total sales can be identified from `sales_by_product.png`.
- Regional sales differences are shown in `sales_by_region.png`.
- Monthly movement is shown in `monthly_sales_trend.png`.
- Order-size distribution is shown in `quantity_distribution.png`.
- Electronics vs. Accessories performance is shown in `sales_by_category.png`.

## Tools Used
- Python
- Pandas
- NumPy
- Matplotlib

## Files
- `data/raw_sales_data.csv` — intentionally messy source dataset
- `data/cleaned_sales_data.csv` — cleaned dataset
- `data_cleaning_visualization.py` — complete cleaning and visualization script
- `outputs/` — generated charts
- `README.md` — project documentation
- `requirements.txt` — Python dependencies
