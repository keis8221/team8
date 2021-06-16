while True:
    try:
        Weight = float(input('体重(kg)を入力してください：'))
        Height = float(input('身長(m)を入力してください：'))
        
        BMI = Weight/(Height*Height)
        break;
    except:
            print("入力ミスがあります．再度入力してください．")
            

BMI_L = 18.5
BMI_M = 25.0
BMI_H = 30.0

if BMI < BMI_L:
    Judge = '痩身'
elif BMI >= BMI_L and BMI < BMI_M:
    Judge = '標準'
elif BMI >= BMI_M and BMI < BMI_H:
    Judge = '軽肥満'
else:
    Judge = '肥満'

print(f'BMI：{BMI}')
print(f'このBMIの方は「{Judge}」です．')

Weight_Std=22*(Height*Height)
# Weight_Stdを計算する部分を上に追加するべし．
print(f'身長 {Height} mの方の標準体重は {Weight_Std} kgです．')