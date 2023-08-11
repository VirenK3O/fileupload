from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge
import os

app = Flask(__name__)
app.config['UPLOAD_DIRECTORY'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB
app.config['ALLOWED_EXTENSIONS'] = ['.jpg', '.jpeg', '.png', '.pdf']


@app.route('/')
@app.route('/index/')
def index():
	files = os.listdir(app.config['UPLOAD_DIRECTORY'])
	print(files)
	return render_template('index.html')


@app.route('/upload/', methods=['POST'])
def upload():
	try:
		file = request.files['file']

		if file:
			file.save(os.path.join(app.config['UPLOAD_DIRECTORY'], secure_filename(file.filename)))

	except:
		return "File is Larger than 16 MB limit."

	return redirect('/')


if __name__ == '__main__':
	app.run(debug=True)
