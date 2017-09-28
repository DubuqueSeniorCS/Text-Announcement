from flask import Flask, render_template, request, redirect
app=Flask(__name__)

message=""
@app.route('/')
def index():
	return render_template('index.html')
@app.route('/form', methods = ['POST'])
def form():
	global message
	color = request.form['color']
	message = request.form['message']
	print("this is the data '" + color + message + "'")
	message = color + " "+message
	return redirect('/')


@app.route('/announcement')
def announcement():
	return message
	
	






if __name__=='__main__':
	app.run(debug=True, host='0.0.0.0')
