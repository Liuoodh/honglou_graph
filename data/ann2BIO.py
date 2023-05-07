# 把ANN格式转换为BIO格式，用于命名实体识别模型微调
import glob

def ann2BIO(text,ann_str,fstream):
    label=['O' for _ in range(len(text))]
    ann_list=ann_str.strip().split('\n')
    for i,line in enumerate(ann_list):
        try:
            T,typ,word=line.strip().split('\t')
            t,s,e=typ.split()
            s,e=int(s),int(e)
            label[s-2]='B-'+t
            while s<e-1:
                s+=1
                label[s-2]='I-'+t
        except:
            continue
    for t,l in zip(list(text),label):
        line='\t'.join([t,l])
        fstream.write(line)
        fstream.write('\n')
    fstream.write('\n')


def gen_train_data():
    root_dir="process1datas/outputs"
    stream=open("ner_train.txt","a+",encoding='utf8')
    file_list=glob.glob(root_dir+'/*.ann')
    for ann_path in file_list:
        ann_path=ann_path.replace('\\','/')
        txt_path=ann_path.replace('/outputs','').replace('ann','txt')
        try:
            ft=open(txt_path,'r',encoding='utf8')
            text=ft.read().strip()
            ft.close()
            fa=open(ann_path,'r',encoding='utf8')
            ann=fa.read().strip()
            fa.close()
            if ann=='':
                continue
            ann2BIO(text,ann,stream)
        except Exception as e:
            print(ann_path,e)
    stream.close()

if __name__ == '__main__':
    gen_train_data()