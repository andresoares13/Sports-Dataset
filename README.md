# Sports Dataset

**[datasetName]** is a sports dataset based on the query logs from searches on the [zerozero](https://www.zerozero.pt) platform.\
**Paper**: [PaperName](https://google.com)

## Logs Dataset

The logs consist of the user interactions collected between October 2024 and February 2025, corresponding to a total of 150 days. Approximately 1.9 million click log entries were grouped together over the 500 most popular queries, i.e., with the highest number of clicks. The `dataset.csv` file contains the list of queries and corresponding entities with clicks in the following format:

| Query   | Locale | Total Clicks | Results (Entity, (Clicks;Average Position)) |
|---------|--------|--------------|---------------------------------------------|
| atalanta | pt     | 1592         | Atalanta-Italia-Team-Futebol-Q1886 (1560;1.01), Rui Patrício-Portugal-Player-Futebol-Q294980 (32;2.0) |

Where each entity contains the name, country, type of entity, sport and Wikidata ID.


## Document Collection

The collection of documents generated from the entities that were possible to be matched in Wikidata. It contains a total of 1593 documents and can be found in JSON format in the file `wikiCollection.json`. Each document represents an entity that can be a player, team, coach or league and contains several fields: ID, title, type, description, country, list of nicknames, aka (represent also known as), list of teams (in the case of players and coaches), league (in the case of teams) and number of participants (in the case of league).


## QRels File

The QRels used can be found in the file `qrels.txt`. It was generated to be used in trec eval and it uses graded relevance. 
Three different levels of relevance were established. The first level, which was the most relevant, represented entities that had between 100 and 75% of the total clicks for a query and was given a value of 3.
The range of the second level was between 74 and 50%, and was given a value of 2, while the range of the third level was between 49 and 25% and was given a value of 1. Any lower percentage of clicks was deemed irrelevant. The list is organized in the following format:

| Query;Locale   | QueryID | DocumentID | Relevance Score |
|---------|--------|--------------|---------------------------------------------|
| academica;pt | 0     | Q243235         | 3 |
