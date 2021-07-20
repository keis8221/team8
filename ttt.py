import os
from flask import Flask,  render_template, send_file
import pandas as pd

app = Flask(__name__)
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/apply')
def apply():
    return render_template('apply.html')

@app.route('/subject')
def subject():
    return render_template('subject.html')

@app.route('/attenpt')
def ttt():
    df = pd.read_csv('./subject.templates/M1.csv',keep_default_na=False,header=None,index_col=False,encoding="utf-8").values.tolist()
    print(df)
    return render_template('M1.html', title='心理学',df=df,table_id="table")

@app.route('/attenpt1')
def ttt1():
    df = pd.read_csv('./subject.templates/M2.csv',keep_default_na=False,header=None,index_col=False,encoding="utf-8").values.tolist()
    print(df)
    return render_template('M2.html', title='教養英語',df=df)

@app.route('/attenpt2')
def ttt2():
    df = pd.read_csv('./subject.templates/M3.csv',keep_default_na=False,header=None,index_col=False,encoding="utf-8").values.tolist()
    print(df)
    return render_template('M3.html', title='情報理論',df=df)

@app.route('/attenpt3')
def ttt3():
    df = pd.read_csv('./subject.templates/M4.csv',keep_default_na=False,header=None,index_col=False,encoding="utf-8").values.tolist()
    print(df)
    return render_template('M4.html', title='システム開発演習',df=df)

@app.route('/attenpt4')
def ttt4():
    df = pd.read_csv('./subject.templates/T2.csv',keep_default_na=False,header=None,index_col=False,encoding="utf-8").values.tolist()
    print(df)
    return render_template('T2.html', title='英会話',df=df)

@app.route('/attenpt5')
def ttt5():
    df = pd.read_csv('./subject.templates/T3_1.csv',keep_default_na=False,header=None,index_col=False,encoding="utf-8").values.tolist()
    print(df)
    return render_template('T3_1.html', title='電子回路学',df=df)

@app.route('/attenpt6')
def ttt6():
    df = pd.read_csv('./subject.templates/T3_2.csv',keep_default_na=False,header=None,index_col=False,encoding="utf-8").values.tolist()
    print(df)
    return render_template('T3_2.html', title='物理学',df=df)

@app.route('/attenpt7')
def ttt7():
    df = pd.read_csv('./subject.templates/T4.csv',keep_default_na=False,header=None,index_col=False,encoding="utf-8").values.tolist()
    print(df)
    return render_template('T4.html', title='応用数学数学',df=df)

@app.route('/attenpt8')
def ttt8():
    df = pd.read_csv('./subject.templates/T5.csv',keep_default_na=False,header=None,index_col=False,encoding="utf-8").values.tolist()
    print(df)
    return render_template('T5.html', title='数学演習',df=df)

@app.route('/attenpt9')
def ttt9():
    df = pd.read_csv('./subject.templates/W12.csv',keep_default_na=False,header=None,index_col=False,encoding="utf-8").values.tolist()
    print(df)
    return render_template('W12.html', title='プログラミング',df=df)

@app.route('/attenpt10')
def ttt10():
    df = pd.read_csv('./subject.templates/W3_1.csv',keep_default_na=False,header=None,index_col=False,encoding="utf-8").values.tolist()
    print(df)
    return render_template('W3_1.html', title='経済学',df=df)

@app.route('/attenpt11')
def ttt11():
    df = pd.read_csv('./subject.templates/W3_2.csv',keep_default_na=False,header=None,index_col=False,encoding="utf-8").values.tolist()
    print(df)
    return render_template('W3_2.html', title='文学・文化学(W3_2)',df=df)

@app.route('/attenpt12')
def ttt12():
    df = pd.read_csv('./subject.templates/W4.csv',keep_default_na=False,header=None,index_col=False,encoding="utf-8").values.tolist()
    print(df)
    return render_template('W4.html', title='信号処理',df=df)

@app.route('/attenpt13')
def ttt13():
    df = pd.read_csv('./subject.templates/W5_1.csv',keep_default_na=False,header=None,index_col=False,encoding="utf-8").values.tolist()
    print(df)
    return render_template('W5_1.html', title='保健体育',df=df)

@app.route('/attenpt14')
def ttt14():
    df = pd.read_csv('./subject.templates/W5_2.csv',keep_default_na=False,header=None,index_col=False,encoding="utf-8").values.tolist()
    print(df)
    return render_template('W5_2.html', title='コミュニケーション入門',df=df)

@app.route('/attenpt15')
def ttt15():
    df = pd.read_csv('./subject.templates/Th2.csv',keep_default_na=False,header=None,index_col=False,encoding="utf-8").values.tolist()
    print(df)
    return render_template('Th2.html', title='計算機アーキテクチャ',df=df)

@app.route('/attenpt16')
def ttt16():
    df = pd.read_csv('./subject.templates/Th34.csv',keep_default_na=False,header=None,index_col=False,encoding="utf-8").values.tolist()
    print(df)
    return render_template('Th34.html', title='情報工学実習',df=df)

@app.route('/attenpt17')
def ttt17():
    df = pd.read_csv('./subject.templates/Th5_1.csv',keep_default_na=False,header=None,index_col=False,encoding="utf-8").values.tolist()
    print(df)
    return render_template('Th5_1.html', title='電磁気学',df=df)

@app.route('/attenpt18')
def ttt18():
    df = pd.read_csv('./subject.templates/Th5_2.csv',keep_default_na=False,header=None,index_col=False,encoding="utf-8").values.tolist()
    print(df)
    return render_template('Th5_2.html', title='電子回路学(Th5_2)',df=df)

@app.route('/attenpt19')
def ttt19():
    df = pd.read_csv('./subject.templates/F1.csv',keep_default_na=False,header=None,index_col=False,encoding="utf-8").values.tolist()
    print(df)
    return render_template('F1.html', title='科学英語',df=df)

@app.route('/attenpt20')
def ttt20():
    df = pd.read_csv('./subject.templates/F2.csv',keep_default_na=False,header=None,index_col=False,encoding="utf-8").values.tolist()
    print(df)
    return render_template('F2.html', title='情報ネットワーク',df=df)

@app.route('/attenpt21')
def ttt21():
    df = pd.read_csv('./subject.templates/F3.csv',keep_default_na=False,header=None,index_col=False,encoding="utf-8").values.tolist()
    print(df)
    return render_template('F3.html', title='アルゴリズムとデータ構造',df=df)

@app.route('/attenpt22')
def ttt22():
    df = pd.read_csv('./subject.templates/F4_1.csv',keep_default_na=False,header=None,index_col=False,encoding="utf-8").values.tolist()
    print(df)
    return render_template('F4_1.html', title='文学・文化学(F4_1)',df=df)

@app.route('/attenpt23')
def ttt23():
    df = pd.read_csv('./subject.templates/F4_2.csv',keep_default_na=False,header=None,index_col=False,encoding="utf-8").values.tolist()
    print(df)
    return render_template('F4_2.html', title='心理学(F4_2)',df=df)


@app.route("/download")
def downfile():
    p="./subject.templates/M1.csv"
    return send_file(p,as_attachment=True)

@app.route("/download1")
def downfile1():
    p="./subject.templates/M2.csv"
    return send_file(p,as_attachment=True)

@app.route("/download2")
def downfile2():
    p="./subject.templates/M3.csv"
    return send_file(p,as_attachment=True)

@app.route("/download3")
def downfile3():
    p="./subject.templates/M4.csv"
    return send_file(p,as_attachment=True)

@app.route("/download4")
def downfile4():
    p="./subject.templates/T2.csv"
    return send_file(p,as_attachment=True)

@app.route("/download5")
def downfile5():
    p="./subject.templates/T3_1.csv"
    return send_file(p,as_attachment=True)

@app.route("/download6")
def downfile6():
    p="./subject.templates/T3_2.csv"
    return send_file(p,as_attachment=True)

@app.route("/download7")
def downfile7():
    p="./subject.templates/T4.csv"
    return send_file(p,as_attachment=True)

@app.route("/download8")
def downfile8():
    p="./subject.templates/T5.csv"
    return send_file(p,as_attachment=True)

@app.route("/download9")
def downfile9():
    p="./subject.templates/W12.csv"
    return send_file(p,as_attachment=True)

@app.route("/download10")
def downfile10():
    p="./subject.templates/W3_1.csv"
    return send_file(p,as_attachment=True)

@app.route("/download11")
def downfile11():
    p="./subject.templates/W3_2.csv"
    return send_file(p,as_attachment=True)

@app.route("/download12")
def downfile12():
    p="./subject.templates/W4.csv"
    return send_file(p,as_attachment=True)

@app.route("/download13")
def downfile13():
    p="./subject.templates/W5_1.csv"
    return send_file(p,as_attachment=True)

@app.route("/download14")
def downfile14():
    p="./subject.templates/W5_2.csv"
    return send_file(p,as_attachment=True)

@app.route("/download15")
def downfile15():
    p="./subject.templates/Th2.csv"
    return send_file(p,as_attachment=True)

@app.route("/download16")
def downfile16():
    p="./subject.templates/Th34.csv"
    return send_file(p,as_attachment=True)

@app.route("/download17")
def downfile17():
    p="./subject.templates/Th5_1.csv"
    return send_file(p,as_attachment=True)

@app.route("/download18")
def downfile18():
    p="./subject.templates/Th5_2.csv"
    return send_file(p,as_attachment=True)

@app.route("/download19")
def downfile19():
    p="./subject.templates/F1.csv"
    return send_file(p,as_attachment=True)

@app.route("/download20")
def downfile20():
    p="./subject.templates/F2.csv"
    return send_file(p,as_attachment=True)

@app.route("/download21")
def downfile21():
    p="./subject.templates/F3.csv"
    return send_file(p,as_attachment=True)

@app.route("/download22")
def downfile22():
    p="./subject.templates/F4_1.csv"
    return send_file(p,as_attachment=True)

@app.route("/download23")
def downfile23():
    p="./subject.templates/F4_2.csv"
    return send_file(p,as_attachment=True)

if __name__=="__main__":
    app.run(debug=True)