from flask import Flask,jsonify,request
app=Flask(__name__)

animals=[{'name':'cats'},{'name':'dogs'},{'name':'python'},{'name':'leopard'}]

@app.route('/',methods=['GET'])
def test():
	return jsonify({"msg":"working"})

@app.route('/animals',methods=['POST'])
def updateList():
	a={'name':request.json['name']}
	animals.append(a)
	return jsonify({'my animals':animals})

if __name__=='__main__':
	app.run(debug=True,port=8080)