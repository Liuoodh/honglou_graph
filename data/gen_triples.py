#利用关系抽取模型和待关系抽取的数据得到人物关系三元组
import json
import numpy as np
from model.RE_model.bert.extract_feature import BertVector
from keras.models import load_model
from model.RE_model.att import Attention

with open('rel_dict.json', 'r', encoding='utf-8') as f:
    rel_dict = json.load(f)

id_rel_dict = {v:k for k,v in rel_dict.items()}
bert_model = BertVector(pooling_strategy="NONE", max_seq_len=128)
best_model_path = '../model/RE_model/models/per-rel-02-0.9889.h5'
model = load_model(best_model_path, custom_objects={"Attention": Attention})
with open("redata.txt","r",encoding="utf8") as f:
    with open("model_gen_triple.txt","a+",encoding="utf8") as t:
        for line in f:
            text1=line
            per1, per2, doc = text1.split('#')
            text = '$'.join([per1, per2, doc.replace(per1, len(per1) * '#').replace(per2, len(per2) * '#')])
            vec = bert_model.encode([text])["encodes"][0]
            x_train = np.array([vec])
            predicted = model.predict(x_train)
            y = np.argmax(predicted[0])
            relation=id_rel_dict[y]
            t.write(per1+" "+per2+" "+relation+"\n")


