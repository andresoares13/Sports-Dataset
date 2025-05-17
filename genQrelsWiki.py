
newLines = []

with open("search_string_items_wiki.txt", "r") as txt_file:
    for line in txt_file:
        parts = line.strip().split("|")
        if parts[3] == '':
            continue
        if len(parts) > 3:
            ids = parts[3].split(",")
            totalClicks = int(parts[2])
            rel = 3
            for id_str in ids:
                newLine = ""
                newLine += parts[0].replace(" ", "_") + ";" + parts[1] + " 0 "
                clean_id = id_str.split("(")[0].strip()
                clicks = int(id_str.split("(")[1].split(";")[0])
                clickWeight = round((clicks/totalClicks) * 100,2)

                if clickWeight >= 75:
                    rel = 3
                elif 50 <= clickWeight < 75:
                    rel = 2
                elif 25 <= clickWeight < 50:
                    rel = 1
                else:
                    break

                newLine += clean_id + " " + str(rel)

                newLines.append(newLine)

with open("qrels3Wiki.txt", "w") as qrel_file:
    for line in newLines:
        qrel_file.write(line + "\n")

                