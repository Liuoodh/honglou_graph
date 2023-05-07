from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

# 生成关系抽取的目标数据集

#处理为一行一个句号
def process(path):
    with open(path,'r',encoding='utf8') as f:
        with open('hongloumeng.txt','a+',encoding='utf8') as t:
            for line in f.readlines():
                if(line=="" or line=="\n"):
                    continue
                line=line.strip()
                split = line.split('。')
                for item in split:
                    t.write(item+'\n')

#利用命名实体识别模型得到关系抽取数据集
def gen_re_data():
    ner_pipeline = pipeline(Tasks.named_entity_recognition,
                            'D:/Python Project/honglou_graph/model/RANER_model/230424133714.898648/output_best')
    with open('hongloumeng.txt', 'r', encoding='utf8') as f:
        with open('redata1.txt','a+',encoding='utf8') as t:
            for line in f:
                if line=="" or line=='\n':
                    continue
                # print(line)
                result=ner_pipeline(line)
                output=result['output']
                #去除重复出现的
                spans=[]
                ans_spans=[]
                for item in output:
                    if item['span'] not in spans:
                        ans_spans.append(item['span'])
                        spans.append(item['span'])
                if len(ans_spans)<2:
                    continue
                for i in range(len(ans_spans)):
                    if i==len(ans_spans)-1:
                        continue
                    for j in range(i+1,len(ans_spans)):
                        t.write(ans_spans[i]+"#"+ans_spans[j]+"#"+line)







if __name__ == '__main__':
    gen_re_data()



