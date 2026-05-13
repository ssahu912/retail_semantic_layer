# retail_semantic_layer
This repository helps you set up and explore a sample knowledge Graph built for a quick service restaurant (QSR) retail business.

---

## 🚀 Quick Start

### Prerequisites
- macOS (or Linux/Windows)
- Git
- Docker (recommended for GraphDB) or access to Ontotext GraphDB installation
- Python 3.8+ and pip
- Java 11+ (needed for Protege and some GraphDB installations)

### Clone and run ETL

1. Clone the repo:

```bash
git clone https://github.com/ssahu912/retail_semantic_layer.git
cd retail_semantic_layer
```

2. Create a Python virtual env and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pandas
```

3. Run ETL example (generates `dataset/business_day_attributes.csv`):

```bash
python ETL/BusinessDayAttributes.py
```

---

## 📁 Repository Structure

- `dataset/` — source CSVs and dataset README
  - `sales_transactions.csv`, `stores.csv`, `promotions.csv`, ...
- `ETL/` — simple extraction/transformation scripts (e.g., `BusinessDayAttributes.py`)
- `Mappings/` — sample mapping JSONs for data → RDF transformations
- `Materialized Graph/` — TTL files and materialized graph outputs (ready to import into GraphDB)
- `QSR-ontology/` — ontology modules and supporting files
- `Visualization/` — graph images and derived views

---

## 🔧 Ontotext GraphDB Setup (Recommended via Docker)

You can run GraphDB locally with Docker or install GraphDB on your machine.

### Docker (fast and reproducible)

```bash
# Pull and run GraphDB (change tag if you need a specific version)
docker run -d --name graphdb -p 7200:7200 \
  -e GRAPHDB_JAVA_OPTS='-Xms512m -Xmx2g' \
  ontotext/graphdb:latest
```

- Open the Workbench at: http://localhost:7200
- Create a repository (e.g., `retail-kg`) — choose a store type and an inference ruleset (e.g., `RDFS`/`OWL2-RL` if needed)
- Import TTLs from `QSR-ontology/` (ontologies first) and `Materialized Graph/` (data)
- SPARQL endpoint: `http://localhost:7200/repositories/<repo-id>`

### Local install
- Download from Ontotext: https://www.ontotext.com/products/graphdb/
- Follow installer instructions, set repository and import TTL files as above.

### Notes
- For larger graphs increase Java heap via `GRAPHDB_JAVA_OPTS` or product config
- Enable inference if you need RDFS/OWL reasoning (select ruleset when creating repo)

---

## 🛠 Ontotext Refine (Data curation → RDF)

This repo assumes you might use OpenRefine (and its RDF extension) for data cleaning and RDF export.

1. Download and run Ontetext Refine: https://platform.ontotext.com/ontorefine/install-migrate.html
2. Use OpenRefine to clean `dataset/*.csv` and export RDF (Turtle) or publish directly to GraphDB via SPARQL endpoint : https://platform.ontotext.com/ontorefine/loading-data-using-ontorefine.html

---

## 👩‍💻 Protege (Ontology editing & reasoning)

1. Download Protégé: https://protege.stanford.edu/
2. Open any `.ttl` in `QSR-ontology/` or `QSROntology.ttl` to inspect classes/properties
3. Install reasoners (HermiT, ELK) from `File → Check for plugins` or their plugin pages
4. Use Protege to validate the ontology, run classification, or export modified TTL

Optional: install SPARQL plugins to query a remote endpoint directly from Protege (useful for synchronizing changes)

---

## ✅ Typical workflow

1. Clean raw CSVs in `dataset/` (OpenRefine or Python)
2. Transform to RDF using mapping scripts or tools, place TTLs in `Materialized Graph/`
3. Start GraphDB and import ontology TTLs → create repository → import data TTLs
4. Inspect & query with GraphDB Workbench, or open ontology in Protege for reasoning

---

## 🔗 Useful links

- GraphDB docs: https://graphdb.ontotext.com/
- OpenRefine: https://openrefine.org/
- OpenRefine RDF extension: https://github.com/stkenny/grefine-rdf-extension
- Protégé: https://protege.stanford.edu/

---

## ❗ Troubleshooting & Tips
- If GraphDB fails to start, check container logs: `docker logs graphdb` and increase heap size
- If imports are slow, split large TTLs and import in chunks
- Keep ontologies (schema) loaded before instance data for cleaner inference results

---
