from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Meu primeiro site'

app.run(host='0.0.0.0', port=81)


#@app.route('/a')
#def helloWorld():
#   return 'Hello World'