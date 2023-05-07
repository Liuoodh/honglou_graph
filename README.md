# 红楼梦人物关系知识图谱

## 命名实体识别

使用RaNER中文命名实体识别网络

模型结构如下：

![模型结构](https://modelscope.cn/api/v1/models/damo/nlp_raner_named-entity-recognition_chinese-base-book/repo?Revision=master&FilePath=description/model_image.jpg&View=true)

参考论文：https://aclanthology.org/2021.acl-long.142/

该模型在[book](https://aclanthology.org/2020.emnlp-main.518.pdf)数据集上预训练并在红楼梦数据集上微调，微调数据见data/train.txt

微调模型见：

> 链接：https://pan.baidu.com/s/12o7bAn3A8B0ypSmtB-WUZw 
> 提取码：kkuu 
>

使用方式：

```
python3 data/gen_re_data.py
```

使用前将模型路径替换为本地路径，使用后生成满足关系抽取模型输入格式的文本数据

## 关系抽取

使用BERT + 双向GRU + Attention + FC完成人物关系抽取

![img](https://github.com/percent4/people_relation_extract/raw/master/model.png)

参考项目：https://github.com/percent4/people_relation_extract

共定义了45种红楼梦人物关系:

```json
{
    "不知道":0,
    "父亲":1,
    "儿子":2,
    "奴才":3,
    "主人":4,
    "夫人":5,
    "丈夫":6,
    "丫环":7,
    "女儿":8,
    "母亲":9,
    "兄弟":10,
    "儿媳":11,
    "婆婆":12,
    "外祖母亲":13,
    "外孙女":14,
    "被抚养":15,
    "侄女":16,
    "姐妹":17,
    "好友":18,
    "养子":19,
    "哥哥":20,
    "买办":21,
    "嫂子":22,
    "陪房":23,
    "乳母亲":24,
    "相好":25,
    "孙子":26,
    "姑舅哥哥":27,
    "侄儿":28,
    "姑母亲":29,
    "兄妹":30,
    "岳母亲":31,
    "老师":32,
    "岳父亲":33,
    "朋友":34,
    "好兄弟":35,
    "女婿":36,
    "乾娘":37,
    "暧昧":38,
    "养父亲":39,
    "孙女":40,
    "伯父亲":41,
    "弟弟":42,
    "爷爷":43,
    "奶奶":44
}
```

训练数据见：data/re_train_data 和data/process2_datas

运行该项目的模型训练和模型预测脚本需要准备BERT中文版的模型数据，下载网址为：<https://github.com/google-research/bert/blob/master/multilingual.md> 。

训练模型：

```
python3 /model/RE_model/model_train.py
```

预测：

```
python3 /data/gen_triples.py
```

预测后生成人物关系三元组

## 爬虫

作为人物关系的补充，爬取了红楼梦人物列表 - 维基百科，获取了补充的人物关系三元组，见：

reptile/reptile_triples.txt

