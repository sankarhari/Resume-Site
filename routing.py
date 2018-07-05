from bottle import route, run, template

@route('/home')
def home():
	return '<h2>Welcome to bottle</h2><a href="\contact">Contact</a>'
@route('/contact')
def contact():
	return '<h2>Welcome to Contact Page</h2>'
@route('/article/<id>')
def article(id):
	return '<h2> testing REST data '+ id +'</h2>'

@route('/result/<id>/<student>')
def result(id, student):
	return '<h2>User name is:'+ student +'<br>User ID is: '+id+'</h2>'

@route('/')
def index():
	return template('index')

if __name__ == '__main__':
	run(debug = True, reloader = True)
