#coding:utf-8
file = open("tweets2.txt", 'r', encoding='utf-8')
lines = file.readlines()
file.close()

for line in lines:
    diccionario = eval(line)
    if 'sex' not in diccionario['text']:
        try:
            print(diccionario['text'])
        except:
            pass