from flask import Flask
from flask import request
from rembg import remove

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/post",methods=['POST'])
def post():
	image = request.files['image']
	image_data = image.read()
    output = remove(image_data)
	return output

if __name__ == '__main__':
    app.run()