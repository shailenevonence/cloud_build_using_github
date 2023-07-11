from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    branch_name = os.getenv('BRANCH_NAME', 'unknown')
    if branch_name == 'evonence':
        return 'Hello World ! Evonence'
    elif branch_name == 'master':
        return 'Hello World ! master'
    elif branch_name == 'ncorium':
        return 'Hello World ! Ncorium'
    else:
        return 'Hello World ! Unknown Branch'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
