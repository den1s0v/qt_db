# qt_db_web_server.py

import sys

from flask import Flask, request, render_template, jsonify, url_for, redirect

from options import DEBUG, HOST, PORT

if not DEBUG:
	from waitress import serve

def create_app():

	# cache = Cache(config={'CACHE_TYPE': 'simple'})

	app = Flask(__name__, template_folder='views', static_folder='static',)

	# bind the cache instance on to the app
	# cache.init_app(app)

	@app.route('/index.html')
	@app.route('/index/')
	@app.route('/')
	def index():
		return render_template('index.html')

	@app.route('/demo/')
	@app.route('/iswc/demo/')
	def demo():
		return render_template('demo.html')

	@app.route('/api_test/')
	@app.route('/test/')
	def api_test():
		return render_template('api_test.html')

	@app.route('/blockly_test/<lang>/')
	@app.route('/blockly_test/')
	def blockly_test(lang='en'):
		return render_template('blockly_test.html', language=lang)

	# app.add_url_rule('/favicon.ico',
	#                  redirect_to=url_for('static',
	#                  	filename='letter-c (Abrrakhlaed2626).png'))
	@app.route('/favicon.ico')
	def icon():
		url = url_for('static', filename='letter-c (Abrrakhlaed2626).png')
		return redirect(url)
		# return render_template('index.html')
	# # from flask import send_from_directory
	# def favicon():
	#     return send_from_directory(os.path.join(app.root_path, 'static'),
	#                           'favicon.ico',mimetype='image/vnd.microsoft.icon')

	@app.errorhandler(404)
	def http_404_handler(error):
		# return "<p>HTTP 404 Error Encountered</p>", 404
		if not 'static' in request.url:
			url = url_for('static', filename=request.path)
			return redirect(url)

		url = url_for('index')
		return '<p>HTTP 404 (Not Found) Error Encountered</p><p>Requested URL: %s</p>Get me <a href="%s">Home</a>' % (request.url, url), 404
		# return redirect(url)

	return app


if __name__ == "__main__":

	# first, use defaults from options
	host = HOST
	port = PORT

	# check if some config passed on the command line
	for arg in sys.argv[1:]:
		if arg.startswith('host='):
			host = arg.replace('host=', '')
			print("Using host specified on command line:", host)
		elif arg.startswith('port='):
			port = arg.replace('port=', '')
			print("Using port specified on command line:", port)
			port = int(port)  # convert & ensure valid int :)


	app = create_app()  # Flask app

	if DEBUG:
		app.run(debug=DEBUG, host=host, port=port)
	else:
		serve(app, host=host, port=port)
