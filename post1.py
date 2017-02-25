from flask import Flask,jsonify,request
import json
app=Flask(__name__)

animals=[{'name':'cats'},{'name':'dogs'},{'name':'python'},{'name':'leopard'}]

@app.route('/',methods=['GET'])
def test():
	return jsonify({"msg":"working"})

@app.route('/animals',methods=['POST'])
def updateList():
	data=request.data
	data=json.loads(data)
	animals.append(data)
	return jsonify({'my new animal':animals})

if __name__=='__main__':
	app.run(debug=True,port=1111)
