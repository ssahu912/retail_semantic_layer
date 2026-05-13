# Burger Haven QSR Dataset - Final Summary

## 📦 DATASET PACKAGE CONTENTS

### CSV Data Files (8 files)
1. **stores.csv** - 5 store locations in Riyadh
2. **sales_transactions.csv** - 450 daily aggregated sales records
3. **detailed_transactions.csv** - 8,000 individual transaction records
4. **inventory.csv** - 1,125 inventory snapshot records
5. **promotions.csv** - 12 promotional campaigns
6. **weather.csv** - 90 days of weather data
7. **poi.csv** - 36 points of interest
8. **competitor_pricing.csv** - 360 competitor pricing records

### Documentation Files (4 files)
1. **README.md** - Complete dataset documentation
2. **business_rules_operations.md** - QSR operational constraints and rules

---

## 📊 DATASET STATISTICS

**Total Records**: 10,078 (excluding headers)  
**Time Period**: October 1 - December 29, 2024 (90 days)  
**Location**: Riyadh, Saudi Arabia  
**Business Type**: Quick Service Restaurant Chain


## 📋 BUSINESS CONSTRAINTS (SUMMARY)

### Operational Hours
- Standard: 08:00 - 23:30 (Sun-Thu)
- Weekend: 08:00 - 00:30 (Fri-Sat)
- Ramadan: Special evening hours

### Service SLAs
- Dine-in: 12 minutes max
- Drive-thru: 5 minutes max
- Delivery: 35 minutes max

### Inventory Rules
- Reorder at 25% capacity
- 3 days safety stock
- <3% waste target

### Pricing Strategy
- 10-15% premium vs local chains
- Match/undercut global chains on value items
- Quarterly price reviews

### Financial Targets
- Daily revenue targets by store (10.5K - 15.5K SAR)
- 95% of monthly budget minimum
- 18% gross margin minimum

---

## 🔍 DATA RELATIONSHIPS

```
stores (5) ─┬─→ sales_transactions (450)
            ├─→ detailed_transactions (8,000)
            ├─→ inventory (1,125)
            └─→ poi (36)

weather (90) ──→ sales_transactions (450)
                 detailed_transactions (8,000)

promotions (12) ──→ sales_transactions (450)

competitor_pricing (360) [reference]
```
