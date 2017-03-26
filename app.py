from flask import render_template, request, Flask, send_file, send_from_directory
from PIL import Image

import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/img/<path:path>')
def send_js(path):
    return send_from_directory('./statics', path)

@app.route("/rec", methods = ['POST'])
def recg():
	f = request.files['file']
	fname = ''.join(random.choice("weuifhiosdjfisdn89f2023jerio290u") for i in range(5))
	f.save('./statics/' + fname + '.gif')

	print("@@@", fname)

	#img = Image.open(request.files['file'].stream)

	#r = util.Recognizing('./statics/' + fname + '.gif')
	return str("<h1>第二步, 打开图片</h1><br><a href='http://zheye.shidaixin.com/img/" + fname + ".gif'>click me!</a>")
	


if __name__ == "__main__":
    app.run(debug=True)