import json

with open('dataset.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

newLines = []


for query in data:
    
    results = query['results']

    totalClicks = int(query['total_clicks'])
    rel = 3
    ids = []
    for entity in results:

        if 'entity_id' not in entity:
            continue

        #Players that became coaches are different entities in zerozero but in Wikidata are matched to the same entity
        if entity['entity_id'] in ids:
            continue
        else:
            ids.append(entity['entity_id'])

        newLine = ""
        newLine += query['query'].replace(" ","_") + ";" + query['locale'] + " 0 "
        clicks = int(entity['clicks'])
        clickWeight = round((clicks/totalClicks) * 100,2)

        if clickWeight >= 75:
            rel = 3
        elif 50 <= clickWeight < 75:
            rel = 2
        elif 25 <= clickWeight < 50:
            rel = 1
        else:
            break

        newLine += entity['entity_id'] + " " + str(rel)
        newLines.append(newLine)

with open("zz_query_log_qrels.txt", "w") as qrel_file:
    for i, line in enumerate(newLines):
        if i < len(newLines) - 1:
            qrel_file.write(line + "\n")
        else:
            qrel_file.write(line)

                