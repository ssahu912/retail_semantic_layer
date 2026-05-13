# Materialized Graph — QSR Knowledge Graph 📚🔧

## Overview

This folder contains *materialized* Knowledge Graph (KG) files derived from the QSR (Quick Service Restaurant) ontology for the Burger Haven dataset. Each Turtle (`.ttl`) file is a snapshot of entities, relationships and aggregated events (sales, transactions, promotions, weather, stores, etc.). The graphs use the base namespace `http://example.org/qsr_kg#` and ontology modules such as:

- `QSREventsOntology#` (events)
- `QSRTimeOntology#` (time / business days)
- `QSRLocationOntology#` (locations, POIs)
- `QSRPromotionsOntology#` (promotions)
- `QSRInventoryOntology#`, `QSRPerformanceOntology#`, `QSRCoreOntology#`, etc.

---

## Files

### ✅ `BurgerHavenKG.ttl`
- **Type:** Full combined KG (base individuals & ontology-generated individuals)
- **Contents:** Core individuals (payment methods, order channels), many `Weather` individuals, and ontology metadata.
- **Use:** Useful as a canonical snapshot or reference when you want to inspect ontology individuals and core named instances.

### ✅ `businessDay.ttl`
- **Type:** Time / business-day instances
- **Contents:** Instances of `timeOnt:BusinessDay` (one per business day in the dataset) and associated time properties.
- **Use:** Join with `transactionPerDay.ttl`, `salesPerDay.ttl`, or `weather.ttl` to do time-based analysis.

### ✅ `transactionPerDay.ttl`
- **Type:** Transaction events
- **Contents:** `events:TransactionEvent` individuals (per transaction) and related properties like payment method, order channel and `transactionOccuredOn` relationships to business days.
- **Use:** Raw transaction-level facts; use for granular analytics or to re-aggregate by store/day/payment type.

### ✅ `salesPerDay.ttl`
- **Type:** Aggregated sales events
- **Contents:** `events:SalesAggregation` individuals summarizing sales metrics (e.g., total sales, counts) and their `aggregatesOn` business day.
- **Use:** Fast queries for daily performance and trend analysis without re-aggregating raw transactions.

### ✅ `stores.ttl`
- **Type:** Store catalog and locations
- **Contents:** `core:Store` individuals with `rdfs:label` and `location:hasLocation` linking to `location:Location` (latitude/longitude and label).
- **Use:** Spatial joins (map visualizations), store-level rollups and proximity queries.

### ✅ `promotions.ttl`
- **Type:** Promotions and applicability
- **Contents:** `promotions:*` individuals describing promotions, intervals, start/end business days and applicability (`isApplicableOn` relationships).
- **Use:** Analyze promotion impact on sales when joined to `salesPerDay` and `transactionPerDay`.

### ✅ `weather.ttl`
- **Type:** Weather facts
- **Contents:** `base:Weather` individuals tied to `timeOnt:BusinessDay`, with weather attributes (temperature, condition, etc.).
- **Use:** Correlate weather to sales/transactions or detect seasonality and weather-driven behavior.

### ✅ `POI.ttl` (if present)
- **Type:** Points of Interest
- **Contents:** Nearby POIs, categories and relations (near/hasPOICategory) useful for competitive/contextual analysis.

### ✅ `Materialized_Inferred_KG_with annotations.ttl`
- **Type:** Inferred KG (OWL/TTL)
- **Contents:** Inferred triples and reasoning annotations produced by an OWL reasoner (SWRL rules, property characteristics, etc.).
- **Use:** Import into an OWL-aware store to inspect inferred facts and rule traces.

### ✅ `catalog-v001.xml`, `BurgerHavenKG.properties`
- **Type:** Metadata / properties
- **Contents:** Dataset metadata and loader/graph configuration used by the materialization pipeline.

---

## Example SPARQL queries 🔍

- Find total sales per business day:

```sparql
SELECT ?day (SUM(?total) AS ?sales)
WHERE {
  ?agg a events:SalesAggregation ;
       performance:totalSales ?total ;
       events:aggregatesOn ?day .
}
GROUP BY ?day
ORDER BY ?day
```

- Transactions for a store on a day:

```sparql
SELECT ?txn ?payMethod ?channel
WHERE {
  ?txn a events:TransactionEvent ;
       events:forStore core:S001 ;
       events:transactionOccuredOn ?day ;
       base:hasPaymentMethod ?payMethod ;
       base:hasOrderChannel ?channel .
  FILTER(?day = base:3dfeb9a1278a0489cf08b7b6c2844963)
}
```



---

## How to load and use 🔧

- Upload `.ttl` files to your RDF store (GraphDB, Fuseki, Blazegraph, Stardog, etc.).
- If you need the inferred triples, import `Materialized_Inferred_KG_with annotations.xml` into an OWL-enabled store or re-run reasoning.
- Use the provided `.properties` and `catalog-v001.xml` for automating imports if your platform supports them.

---

## Tips & Caveats ⚠️

- The graphs are materialized snapshots — if the upstream data changes, re-run the ETL/materialization pipeline in `/ETL` to regenerate them.
- RDF prefixes are consistent across files but confirm base URI if you merge graphs.
- Large TTLs (transactions/sales) can be heavy to load — prefer loading aggregated files when possible for quick analytics.

---

## Contact / Next steps 💡
- For regenerating or extending the materialized KG, check the `ETL/` scripts and `Mappings/` folder.
---

*Generated: Feb 3, 2026*