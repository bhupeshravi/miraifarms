from flask import Flask, jsonify, render_template, request
import json
# from flask_cors import CORS


app = Flask(__name__)
# CORS(app)


@app.route('/home')
def hello_world():
  return render_template('C:/Users/Boobesh/Desktop/vegefoods/index.html')



@app.route('/fun')
def home():
  return 'Hello, home!'


if __name__ == '__main__':
    app.run()