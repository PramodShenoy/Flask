from flask import Flask,jsonify,request
app=Flask(__name__)

animals=[{'name':'cats','do i love it?':'yes'},{'name':'dogs'},{'name':'python'},{'name':'leopard'}]

@app.route('/',methods=['GET'])
def test():
	return jsonify({"msg":"working"})

@app.route('/animals',methods=['GET'])
def zoo():
	return jsonify({"animals":animals})

if __name__=='__main__':
	app.run(debug=True,port=8080)
