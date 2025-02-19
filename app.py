from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
     return " I am Eman Tahir and im trying to deploy Flask App at Vercel"

if __name__ == '__main__':
    app.run()