"""
Script to generate a TREC-style qrels file from the ZZQueryLog dataset.
This utility processes query logs containing user interactions and entity clicks,
and assigns graded relevance levels based on click share thresholds. Entities
with Wikidata matches are included and grouped per query.
Relevance levels:
- 3: ≥ 75% of total clicks
- 2: ≥ 50% and < 75%
- 1: ≥ 25% and < 50%
- 0: < 25% (excluded)
Input: zz_query_log_queries.json
Output: zz_query_log_qrels.txt
Author: André Soares
Date: May 2025
"""


import json

#Loads the query logs
with open('zz_query_log_queries.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

newLines = []


for query in data:
    
    results = query['results'] #entities with clicks for each query

    totalClicks = int(query['total_clicks'])
    rel = 3 #relevance grade
    ids = []
    counter = 0
    for entity in results:

        if 'entity_id' not in entity: #skips entities that did not have a match in Wikidata
            continue

        #Players that became coaches are different entities in zerozero but in Wikidata are matched to the same entity
        if entity['entity_id'] in ids:
            continue
        else:
            ids.append(entity['entity_id'])

        newLine = ""
        newLine += query['query_id'] + " " + str(counter) + " "
        clicks = int(entity['clicks'])
        clickWeight = round((clicks/totalClicks) * 100,2) #percentage of clicks for each results inside of each query

        if clickWeight >= 75: #graded relevance calculation
            rel = 3
        elif 50 <= clickWeight < 75:
            rel = 2
        elif 25 <= clickWeight < 50:
            rel = 1
        else:
            break

        newLine += entity['entity_id'] + " " + str(rel)
        newLines.append(newLine)
        counter += 1

#writes lines to qrels file
with open("zz_query_log_qrels.txt", "w") as qrel_file:
    for i, line in enumerate(newLines):
        if i < len(newLines) - 1:
            qrel_file.write(line + "\n")
        else:
            qrel_file.write(line)

                