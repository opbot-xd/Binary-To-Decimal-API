from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'This is my first API call!'


@app.route('/dtb', methods=["POST"])
def decimalToBinary():
    input_json = request.get_json(force=True)
    outputNumber = bin(int(input_json['num'])).replace("0b", "")
    dictToReturn = {'output':outputNumber}
    return jsonify(dictToReturn)   


@app.route('/btd', methods=["POST"])
def binaryToDecimal():
    input_json = request.get_json(force=True)
    if (input_json['num'])[0]!='-':
        outputNumber = int('0b'+input_json['num'],2)
    else:
        outputNumber = int('0b'+(input_json['num'])[1:],2)*-1

    dictToReturn = {'output':str(outputNumber)}
    return jsonify(dictToReturn)

if __name__=="__main__":
    app.run()