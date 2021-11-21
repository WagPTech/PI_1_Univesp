from waitress import serve
import b3 
print("URL: http://techslave.com.br:5100")
serve(b3.app, host='0.0.0.0', port=5100)
