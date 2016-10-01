# -*- coding: utf-8 -*-


#coding:utf-8
import csv
f = open('path/data2.csv', 'ab') #ファイルが無ければ作る、の'a'を指定します


csvWriter = csv.writer(f)


from os.path import join, relpath
from glob import glob
path = 'ファイル名抽出先を指定'
files = [relpath(x, path) for x in glob(join(path, '*'))]

val = 0
for word in enumerate(files):
 print word
 listData = []
 val = word
 listData.append(val)  
                   #listにデータの追加

 for loop in range(0, 1):
      #val = val * 10 + num
      val = "1"
      listData.append(val)
 csvWriter.writerow(listData)          #1行書き込み
   
f.close()