from app import app

@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/test')
def main():
	return "hello world"