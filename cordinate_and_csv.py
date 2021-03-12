import os
import json
import glob
import csv
import re
import time
import subprocess
import winsound

i = 0

oprun = subprocess.Popen(["C:\optest\openposepre.bat"], shell=False, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

while True:
    try:
        all_files = glob.glob('/openpose/output/*.json') 
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
        with open("neck_data.csv", "a") as f:            
            writer = csv.writer(f, lineterminator='\n')  
            writer.writerow(neck)

        with open("left_shoulder_data.csv", "a") as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(left_shoulder)

        with open("right_shoulder_data.csv", "a") as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(right_shoulder)
    
        i = i + 1
        
        #if neck[0] < 600:
         #   winsound.Beep(2000, 500)

    except IndexError:
        print("Waiting for the file to be created")
    
    
    