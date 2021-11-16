from flask import Flask, request, render_template, jsonify
import sys
import re
sys.path.append("/home/jhanks/.local/lib")
import pymysql
app = Flask(__name__)
wsgi_app = app.wsgi_app
lista = []
def regexp(expr, item):
    reg = re.compile(expr)
    return reg.search(item) is not None

@app.route('/')
def someName():
    db = pymysql.connect(host='localhost',
                        user='univesp',
                        password='Univesp123@',
                        database='univesp',
                        cursorclass=pymysql.cursors.DictCursor)
    try:
        
        with db.cursor() as cursor:
            sql = "SELECT CODNEG FROM ativos;"
            #sql = "SELECT CODNEG FROM ativos "
            #sql = "SELECT table_schema \"Univesp\", ROUND(SUM(data_length + index_length) / 1024 / 1024, 1) \"Size(MB)\" FROM information_schema.tables GROUP BY table_schema"
            #sql = "SELECT CODNEG FROM ativos WHERE CODNEG = \'VALE3\'"
            cursor.execute(sql)
            results  = cursor.fetchall()
            for row in results:
                lista.append(row['CODNEG'])
                #lista.append(row)

            return render_template('index3.html', results=lista)
    finally:
            db.close()
    #return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,  debug=True)

