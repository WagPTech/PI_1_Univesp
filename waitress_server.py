from waitress import serve
import mywebdb
serve(mywebdb.app, host='0.0.0.0', port=5000)
