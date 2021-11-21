from flask import Flask, request, render_template, jsonify
import sys
import re
import pymysql
from sqlalchemy import create_engine
import pandas as pd
import urllib.parse
import plotly
#import plotly.express as px
import plotly.graph_objects as px
import json
app = Flask(__name__)
wsgi_app = app.wsgi_app
lista = []

senha = 'Univesp123!'
db_connection_str = "mysql+pymysql://univesp:{}@localhost/univesp".format(urllib.parse.quote_plus(senha))
#db_connection_str = "mysql+pymysql://univesp:{}@techslave.com.br/univesp".format(urllib.parse.quote_plus(senha))
db_connection = create_engine(db_connection_str)

df = pd.read_sql('SELECT CODNEG FROM ativos', con=db_connection)
#('{}', '{}', '{}')
@app.route('/')
def menu():
    try:
        return render_template('index.html')
    finally:
            db_connection.dispose()
@app.route('/', methods=['POST'])
def form_post():
    acao1 = request.form['acao1']
    acao2 = request.form['acao2']
    acao3 = request.form['acao3']
    data_inicial = request.form['data_inicial']
    data_final = request.form['data_final']
    print("#####\nAções: {}, {}, {}\nData Inicial: {}\nData Final: {}\n#####".format(acao1, acao2, acao3, data_inicial, data_final))
    try:
        df1 = pd.read_sql("SELECT DTPREG, PREMED FROM precota WHERE CODNEG = '{}' AND DTPREG >= '{}' AND DTPREG <= '{}';".format(acao1, data_inicial, data_final), con=db_connection)
        df2 = pd.read_sql("SELECT DTPREG, PREMED FROM precota WHERE CODNEG = '{}' AND DTPREG >= '{}' AND DTPREG <= '{}';".format(acao2, data_inicial, data_final), con=db_connection)
        df3 = pd.read_sql("SELECT DTPREG, PREMED FROM precota WHERE CODNEG = '{}' AND DTPREG >= '{}' AND DTPREG <= '{}';".format(acao3, data_inicial, data_final), con=db_connection)
        
        fig = px.Figure()
        #df1
        #fig = px.line(df1, x="DTPREG", y="PREMED", title="Ação: {}".format(acao1))
        fig.add_scatter(x=df1['DTPREG'], y=df1['PREMED'], mode='lines', hovertext=df1['PREMED'], hoverinfo="all", name=acao1.upper())
        #df2
        fig.add_scatter(x=df2['DTPREG'], y=df2['PREMED'], mode='lines', hovertext=df2['PREMED'], hoverinfo="all", name=acao2.upper())
        #df3
        fig.add_scatter(x=df3['DTPREG'], y=df3['PREMED'], mode='lines', hovertext=df3['PREMED'], hoverinfo="all", name=acao3.upper())
        print(df1, df2, df3)
        
        fig.show()
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template('index.html', graphJSON=graphJSON)
    finally:
        db_connection.dispose()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100,  debug=True)
