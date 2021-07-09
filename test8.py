import linecache
import pandas as pd

df = pd.read_csv('-F1.csv')

for i in range(2):
 target_line = linecache.getline('-F1.csv', i+2)
 num = target_line.count('×')

 # print(target_line) 
 print(num)

 #欠席回数で学生名の色を変える
 name = df["名前"][i]
 k=num

 if k>=5:
     print('\033[31m'+name+'\033[0m')

 elif 3<=k<5:
     print('\033[33m'+name+'\033[0m')

 else:
     print('\033[37m'+name+'\033[0m')

 linecache.clearcache() 