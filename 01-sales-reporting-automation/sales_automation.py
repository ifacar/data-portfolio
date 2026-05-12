import pandas as pd
import os
from pathlib import Path

# ============================================
# SALES REPORTING AUTOMATION SCRIPT
# ============================================
# Bu script 3 aylık satış verilerini birleştirip
# KPI'lar hesaplıyor.

# 1. Veri Yükleme (Loading)
print("=" * 60)
print("SALES REPORTING AUTOMATION")
print("=" * 60)
print("\n📂 Loading CSV files...")

# sample_data klasöründeki tüm CSV'leri bul
data_folder = "sample_data"
csv_files = sorted([f for f in os.listdir(data_folder) if f.endswith('.csv')])

print(f"✓ Found {len(csv_files)} files: {csv_files}")

# 2. Her CSV'yi oku ve liste'ye koy
dataframes = []
for csv_file in csv_files:
    file_path = os.path.join(data_folder, csv_file)
    df = pd.read_csv(file_path)
    dataframes.append(df)
    print(f"  ✓ Loaded: {csv_file} ({len(df)} rows)")

# 3. Tüm DataFrame'leri birleştir (Concatenate)
print("\n🔗 Merging files...")
combined_df = pd.concat(dataframes, ignore_index=True)
print(f"✓ Total rows after merge: {len(combined_df)}")

# 4. Tarih sütununu datetime'a çevir
combined_df['date'] = pd.to_datetime(combined_df['date'])
combined_df['month'] = combined_df['date'].dt.to_period('M')

# 5. KPI'lar Hesapla
print("\n📊 Calculating KPIs...\n")

# --------- KPI 1: Aylık Toplam Satış (Revenue) ---------
monthly_revenue = combined_df.groupby('month').apply(
    lambda x: (x['quantity_sold'] * x['unit_price']).sum()
).round(2)

print("📈 MONTHLY REVENUE:")
print(monthly_revenue)

# --------- KPI 2: Month-over-Month (MoM) Growth ---------
mom_growth = monthly_revenue.pct_change() * 100

print("\n📊 MONTH-OVER-MONTH GROWTH (%):")
for month, growth in mom_growth.items():
    if pd.notna(growth):
        direction = "📈" if growth > 0 else "📉"
        print(f"  {month}: {direction} {growth:.2f}%")

# --------- KPI 3: Kategori Başına Satış ---------
print("\n🏆 REVENUE BY CATEGORY:")
category_revenue = combined_df.groupby('category').apply(
    lambda x: (x['quantity_sold'] * x['unit_price']).sum()
).round(2).sort_values(ascending=False)

for category, revenue in category_revenue.items():
    print(f"  {category}: ${revenue:,.2f}")

# --------- KPI 4: Top 5 Ürün ---------
print("\n⭐ TOP 5 PRODUCTS BY REVENUE:")
product_revenue = combined_df.groupby('product_name').apply(
    lambda x: (x['quantity_sold'] * x['unit_price']).sum()
).round(2).sort_values(ascending=False).head(5)

for i, (product, revenue) in enumerate(product_revenue.items(), 1):
    print(f"  {i}. {product}: ${revenue:,.2f}")

# --------- KPI 5: Toplam İstatistikler ---------
print("\n📋 OVERALL STATISTICS:")
total_revenue = (combined_df['quantity_sold'] * combined_df['unit_price']).sum()
total_quantity = combined_df['quantity_sold'].sum()
avg_order_value = total_revenue / len(combined_df)

print(f"  Total Revenue: ${total_revenue:,.2f}")
print(f"  Total Units Sold: {total_quantity:,.0f}")
print(f"  Average Order Value: ${avg_order_value:,.2f}")

# 6. Raporu CSV'ye Kaydet
print("\n💾 Saving report...\n")

# Summary DataFrame oluştur
summary_data = {
    'Month': monthly_revenue.index.astype(str),
    'Revenue': monthly_revenue.values,
    'MoM_Growth_%': mom_growth.values
}
summary_df = pd.DataFrame(summary_data)

# CSV'ye yaz
output_file = "sales_report.csv"
summary_df.to_csv(output_file, index=False)
print(f"✓ Report saved: {output_file}")

# Ayrıca Excel'e de kaydet (bonus)
excel_file = "sales_report.xlsx"
with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
    summary_df.to_excel(writer, sheet_name='Monthly Summary', index=False)
    category_revenue.to_excel(writer, sheet_name='By Category')
    product_revenue.to_excel(writer, sheet_name='Top Products')

print(f"✓ Report also saved: {excel_file}")

print("\n" + "=" * 60)
print("✅ AUTOMATION COMPLETE!")
print("=" * 60)