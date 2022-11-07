import json
from tempfile import tempdir
from traceback import print_tb
#from opencc import OpenCC

# f = open("item-names.json",'r',encoding='utf8')
#
# data = f.readlines()
# jd = json.load(f)
# print(jd)

my_json_data = []
or_json_data = []
new_json_data = []

#with open('./item-names.json','r',encoding='utf-8-sig')as fp:
#    my_json_data = json.load(fp)

with open('./resource/to_extract/item-runes.json','r',encoding='utf-8-sig')as fp:
    my_json_data = json.load(fp)

with open('./ori/item-runes.json','r',encoding='utf-8-sig')as dp:
    or_json_data = json.load(dp)

comment = {}
float_value = {}

#rune
for item in or_json_data:
    key = item["Key"]
    name = item["zhCN"]

    #符文显示文本
    if key.find("r") == 0 and name.find("符文") != -1:
        comment[item['id']] = ["ÿc2"+name[:name.find("符文")]+"ÿc8"+":#"+key[1:],"ÿc2"+item["zhTW"][3:]+"ÿc8"+":#"+key[1:]]
    elif key.find("r") == 0 and key.find("L") != -1:
         comment[item['id']] = ["ÿc2"+name[:2]+"ÿc8"+"#"+key[1:-1], "ÿc2"+item["zhTW"][0:2]+"ÿc8"+"#"+key[1:-1]]
        # comment[item['id']] = ["#"+key[1:-1], "#"+key[1:-1]]
        # print(comment[item['id']])

#runewordcls
for item in my_json_data:
    # print(item["zhCN"])
    key = item["Key"]
    
    r = key.find("Runeword")
    if r != -1:
        name = item["zhCN"]

        # 抽出来所有浮动数值id
        t = name.find("MAX:")
        if t != -1:
            t1 = item["zhTW"].find("MAX:")
            n1 = item["zhTW"].find("]")

            #print(name)
            n = name.find("]")
            float_value[item['id']]=[name[t:n],item["zhTW"][t1:n1]]
            #print(float_value[item['id']])

        #抽出吐槽
        t = name.find("ÿc5")
        if t != -1:
            n = name.find("\n",t+1,len(name))
            t1 = item["zhTW"].find("ÿc5")
            n1 = item["zhTW"].find("\n",t1+3,len(item["zhTW"]))
            #print(name[t+3:n])
            comment[item['id']] = [name[t+3:],item["zhTW"][t1+3:]]
        else:
            t = name.find("\n")
            n = name.find("MAX:")
            if t != -1 and n==-1:
                #print(name)
                t1 = item["zhTW"].find("\n")
                comment[item['id']] = [name[:t], item["zhTW"][:t1]]
            elif t!=-1 and n!=-1:
                m = name.find("\n",t+1,len(name))
                if m!=-1:
                    #print(name)
                    #comment[item['id']] = [name[t+1:m], item["zhTW"][t+1:m]]
                    comment[item['id']] = [name[t+1:m], item["zhTW"][t+1:m]]

                    #comment[item['id']] = [OpenCC("s2t").convert(name[t+1:m]), OpenCC("s2t").convert((item["zhTW"][t+1:m]))]  转化为繁体
                
#print("所有符文吐槽")
#print(json.dumps(comment, ensure_ascii=False))

with open('./table/rune_float_value.json','w',encoding='utf-8')as fp:
    fp.write(json.dumps(float_value,ensure_ascii=False))

with open('./table/rune_comment.json','w',encoding='utf-8')as fp:
    fp.write(json.dumps(comment,ensure_ascii=False))