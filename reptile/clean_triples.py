def read_relations(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()
    relations = []
    for row in data:
        d = row.strip().split(",")
        relations.append(d)
    return relations


relations = read_relations('raw_relations.txt')
clean_relations = []
for d in relations:
    if len(d) != 3: continue
    if d[2] == "一": continue
    if "即" in d[1]: 
        clean_relations.append([d[0], d[1][1:], d[2]])
        continue
    if "、" in d[1]:
        e1 = d[1].split("、")[0]
        e2 = d[1].split("、")[1]
        clean_relations.append([d[0], e1, d[2]])
        clean_relations.append([d[0], e2, d[2]])
        continue
    clean_relations.append(d)


with open('reptile_triples.txt', 'w', encoding='utf-8') as f:
    for r in clean_relations:
        f.write('%s,%s,%s\n' % (r[0], r[1], r[2]))