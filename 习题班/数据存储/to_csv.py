'''
CSV 逗号分割符
ID  Username, Age, Country
xxx xxxxxxxx  xxx  xxxxx
'''

import csv
headers = ["ID", "UserName", "Age", "Country"]
rows =[
    (1001, "liudana", 18, "BeiJing"),
    (1002, "huanglaoban", 28, "chengdu"),
    (1002, "yitengjun", 29, 'jinan')
]
with open("test.csv", "w",newline="")as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)
