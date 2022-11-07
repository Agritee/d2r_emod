import json
from tokenize import Special
import shutil

light = []
mid = []
heavy = []
epic = []
ext = []
material = []
comment = {}
rune_float_value = {}
rune_comment = {}
float_value = {}
abbreviation = []
specialItem = []
specialAffix = []
item_names = {}
item_modifiers = {}
item_nameaffixes = {}

item_names = {}
item_modifiers = {}
item_nameaffixes = {}
item_runes = {}
item_baned = []

new_item_names = []
new_item_nameaffixes = []
new_item_names_ban = []
new_item_nameaffixes_ban = []
new_item_runes = []
ui = []


golds = []
greens = []

with open('./table/好底材id.json', 'r', encoding='utf8') as dp:
    material = json.load(dp)
with open('./table/精华装备id.json', 'r', encoding='utf8') as dp:
    epic = json.load(dp)
with open('./table/扩展装备id.json', 'r', encoding='utf8') as dp:
    ext = json.load(dp)
with open('./table/轻型装备id.json', 'r', encoding='utf8') as dp:
    light = json.load(dp)
with open('./table/中型装备id.json', 'r', encoding='utf8') as dp:
    mid = json.load(dp)
with open('./table/重型装备id.json', 'r', encoding='utf8') as dp:
    heavy = json.load(dp)
with open('./table/float_value.json', 'r', encoding='utf8') as dp:
    float_value = json.load(dp)
with open('./table/comment.json', 'r', encoding='utf8') as dp:
    comment = json.load(dp)
with open('./table/rune_float_value.json', 'r', encoding='utf8') as dp:
    rune_float_value = json.load(dp)
with open('./table/rune_comment.json', 'r', encoding='utf8') as dp:
    rune_comment = json.load(dp)
with open('./table/名称缩短.json', 'r', encoding='utf8') as dp:
    abbreviation = json.load(dp)
with open('./table/特殊物品.json', 'r', encoding='utf8') as dp:
    specialItem = json.load(dp)
with open('./table/特殊词缀.json', 'r', encoding='utf8') as dp:
    specialAffix = json.load(dp)
with open('./table/暗金物品名称.txt', 'r') as dp:
    golds = dp.readlines()
with open('./table/绿色物品名称.txt', 'r') as dp:
    greens = dp.readlines()
with open('./table/屏蔽物品id.json', 'r', encoding='utf8') as dp:
    item_baned = json.load(dp)
with open('./sourceFile/data/data/local/lng/strings/item-names.json', 'r', encoding='utf-8-sig') as dp:
    item_names = json.load(dp)
# with open('./sourceFile/data/data/local/lng/strings/item_modifiers.json','r',encoding='utf-8-sig')as dp:
#     item_modifiers = json.load(dp)
with open('./sourceFile/data/data/local/lng/strings/item-nameaffixes.json', 'r', encoding='utf-8-sig') as dp:
    item_nameaffixes = json.load(dp)
with open('./sourceFile/data/data/local/lng/strings/item-runes.json', 'r', encoding='utf-8-sig') as dp:
    item_runes = json.load(dp)

with open('./sourceFile/data/data/local/lng/strings/ui.json', 'r', encoding='utf-8-sig') as dp:
    ui = json.load(dp)

def add_separator_suffix(name, separator, suffix):
    if separator != "":
        if name.find(separator) != -1:
            return name + suffix
    return name + separator + suffix

def find_index_in_array(id, array):
    index = 0
    for index in range(len(array)):
        if array[index]["id"] == int(id):
            return index
    return -1

def find_item_color(n):
    find = False
    for name in golds:
        name = name[:-1]
        if n == name:
            find = True
            break
    if find:
        return 0

    for name in greens:
        name = name[:-1]
        if n == name:
            find = True
            break
    if find:
        return 1

    return -1

#item_names
for item in item_names:
    # print(item["zhCN"])
    name = item

    #底材类型，轻扩重，轻不显示出来
    if name["id"] in ext:
        name["zhCN"] = add_separator_suffix(name["zhCN"], "|", "扩")
        name["zhTW"] = add_separator_suffix(name["zhTW"], "|", "擴")
    if name["id"] in epic:
        name["zhCN"] = add_separator_suffix(name["zhCN"], "|", "精")
        name["zhTW"] = add_separator_suffix(name["zhTW"], "|", "精")
    if name["id"] in light:
        name["zhCN"] = add_separator_suffix(name["zhCN"], "|", "轻")
        name["zhTW"] = add_separator_suffix(name["zhTW"], "|", "輕")
    if name["id"] in mid:
        name["zhCN"] = add_separator_suffix(name["zhCN"], "|", "中")
        name["zhTW"] = add_separator_suffix(name["zhTW"], "|", "中")
    if name["id"] in heavy:
        name["zhCN"] = add_separator_suffix(name["zhCN"], "|", "重")
        name["zhTW"] = add_separator_suffix(name["zhTW"], "|", "重")
    if name["id"] in material:
        name["zhCN"] = add_separator_suffix(name["zhCN"], "", "ÿc1*")       #底材
        name["zhTW"] = add_separator_suffix(name["zhTW"], "", "ÿc1*")

    #吐槽
    if str(name["id"]) in comment.keys():
        item_color = ""
        if find_item_color(name["enUS"]) == 0:
            item_color = "ÿc4"
        if find_item_color(name["enUS"]) == 1:
            item_color = "ÿc2"

        name["zhCN"] = "ÿc8" + comment[str(name["id"])][0] + "\n" + item_color + name["zhCN"]
        name["zhTW"] = "ÿc8" + comment[str(name["id"])][1] + "\n" + item_color + name["zhTW"]

    #变量
    if str(name["id"]) in float_value.keys():
        item_color = ""
        if find_item_color(name["enUS"]) == 0:
            item_color = "ÿc4"
        if find_item_color(name["enUS"]) == 1:
            item_color = "ÿc2"

        name["zhCN"] = "ÿc3" + float_value[str(name["id"])][0] + "\n" + item_color + name["zhCN"]
        name["zhTW"] = "ÿc3" + float_value[str(name["id"])][1] + "\n" + item_color + name["zhTW"]

    #名称缩短
    index = find_index_in_array(name["id"], abbreviation)
    if index != -1:
        name = abbreviation[index]
    
    #特殊物品
    index = find_index_in_array(name["id"], specialItem)
    if index != -1:
        name = specialItem[index]

    #特殊词缀
    index = find_index_in_array(name["id"], specialAffix)
    if index != -1:
        name = specialAffix[index]

    #备份未屏蔽的文件，用于同时生成屏蔽版和非屏蔽版本的文件
    new_item_names.append(name)

    #屏蔽
    name_ban = name.copy()
    if name_ban["id"] in item_baned:
        name_ban["zhTW"] = ""
        #print(name_ban["zhCN"])

    new_item_names_ban.append(name_ban)

#item_nameaffixes
for item in item_nameaffixes:
    # print(item["zhCN"])
    name = item
    index = find_index_in_array(name["id"], abbreviation)       #名称缩短
    if index != -1:
        name = abbreviation[index]
    index = find_index_in_array(name["id"], specialItem)        #特殊物品        
    if index != -1:
        name = specialItem[index]
    index = find_index_in_array(name["id"], specialAffix)         #特殊词缀
    if index != -1:
        name = specialAffix[index]
        #print(name["zhTW"])

    #备份未屏蔽的文件，用于同时生成屏蔽版和非屏蔽版本的文件
    new_item_nameaffixes.append(name)
    
    #屏蔽
    name_ban = name.copy()
    if name_ban["id"] in item_baned:
        name_ban["zhTW"] = ""
        #print(name_ban["zhCN"])  
    
    new_item_nameaffixes_ban.append(name_ban)

#runeword
for item in item_runes:
    name = item

    #吐槽
    if str(name["id"]) in rune_comment.keys():
        if rune_comment[str(name["id"])][0].find("#") != -1:
            name["zhCN"] = rune_comment[str(name["id"])][0]
            name["zhTW"] = rune_comment[str(name["id"])][1]
        else:
            name["zhCN"] = "ÿc8" + rune_comment[str(name["id"])][0] + "\n" + item_color + name["zhCN"]
            name["zhTW"] = "ÿc8" + rune_comment[str(name["id"])][1] + "\n" + item_color + name["zhTW"]

    #变量
    if str(name["id"]) in rune_float_value.keys():
        item_color = ""
        if find_item_color(name["enUS"]) == 0:
            item_color = "ÿc4"
        if find_item_color(name["enUS"]) == 1:
            item_color = "ÿc2"

        name["zhCN"] = "ÿc3" + rune_float_value[str(name["id"])][0] + "\n" + "ÿc7" + name["zhCN"]
        name["zhTW"] = "ÿc3" + rune_float_value[str(name["id"])][1] + "\n" + "ÿc7" + name["zhTW"]  

    new_item_runes.append(name)

#ui，黑毛提示修改
for item in ui:
    if item["id"] >= 27186 and item["id"] <= 27191:
        item["zhTW"] = item["zhTW"] + "  " + str(item["id"] - 27185) + "/6"
        item["zhCN"] = item["zhCN"] + "  " + str(item["id"] - 27185) + "/6"


#拷贝源文件到预览文件夹
shutil.copy('./sourceFile/data/data/local/lng/strings/item-names.json', './preview/sourceFile')
shutil.copy('./sourceFile/data/data/local/lng/strings/item-nameaffixes.json', './preview/sourceFile')
shutil.copy('./sourceFile/data/data/local/lng/strings/item-runes.json', './preview/sourceFile')

#未屏蔽的item-names
with open('./release/fullVersion/item-names.json', 'w', encoding='utf-8-sig') as dp:      #写入release文件夹
    dp.write(json.dumps(new_item_names, ensure_ascii=False, indent=2))
with open('./preview/releaseFile/fullVersion/item-names.json', 'w', encoding='utf-8-sig') as dp:    #写入预览文件夹
    dp.write(json.dumps(new_item_names, ensure_ascii=False, indent=2))

#未屏蔽的item-nameaffixes
with open('./release/fullVersion/item-nameaffixes.json', 'w', encoding='utf-8-sig') as dp:
    dp.write(json.dumps(new_item_nameaffixes, ensure_ascii=False, indent=2))
with open('./preview/releaseFile/fullVersion/item-nameaffixes.json', 'w', encoding='utf-8-sig') as dp:
    dp.write(json.dumps(new_item_nameaffixes, ensure_ascii=False, indent=2))

#屏蔽的item-names
with open('./release/item-names.json', 'w', encoding='utf-8-sig') as dp:
    dp.write(json.dumps(new_item_names_ban, ensure_ascii=False, indent=2))
with open('./preview/releaseFile/item-names.json', 'w', encoding='utf-8-sig') as dp:
    dp.write(json.dumps(new_item_names_ban, ensure_ascii=False, indent=2))

#屏蔽的item-nameaffixes
with open('./release/item-nameaffixes.json', 'w', encoding='utf-8-sig') as dp:
    dp.write(json.dumps(new_item_nameaffixes_ban, ensure_ascii=False, indent=2))
with open('./preview/releaseFile/item-nameaffixes.json', 'w', encoding='utf-8-sig') as dp:
    dp.write(json.dumps(new_item_nameaffixes_ban, ensure_ascii=False, indent=2))

#item-runes
with open('./release/item-runes.json', 'w', encoding='utf-8-sig') as dp:
    dp.write(json.dumps(new_item_runes, ensure_ascii=False, indent=2))
with open('./preview/releaseFile/item-runes.json', 'w', encoding='utf-8-sig') as dp:
    dp.write(json.dumps(new_item_runes, ensure_ascii=False, indent=2))

#ui
with open('./release/ui.json', 'w', encoding='utf-8-sig') as dp:
    dp.write(json.dumps(ui, ensure_ascii=False, indent=2))

