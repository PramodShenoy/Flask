from flask import Flask,jsonify,request
app=Flask(__name__)

animals=[{'name':'cats'},{'name':'dogs'},{'name':'python'},{'name':'leopard'}]

@app.route('/',methods=['GET'])
def test():
	return jsonify({"msg":"working"})

@app.route('/animals',methods=['GET'])
def zoo():
	return jsonify({"animals":animals})

@app.route('/animals/<string:name>',methods=['GET'])
def show(name):
	animal=[a for a in animals if a['name']==name]
	return jsonify({'animal':animal[0]})

if __name__=='__main__':
	app.run(debug=True,port=1234)
