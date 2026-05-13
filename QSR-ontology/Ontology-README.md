# QSR-KG Ontologies — Loading into Protege & Import Resolution ✅

This README explains how to open the QSR-KG ontology files in Protege, resolve imports (locally or via a simple local HTTP server), and describes the purpose of each ontology file in this folder.

---

## Quick overview (what's in this folder) 🔍
| Filename | Purpose |
|---|---|
| `master.ttl` | Master/entry ontology that references and documents the combined QSR ontologies and common properties. Use this as your starting point. |
| `qsr-core.ttl` | Core business entities: `Organization`, `Store`, `Product`, `ProductCategory` and store-specific attributes like `isDriveThru`, `isDeliveryEnabled` and `operatesStore`. |
| `qsr-events.ttl` | Business events and event-related properties: `Event`, `TransactionEvent`, `SalesAggregation`, `InventorySnapshot`, `forStore`, `occurredOn`, `hasAmount`. |
| `qsr-time.ttl` | Time concepts: `BusinessDay`, `Day`, `Weekday`, `Weekend`, `TimeInterval`, `TimeUnit` and `hasDayType`. |
| `qsr-location.ttl` | Geographic context: `Location`, `PointOfInterest`, `POICategory` and relations such as `hasLocation`, `near`, `hasPOICategory`. |
| `qsr-inventory.ttl` | Inventory concepts (`InventoryItem`) and numeric thresholds (`hasThreshold`). |
| `qsr-promotions.ttl` | Marketing and promotion concepts (`Promotion`, `PromotionPhase`, `ActivePromotion`) and `hasInterval`. |
| `qsr-competition.ttl` | Competition entities: `Competitor`, `CompetitorType`, `GlobalChain`, `LocalChain` and `hasCompetitorType`. |
| `qsr-performance.ttl` | Performance evaluation concepts: `PerformanceEvent`, `UnderperformanceEvent`, and `causedBy` linking to events. |

---

## Recommended Protege workflow (step-by-step) 🔧
1. Open Protege (5.x or later recommended).  
2. File → Open... → choose `master.ttl` (recommended as the entry point). Protege will attempt to load imports automatically.
3. If imports are unresolved (red import icons):
   - Open the `Active Ontology` tab and find the **Imports** panel.
   - Use **Add import -> From file...** and select the corresponding local `.ttl` file for each missing import. This associates the ontology IRI with the local document.
4. Alternate approach: start a local HTTP server and import by URL (useful when import statements expect HTTP locations):
   - In the `QSR-KG` folder run:
     ```bash
     python -m http.server 8000
     ```
   - In Protege, use **Add import -> From URL...** and supply e.g. `http://localhost:8000/qsr-time.ttl`.
5. After resolving all imports, check the **Imports** panel for green/loaded icons and then run a reasoner (HermiT or ELK) to validate and inspect inferred class memberships.
6. Save the project in Protege (File → Save) so mappings are persisted.

---

## Tips & Troubleshooting ⚠️
- Ensure files are not moved after creating import mappings; if they are, update the mapping or re-import.  
- If Protege can't find an ontology even when the file is present, verify the ontology IRI (top of each `.ttl`) matches the import IRI; the ontology declaration IRI must match the import resource IRI.  
- If many imports are missing, use the local HTTP server technique — it often mirrors the behavior of remote IRIs and makes re-use easier.
- If you change an ontology file externally, reopen or refresh the ontology in Protege to pick up changes.

---

## Helpful commands (macOS / Terminal) 💡
- Start a quick file server from the `QSR-KG` directory:
  ```bash
  cd /path/to/retail_semantic_layer/QSR-KG
  python -m http.server 8000
  ```
- Open Protege (if installed via command line):
  ```bash
  open -a Protege
  ```
___
