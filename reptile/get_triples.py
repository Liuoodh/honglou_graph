# read excel
import pandas as pd
df = pd.read_excel('./wiki_data.xlsx', sheet_name='Sheet1')
# extract relations
all_relations = []
for i in range(len(df)):
    line = df.iloc[i, 1]
    # line是float类型
    if isinstance(line, float):
        continue
    if line == "贾府远房宗族":
        relation = df.iloc[i, 0]
        relation += ",贾府,远房宗族"
        all_relations.append(relation)
    # split by '，' and '。'
    line = line.split('，')
    for t in line:
        t = t.split('。')
        for s in t:
            relation = df.iloc[i, 0]
            if '的' in s:
                # s前面的部分, s后面的部分
                s = s.split('的')
                for r in s:
                    relation+=","+r
            elif '之' in s:
                s = s.split('之')
                for r in s:
                    relation+=","+r
            elif '长子' in s:
                relation += ","+s[:-2]+",长子"
            elif '次子' in s:
                relation += ","+s[:-2]+",次子"
            else:
                continue
            all_relations.append(relation)

with open('raw_relations.txt', 'w', encoding='utf-8') as f:
    for t in all_relations:
        f.write("".join(t).strip() + '\n')