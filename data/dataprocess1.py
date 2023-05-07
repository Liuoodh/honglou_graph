#1、把红楼梦训练集处理为可被标注精灵标注的模式，标注后输出ANN格式
s="红楼梦训练集.txt"
with open(s,"r",encoding="utf-8") as f:
    index=0
    for line in f:
        with open("process1datas/"+str(index)+s,"w",encoding="utf-8") as t:
            t.write(line)
        index+=1