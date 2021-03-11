import json
import os
import re
import glob
import csv

num = len(os.listdir('/openpose/output'))             #フォルダの中のJSONファイル数 違う場所にある場合はpathを変更
all_files = glob.glob('/openpose/output/*.json')      #フォルダ内のJSONファイルを取得 違う場所にある場合はpathを変更

#各JSONファイルのほしい座標データを取得し表示
for i in range(num):                                  
    open_file = open(all_files[i],'r')
    load_file = json.load(open_file)
    part = load_file["part_candidates"]
    position = part[0]
    neck = position["1"]
    left_shoulder = position["2"]
    right_shoulder = position["5"]

    print(neck)
    print(left_shoulder)
    print(right_shoulder)
    
    #各座標データをcsvで出力
    with open("neck_data.csv", "a") as f:            　#データが追加され続けるので新しいデータをとるときは前のファイルを削除またはファイル名を変更
        writer = csv.writer(f, lineterminator='\n')  
        writer.writerow(neck)

    with open("left_shoulder_data.csv", "a") as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(left_shoulder)

    with open("right_shoulder_data.csv", "a") as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(right_shoulder)
    
#csvファイル:左から,X座標,Y座標,信用度
