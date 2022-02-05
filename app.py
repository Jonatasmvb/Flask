from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Meu app em web com flask'

app.run(host='0.0.0.0', port=81)
