# Burger Haven QSR Dataset - README

## Overview
This is a comprehensive, synergetic dataset for a Quick Service Restaurant (QSR) chain called **Burger Haven** operating in Riyadh, Saudi Arabia. The dataset contains ~10,000 records across multiple dimensions designed for retail analytics, demand forecasting, inventory optimization, and business intelligence use cases.

**Time Period**: October 1, 2024 - December 29, 2024 (90 days)  
**Stores**: 5 locations across Riyadh  
**Total Records**: ~10,062 records

---

## Dataset Files

### 1. **stores.csv** (5 records)
Master data for all store locations.

**Columns**:
- `store_id`: Unique store identifier (S001-S005)
- `store_name`: Store name with location
- `location_name`: District/Mall name
- `latitude`, `longitude`: GPS coordinates
- `opening_date`: Store opening date
- `store_size_sqm`: Store area in square meters
- `seating_capacity`: Number of seats
- `drive_thru`: Boolean for drive-thru availability
- `delivery_enabled`: Boolean for delivery service
- `staff_count`: Average staff count
- `rent_sar_monthly`: Monthly rent in Saudi Riyals
- `district`: Riyadh district
- `store_type`: Store classification

**Use Cases**: Store performance analysis, location analytics, capacity planning

---

### 2. **sales_transactions.csv** (450 records)
Daily aggregated sales data for each store.

**Columns**:
- `transaction_id`: Unique transaction group ID
- `store_id`: Foreign key to stores
- `date`: Transaction date (YYYY-MM-DD)
- `day_of_week`: Day name
- `num_transactions`: Count of transactions
- `total_revenue_sar`: Total revenue in SAR
- `avg_ticket_sar`: Average transaction value
- `burgers_sold`, `sides_sold`, `drinks_sold`, `desserts_sold`: Item counts
- `lunch_peak_pct`, `dinner_peak_pct`, `other_hours_pct`: Peak hour distribution
- `delivery_orders`: Count of delivery orders
- `drive_thru_orders`: Count of drive-thru orders

**Key Relationships**: 
- Links to `stores.csv` via `store_id`
- Links to `weather.csv` via `date`
- Links to `promotions.csv` via `date` and `store_id`

**Use Cases**: Revenue analysis, demand forecasting, peak hour optimization

---

### 3. **detailed_transactions.csv** (8,000 records)
Transaction-level data with individual order details.

**Columns**:
- `transaction_id`: Unique transaction ID
- `store_id`: Foreign key to stores
- `date`: Transaction date
- `transaction_time`: Time of transaction (HH:MM)
- `day_of_week`: Day name
- `num_items`: Items in order
- `subtotal_sar`, `discount_sar`, `tax_sar`, `total_sar`: Pricing breakdown
- `payment_method`: Payment type (CASH, CREDIT_CARD, etc.)
- `order_channel`: Order type (DINE_IN, DRIVE_THRU, DELIVERY, TAKEAWAY)
- `customer_satisfaction`: Rating 1-5
- `wait_time_mins`: Service time in minutes

**Key Relationships**:
- Links to `stores.csv` via `store_id`
- Links to `weather.csv` via `date`
- Can be aggregated to match `sales_transactions.csv`

**Use Cases**: Customer behavior analysis, service time optimization, payment preference analysis

---

### 4. **inventory.csv** (1,125 records)
Stock levels for products across stores at various time points.

**Columns**:
- `inventory_id`: Unique inventory record ID
- `store_id`: Foreign key to stores
- `product_id`: Product identifier
- `product_name`: Product name
- `category`: Product category (RAW_MATERIAL, PACKAGING, CONDIMENTS)
- `date`: Inventory snapshot date
- `current_stock`: Current stock level
- `unit`: Unit of measurement
- `reorder_point`: Reorder threshold
- `max_capacity`: Maximum storage capacity
- `days_on_hand`: Days of supply
- `stock_status`: Status (NORMAL, LOW, OVERSTOCK)
- `unit_cost_sar`: Cost per unit

**Key Relationships**:
- Links to `stores.csv` via `store_id`
- Indirectly links to sales data (stock consumption drives sales)

**Use Cases**: Inventory optimization, reorder point analysis, waste reduction, cost analysis

---

### 5. **promotions.csv** (12 records)
Promotional campaigns and their parameters.

**Columns**:
- `promo_id`: Unique promotion identifier
- `promo_name`: Promotion name
- `promo_type`: Type (BUNDLE, DISCOUNT, BOGO, FREEBIE)
- `start_date`, `end_date`: Promotion period
- `applicable_stores`: Store IDs (comma-separated or 'ALL')
- `applicable_days`: Days of week (comma-separated)
- `min_order_value_sar`: Minimum order requirement
- `description`: Promotion details
- `bundle_price_sar`: Bundle price (if applicable)
- `regular_price_sar`: Regular price for comparison
- `discount_pct`: Discount percentage

**Key Relationships**:
- Links to `stores.csv` via `applicable_stores`
- Links to sales data via date range overlap

**Use Cases**: Promotion effectiveness analysis, price elasticity studies, revenue lift measurement

---

### 6. **weather.csv** (90 records)
Daily weather conditions for Riyadh.

**Columns**:
- `weather_id`: Unique weather record ID
- `date`: Date (YYYY-MM-DD)
- `city`: Riyadh
- `temp_high_c`, `temp_low_c`: Temperature range in Celsius
- `humidity_pct`: Humidity percentage
- `rainfall_mm`: Rainfall in millimeters
- `wind_speed_kmh`: Wind speed
- `cloud_cover`: Cloud conditions
- `conditions`: Overall weather description
- `visibility_km`: Visibility range
- `uv_index`: UV index

**Key Relationships**:
- Links to all transaction data via `date`

**Use Cases**: Weather impact on sales, demand forecasting with weather features, seasonal analysis

---

### 7. **poi.csv** (36 records)
Points of Interest near store locations.

**Columns**:
- `poi_id`: Unique POI identifier
- `nearest_store_id`: Foreign key to stores
- `poi_name`: POI name
- `poi_type`: Type (MALL, OFFICE, RESIDENTIAL, HOSPITAL, SCHOOL, RECREATION, etc.)
- `latitude`, `longitude`: GPS coordinates
- `distance_km`: Distance from store
- `avg_daily_footfall`: Average daily visitors
- `description`: POI description

**Key Relationships**:
- Links to `stores.csv` via `nearest_store_id`

**Use Cases**: Location analysis, catchment area profiling, site selection for new stores, marketing targeting

---

### 8. **competitor_pricing.csv** (360 records)
Competitor pricing data over time.

**Columns**:
- `pricing_id`: Unique pricing record ID
- `competitor_id`: Competitor identifier
- `competitor_name`: Competitor name
- `product_name`: Product/menu item name
- `category`: Product category
- `date`: Pricing date
- `regular_price_sar`: Regular price
- `promo_price_sar`: Promotional price (if on promo)
- `on_promotion`: YES/NO indicator
- `competitor_type`: Global Chain or Local Chain

**Key Relationships**:
- Can be compared against your own pricing (implied in business rules)
- Time-series data for pricing trends

**Use Cases**: Competitive pricing analysis, price positioning strategy, market share estimation

---

## Data Relationships & Keys

### Primary Relationships
```
stores.csv (store_id)
    ├── sales_transactions.csv (store_id)
    ├── detailed_transactions.csv (store_id)
    ├── inventory.csv (store_id)
    ├── poi.csv (nearest_store_id)
    └── promotions.csv (applicable_stores)

weather.csv (date)
    ├── sales_transactions.csv (date)
    └── detailed_transactions.csv (date)

promotions.csv (date range + store_id)
    └── sales_transactions.csv (date + store_id)
```

### Derived Metrics Examples
You can create powerful insights by joining these datasets:

**Example 1**: Sales vs Weather Impact
```sql
SELECT 
    s.date,
    s.store_id,
    s.total_revenue_sar,
    w.temp_high_c,
    w.conditions,
    w.rainfall_mm
FROM sales_transactions s
JOIN weather w ON s.date = w.date
WHERE w.rainfall_mm > 0;
```

**Example 2**: Promotion Effectiveness
```sql
SELECT 
    p.promo_name,
    AVG(s.total_revenue_sar) as avg_daily_revenue,
    AVG(s.num_transactions) as avg_transactions
FROM sales_transactions s
JOIN promotions p ON s.date BETWEEN p.start_date AND p.end_date
    AND (p.applicable_stores = 'ALL' OR s.store_id IN p.applicable_stores)
GROUP BY p.promo_name;
```

**Example 3**: Inventory Turnover by Store
```sql
SELECT 
    st.store_name,
    i.product_name,
    AVG(i.current_stock) as avg_stock,
    AVG(i.days_on_hand) as avg_days_on_hand
FROM inventory i
JOIN stores st ON i.store_id = st.store_id
GROUP BY st.store_name, i.product_name;
```

---

## Business Context

### Store Profiles

**S001 - Burger Haven Olaya** (Urban Premium)
- High-traffic business district
- Strong lunch rush from nearby offices
- Premium pricing tolerance
- Delivery-heavy

**S002 - Burger Haven Al Malqa** (Mall Location)
- Highest footfall due to mall location
- Family-oriented weekends
- Consistent performance
- Dine-in focused

**S003 - Burger Haven King Fahd** (Urban Standard)
- Standard urban location
- Mixed customer base
- No drive-thru
- Balanced channels

**S004 - Burger Haven Granada** (Shopping Center)
- Shopping center location
- Strong weekend performance
- Family meals popular
- Good drive-thru uptake

**S005 - Burger Haven Riyadh Park** (Mall Premium)
- Premium mall location
- Highest revenue potential
- Affluent customer base
- Strong dine-in business

### Saudi-Specific Considerations

1. **Weekend**: Friday-Saturday (not Saturday-Sunday)
2. **Currency**: Saudi Riyal (SAR)
3. **VAT**: 15% on all sales
4. **Prayer Times**: May impact service during 5 daily prayers
5. **Ramadan**: Dramatically different operating pattern (evening/night focus)
6. **National Day**: September 23 (major sales day)
7. **Summer Season**: Very hot (40°C+), indoor dining preference

---

## Technical Notes

### File Format
- All files in CSV format with UTF-8 encoding
- Comma-separated values
- Headers in first row
- No special characters in delimiters

### Date/Time Formats
- Dates: YYYY-MM-DD
- Times: HH:MM (24-hour format)
- Datetimes: YYYY-MM-DD HH:MM:SS

### Numeric Formats
- Currency: Always 2 decimal places
- Percentages: Decimal format (0.25 = 25%)
- Coordinates: 4 decimal places

### Missing Data Handling
- Empty fields: Indicated by empty string ""
- Not applicable: "N/A"
- Zero values: Explicit 0 or 0.00

---

## Dataset Statistics

### Record Counts
- **Total Records**: 10,062
- Stores: 5
- Sales Transactions: 450
- Detailed Transactions: 8,000
- Inventory: 1,125
- Promotions: 12
- Weather: 90
- POI: 36
- Competitor Pricing: 360

### Time Coverage
- Start Date: 2024-10-01
- End Date: 2024-12-29
- Duration: 90 days
- Frequency: Daily for most datasets

### Geographic Coverage
- City: Riyadh, Saudi Arabia
- Districts: Olaya, Al Malqa, Al Sahafa, Granada, Hittin
- Coordinate Range: 
  - Latitude: 24.68 to 24.79
  - Longitude: 46.61 to 46.74

---

## Citation & Usage

This dataset is designed for educational and interview purposes. When using this dataset:

1. **Attribution**: Burger Haven Dataset v1.0
3. **Restrictions**: Not for commercial use
4. **Data Privacy**: All data is synthetic and does not represent real individuals or transactions

---