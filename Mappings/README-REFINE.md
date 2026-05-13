# Ontotext Refine Mapping Guide ✅

**Purpose:** This guide explains how to use the JSON mapping files in this folder to map CSV datasets to your ontology using the Ontotext Refine (OpenRefine-based) application and export RDF/Turtle triples for ingestion into a triplestore (e.g., GraphDB).

---

## Files in this folder 🔧
- `businessDay.json` — mappings for BusinessDay
- `POI.json` — Point of Interest mappings
- `promotions.json` — Promotion & associated business days
- `salesPerDay.json` — daily sales aggregation mappings
- `stores.json` — stores + location mappings
- `transactionPerDay.json` — transaction events and related types
- `weather.json` — weather and BusinessDay links

> Each JSON contains: `baseIRI`, `namespaces`, `subjectMappings`, `propertyMappings` and uses GREL expressions in `transformation` fields where necessary.

---

## Prerequisites 📋
- Ontotext Refine (or an OpenRefine instance with the RDF/Semantic extension) installed and running.
- The CSV data files (in the `dataset/` folder) available locally: e.g., `business_day_attributes.csv`, `stores.csv`, `promotions.csv`, etc.
- Access to a triplestore (optional) for loading generated TTL (e.g., GraphDB).

---

## Quick Overview — What the mapping JSON does 💡
- `baseIRI` and `namespaces` define prefixes used in generated IRIs and types.
- `subjectMappings` determine how subjects are created (by column value or GREL-based expressions like md5 hashes of dates).
- `propertyMappings` specify triples to be created for each subject, including datatypes and IRIs.
- GREL expressions appear in `transformation.expression` and often construct IRIs using `cells['<col>'].value` and `.md5()`.

---

## Step-by-step: Upload mapping + map data to ontology 🔁
1. **Start Ontotext Refine** and open the web UI (typically `http://127.0.0.1:3333/` or as configured).
2. **Create a new project** using the CSV file for the mapping you want to apply (e.g., choose `dataset/business_day_attributes.csv` for `businessDay.json`).
3. **Install/Enable RDF or Ontology extension** in Refine if not already present. Look for a tab or menu item named `RDF`, `RDF Preview` or `Semantic`.
4. **Open RDF export/mapping UI** in the project. 
   - Look for a control to `Import mapping` or `Load mapping` (some Refine variants allow uploading JSON mapping files or pasting mapping content into the RDF extension UI).
   - If your Refine instance expects a different mapping format, use the mapping file as a reference and recreate the mapping in the UI (namespaces, subject template, and property rules) by copying values from the JSON.
5. **Load/attach the JSON mapping:**
   - If the UI accepts JSON mapping files, upload the corresponding mapping file (e.g., `businessDay.json`).
   - If not, manually configure:
     - **Namespaces**: enter prefixes found under `namespaces` in the JSON.
     - **Subject template**: use `subject.transformation.expression` (GREL or prefix templates).
     - **Property rules**: create properties per `propertyMappings`, set value types (literal, typed literal, or IRI), and add any GREL expressions used to compute values.
6. **Preview generated RDF** (many RDF extensions have a preview or test export). Verify:
   - Generated IRIs match expected patterns (watch for prefix expansion and md5 when used).
   - Literals use correct datatypes (e.g., `xsd:decimal`, `xsd:integer`).
7. **Export triples** to Turtle (`.ttl`) or directly to your triplestore (if Refine supports direct push). Save the TTL file to `Materialized Graph/` or another chosen directory.
8. **Ingest into triplestore** (optional): Use GraphDB or your triplestore UI/API to load the `.ttl` file.

---

## Example notes & mapping gotchas ⚠️
- Column name mismatch: JSON mappings reference column names exactly (`cells['date']`, `cells['poi_id']`). Ensure CSV headers match.
- GREL expressions: `"http://example.org/qsr_kg#"+cells['date'].value.md5()` produces stable hash-based IRIs; test preview to confirm expected values.
- Prefixes: Confirm that the prefix (e.g., `timeOnt`, `core`) expansions are registered in the Refine namespaces UI.
- Datatypes: Ensure `datatype_literal` entries in mapping JSON are reflected in the UI as typed literals (`xsd:decimal`, `xsd:integer`, etc.).

---

## Validation & troubleshooting ✅
- Use the RDF preview to check a few rows before full export.
- If triples are missing, verify the property rule uses correct value source (column vs. row_index) and transformation language (`grel` vs `prefix`).
- If IRIs look wrong, check for accidental extra spaces in GREL expressions (the mappings use exact GREL strings, including quotes and concatenation).

---

## Helpful tips 💡
- Keep a copy of the mapping JSON as a canonical source of truth for programmatic mapping or for reproducing the mapping in other tools.
- For repeated runs, automate the Refine export with the Refine API (if available) to avoid manual steps.
- When in doubt, preview small subsets of rows and compare generated TTL with expected ontology terms.