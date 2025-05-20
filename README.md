# ZZQueryLog
**ZZQueryLog** is a dataset for evaluating entity-oriented information retrieval in the sports domain. It is built from user query logs collected on the [zerozero.pt](https://www.zerozero.pt) platform and aligned with entity documents extracted from Wikidata.
This resource includes:
- An aggregated query log with user click data
- A document collection representing sports-related entities
- Graded relevance judgments derived from click distributions
**Paper**: [TBA]
---
## 📁 Files in the Repository
| File                               | Description                                                                 |
|------------------------------------|-----------------------------------------------------------------------------|
| `zz_query_log_queries.json`        | Aggregated query logs with click counts per entity                         |
| `zz_query_log_documents.json`      | Entity-oriented documents aligned with Wikidata                            |
| `zz_query_log_qrels.txt`           | Graded relevance judgments (qrels) for evaluation                          |
| `generate_qrels_from_zz_queries.py`| Script to generate qrels from the query logs                               |
| `README.md`                        | This documentation file                                                    |
---
## 🔍 Dataset Overview
The dataset spans **150 days** (October 2024–February 2025), comprising:
- ~1.9 million raw click entries
- **500 most popular queries**
- ~1,600 unique entity documents (players, teams, coaches, competitions)
It is designed to support benchmarking of **entity-oriented retrieval systems**, including dense and hybrid ranking models.
---
## 1. Query Logs
**File:** `zz_query_log_queries.json`
Each object corresponds to a query + locale pair and contains:
- `query_id`
- `query`
- `locale`
- `total_clicks`
- `results`: list of clicked entities, sorted by clicks
Each result may include:
- `entity_id` (Wikidata ID)
- `label`, `country`, `type`, `sport`
- `clicks`, `average_position`
### Example:
```json
{
  "query_id": "q039",
  "query": "atalanta",
  "locale": "pt",
  "total_clicks": 1592,
  "results": [
    {
      "entity_id": "Q1886",
      "label": "Atalanta",
      "country": "Italia",
      "type": "Team",
      "sport": "Futebol",
      "clicks": "1560",
      "average_position": "1.01"
    },
    {
      "entity_id": "Q294980",
      "label": "Rui Patrício",
      "country": "Portugal",
      "type": "Player",
      "sport": "Futebol",
      "clicks": "32",
      "average_position": "2.0"
    }
  ]
}
```
---
## 2. Document Collection
**File:** `zz_query_log_documents.json`
Each document corresponds to an entity and includes:
- `doc_id` (internal ID)
- `wikidata_id`
- `retrieved_at`
- `labels`, `descriptions`, `aliases` (multi-language)
- `claims`: key-value property list from Wikidata
Entities include:
- Teams
- Players
- Coaches
- Competitions
---
## 3. Relevance Judgments (QRels)
**File:** `zz_query_log_qrels.txt`
Graded relevance is derived from the proportion of clicks received by each entity per query:
| Relevance Level      | Click Share (of total query clicks) |
|----------------------|--------------------------------------|
| 3 (highly relevant)  | ≥ 75%                                |
| 2 (moderately relevant) | 50%–74%                           |
| 1 (somewhat relevant)   | 25%–49%                           |
| 0 (not relevant)     | < 25% (not included)                |
Each line is formatted for TREC evaluation tools:
```
query;locale   query_id   doc_id   relevance_score
```
---
## QRels Generation Script
**File:** `generate_qrels_from_zz_queries.py`
This Python script parses the `zz_query_log_queries.json` file and creates the graded qrels in the expected format. You can run it to regenerate or customize the relevance levels.
---
## Example Evaluation
Using `trec_eval`:
```bash
trec_eval -m map -m ndcg zz_query_log_qrels.txt my_run.txt
```
---