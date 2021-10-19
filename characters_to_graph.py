import json

with open("characters.json", "r") as f:
    characters = json.load(f)

edges = set()

url_to_title = {}
for character in characters:
    url_to_title[character["url"]] = character["title"]

for character in characters:

    title = character["title"]

    if character["medeni_hali"] != None:
        t = url_to_title[character["medeni_hali"]["url"]]

        edges.add((title, t, "spouse"))
        edges.add((t, title, "spouse"))

    if character["ailesi"] != None:
        for item in character["ailesi"]:
            t = url_to_title[item["url"]]

            edges.add((title, t, "family"))
            edges.add((t, title, "family"))

    if character["arkadaşlar"] != None:
        for item in character["arkadaşlar"]:
            t = url_to_title[item["url"]]

            edges.add((title, t, "friend"))
            edges.add((t, title, "friend"))

    if character["sevgili"] != None:
        for item in character["sevgili"]:
            t = url_to_title[item["url"]]

            edges.add((title, t, "lover"))
            edges.add((t, title, "lover"))

source = []
target = []
relation = []
for edge in edges:
    s, t, r = edge
    source.append(s)
    target.append(t)
    relation.append(r)

with open("graph.json", "w") as f:
    json.dump({"source": source, "target": target, "relation": relation}, f)
