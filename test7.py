#欠席回数で学生名の色を変える

name=input("名前の入力：")
k=int(input("欠席回数の入力："))

if k>=5:
    print('\033[31m'+name+'\033[0m')

if 3<=k<5:
    print('\033[33m'+name+'\033[0m')

if k<3:
    print('\033[37m'+name+'\033[0m')






