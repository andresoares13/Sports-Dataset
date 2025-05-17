# ZZQueryLog

**ZZQueryLog** is a sports dataset based on the query logs from searches on the [zerozero](https://www.zerozero.pt) platform.\
**Paper**: [PaperName](https://google.com)

## Logs Dataset

The logs consist of the user interactions collected between October 2024 and February 2025, corresponding to a total of 150 days. Approximately 1.9 million click log entries were grouped together over the 500 most popular queries, i.e., with the highest number of clicks. The `dataset.json` file contains several JSON objects, each corresponding to a query that contains: query_id, query, locale, total_clicks and results. Each result contains a label, country, type, sport, clicks, average_position. Some entities in the results contain a entitiy_id, which represents their id in Wikidata. An example of a query object can be seen bellow:

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




## Document Collection

The collection of documents generated from the entities that were possible to be matched in Wikidata. It contains a total of 1593 documents and can be found in JSON format in the file `wikiCollection.json`. Each document represents an entity that can be a player, team, coach or league and contains several fields according to wikidata formatting: doc_id, wikidata_id, retrieved_at, labels, descriptions, aliases, claims. Each claim contains the id of the corresponding property alongside the value.

## Aggregated Query Logs

The aggregated query logs obtained from cleaning and grouping all of the query logs generated between October 2024 and February 2025, and that only contain entities that could be matched in Wikidata, can be found in the file `aggregatedQueryLogs.txt`.

## QRels File

The QRels used can be found in the file `qrels.txt`. It was generated to be used in trec eval and it uses graded relevance. The file to generated the QRels from the aggregated query logs that contain the click information for every entity in every query can be found in `genQrelsWiki.py`
Three different levels of relevance were established. The first level, which was the most relevant, represented entities that had between 100 and 75% of the total clicks for a query and was given a value of 3.
The range of the second level was between 74 and 50%, and was given a value of 2, while the range of the third level was between 49 and 25% and was given a value of 1. Any lower percentage of clicks was deemed irrelevant. The list is organized in the following format:

| Query;Locale   | QueryID | DocumentID | Relevance Score |
|---------|--------|--------------|---------------------------------------------|
| academica;pt | 0     | Q243235         | 3 |
