'''
https://dotblogs.com.tw/cylcode/2019/01/11/174719
將csv檔裡面不需要的單詞換成unknown
'''
import csv
#import pandas as pd
# 開啟 CSV 檔案
with open('eggs_two.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    with open('test.csv') as f:
        myCsvDic = csv.DictReader(f)
        for row in myCsvDic:
            if row["word"] != 'yes' and row["word"] != 'no' and row["word"] != 'up' and row["word"] != 'down' and row["word"] != 'left' and row["word"] != 'right' and row["word"] != 'on' and row["word"] != 'off' and row["word"] != 'stop' and row["word"] != 'go' and row["word"] != 'silence' :
                row["word"] = 'unknown'
                writer.writerow([row["id"],row["word"]])
            else :
                writer.writerow([row["id"],row["word"]])