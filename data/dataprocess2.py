# 2、将关系抽取训练数据转换为BERT + 双向GRU + Attention + FC模型所需格式
import json

def gen_re_dataset(filename1,filename2):
    re2id={"不知道": 0, "父亲": 1, "儿子": 2, "奴才": 3, "主人": 4, "夫人": 5, "丈夫": 6, "丫环": 7, "女儿": 8, "母亲": 9, "兄弟": 10, "儿媳": 11, "婆婆": 12, "外祖母亲": 13, "外孙女": 14, "被抚养": 15, "侄女": 16, "姐妹": 17, "好友": 18, "养子": 19, "哥哥": 20, "买办": 21, "嫂子": 22, "陪房": 23, "乳母亲": 24, "相好": 25, "孙子": 26, "姑舅哥哥": 27, "侄儿": 28, "姑母亲": 29, "兄妹": 30, "岳母亲": 31, "老师": 32, "岳父亲": 33, "朋友": 34, "好兄弟": 35, "女婿": 36, "乾娘": 37, "暧昧": 38, "养父亲": 39, "孙女": 40, "伯父亲": 41, "弟弟": 42, "爷爷": 43, "奶奶": 44}
    with open("./re_train_data/"+filename1,"r",encoding="utf8") as f:
        with open("./process2_datas/"+filename2,"a+",encoding="utf8") as t:
            for line in f:
                data=json.loads(line,encoding="utf8")
                text=data['text']
                pos_o1=data["h"]["pos"]
                o1=text[int(pos_o1[0]):int(pos_o1[1])]
                pos_o2=data["t"]["pos"]
                o2=text[int(pos_o2[0]):int(pos_o2[1])]
                r=re2id[data["relation"]]
                text = text.replace(o1, "#" * len(o1))
                text = text.replace(o2, "#" * len(o2))
                t.write(str(r)+" "+o1+"$"+o2+"$"+text+"\n")


if __name__ == '__main__':
    gen_re_dataset("val.json", "re_val.txt")