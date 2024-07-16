from flask import Flask, request, jsonify
import utils

app = Flask(__name__)

@app.route('/get_location_name')
def get_location_name():
    response = jsonify({
        'locations': utils.get_location_name()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    
    estimated_price = utils.get_estimated_price(total_sqft, bhk, bath, location)
    
    response = jsonify({
        'estimated_price': estimated_price
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == '__main__':
    app.run(debug=True)
