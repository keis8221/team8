import pandas as pd
df_csv = pd.read_csv('M1.csv',encoding="utf-8")
 
# <th>内の文字列を真ん中に寄せる
pd.set_option('colheader_justify', 'center')
 
html_string = '''
<html>
  <head><meta charset="UTF-8">
  <title>出欠確認画面</title>
  </head>
  <body>
  <h1>教員名
  <label for="subject">教科名</label>
    <select id="subject" >
      <option id="meat">心理学</option>
      <option id="vege">科学英語</option>
      </select>
      〇：出席　△：遅刻　✕：欠席
    </h1>

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js" integrity="sha384-q2kxQ16AaE6UbzuKqyBE9/u/KzioAlnx2maXQHiDX9d4/zp8Ok3f+M7DPm+Ib6IU" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.min.js" integrity="sha384-pQQkAEnwaBkjpqZ8RU1fF1AKtTcHJwFl3pblpTlHXybJjHpMYo79HY3hIi4NKxyj" crossorigin="anonymous"></script>
    -->
    {table}
    <link rel="stylesheet" type="text/css" href="mystyle.css"/>
  </body>
</html>.
'''
 
# OUTPUT AN HTML FILE
with open('attempt.html', 'w',encoding="utf-8") as f:
    f.write(html_string.format(table=df_csv.to_html(classes='mystyle', index=False)))
