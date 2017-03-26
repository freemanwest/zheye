from flask import render_template, request, Flask, send_file, send_from_directory
from PIL import Image

import random

from zheye import util

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
	return str("<a href='http://localhost:5000/img/" + fname + ".gif'>click me!</a>")
	
	'''
	#r = util.Recognizing(img)
	im = util.centerExtend(img, radius=20)

	return send_file(im, as_attachment=True, attachment_filename='myfile.jpg')
	
	#get center positions
	vec = util.img2vec(im).copy()
	for i in range(vec.shape[0]):
		for j in range(vec.shape[1]):
			if vec[i][j] >= 249:
				vec[i][j] = 255

	Y = []
	for i in range(vec.shape[0]):
		for j in range(vec.shape[1]):
			if vec[i][j] <= 200:
				Y.append([i, j])
	k_means = KMeans(init='k-means++', n_clusters=7, n_init=10)
	k_means.fit(Y)
	k_means_cluster_centers = np.sort(k_means.cluster_centers_, axis=0)


	#predict UP DOWN
	points = []
	#model = keras.models.load_model('./zheye.keras')
	for i in range(7):
		p_x = k_means_cluster_centers[i][0]
		p_y = k_means_cluster_centers[i][1]

		cr = util.crop(im, p_x, p_y, radius=20)
		cr = cr.resize((40, 40), Image.ANTIALIAS)

		#X = np.asarray(cr.convert('1'), dtype='float')
		X = np.asarray(cr.convert('L'), dtype='float')

		#X = X.ravel()
		for (x,y), value in np.ndenumerate(X):
			if value > 200:
				X[x][y] = 1.0
			else:
				X[x][y] = 0.0

		x0 = np.expand_dims(X, axis=0)
		x1 = np.expand_dims(x0, axis=3)

		global model
		m_y = model.predict(x1)
		if m_y[0][0] < 0.5:
			#points.append((p_x-20, p_y-20))
			points.append((p_x, p_y))


	return str(points)
	#response = send_file(img, as_attachment=True, attachment_filename='myfile.gif')
	#return response
	'''

if __name__ == "__main__":
    app.run(debug=True)