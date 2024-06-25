from flask import Flask, redirect, render_template, request, json, jsonify

app = Flask(__name__)

image_data = [
    {
        "id": 101,
        "path": "static/scorpio.jpg"
    },
    {
        "id": 102,
        "path": "static/swift.png"
    },
]

car_data = [
    {
        "id":101,
        "brand": "Mahindra",
        "name": "Scorpio",
        "status": "Available",
        "type":"ECONOMY",
        "cap":4,
        "ftype":"Petrol",
        "gtype":"Manual",
        "class":"SUV",
        "pdprice":800.00,
        "days":3,
        "tprice":2130.00,
        "path": "static/scorpio.jpg"
    },
    {
        "id":102,
        "brand": "Suzuki",
        "name": "Swift",
        "status": "Available",
        "type":"ECONOMY",
        "cap":4,
        "ftype":"Petrol",
        "gtype":"Manual",
        "class":"Hatchback",
        "pdprice":600.00,
        "days":2,
        "tprice":1130.00,
        "path": "static/swift.png"
    },
    {
        "id":103,
        "brand": "Honda",
        "name": "Amaze",
        "status": "Available",
        "type":"ECONOMY",
        "cap":4,
        "ftype":"Petrol",
        "gtype":"Manual",
        "class":"Sedan",
        "pdprice":700.00,
        "days":3,
        "tprice":2030.00,
        "path": "static/amaze.webp"
    },
    {
        "id": 104,
        "brand": "Toyota",
        "name": "Corolla",
        "status": "Available",
        "type": "ECONOMY",
        "cap": 4,
        "ftype": "Petrol",
        "gtype": "Automatic",
        "class": "Hatchback",
        "pdprice": 650.00,
        "days": 5,
        "tprice": 3250.00,
        "path": "/static/corola.jpg"
    },
    {
        "id": 105,
        "brand": "Chevrolet",
        "name": "Malibu",
        "status": "Available",
        "type": "ECONOMY",
        "cap": 4,
        "ftype": "Petrol",
        "gtype": "Manual",
        "class": "Sedan",
        "pdprice": 700.00,
        "days": 3,
        "tprice": 2030.00,
        "path": "/static/malibu.jpg"
    },
    {
        "id": 106,
        "brand": "BMW",
        "name": "4 Series",
        "status": "Available",
        "type": "LUXURY",
        "cap": 5,
        "ftype": "Diesel",
        "gtype": "Automatic",
        "class": "Coupe",
        "pdprice": 1500.00,
        "days": 4,
        "tprice": 6000.00,
        "path": "/static/bmw-4-series.png"
    },
    {
        "id": 107,
        "brand": "Audi",
        "name": "A6",
        "status": "Available",
        "type": "PREMIUM",
        "cap": 5,
        "ftype": "Electric",
        "gtype": "Automatic",
        "class": "Sedan",
        "pdprice": 1800.00,
        "days": 3,
        "tprice": 5400.00,
        "path": "/static/audia6.webp"
    },
    {
        "id": 108,
        "brand": "Nissan",
        "name": "Micra",
        "status": "Available",
        "type": "ECONOMY",
        "cap": 4,
        "ftype": "Petrol",
        "gtype": "Manual",
        "class": "Hatchback",
        "pdprice": 600.00,
        "days": 6,
        "tprice": 3600.00,
        "path": "/static/Micra.webp"
    },
    {
        "id": 109,
        "brand": "Mercedes",
        "name": "C-Class",
        "status": "Available",
        "type": "LUXURY",
        "cap": 5,
        "ftype": "Diesel",
        "gtype": "Automatic",
        "class": "Sedan",
        "pdprice": 2000.00,
        "days": 3,
        "tprice": 6000.00,
        "path": "/static/mercedes-c-class.jpg"
    }


]


@app.route('/')
def home():
   return render_template('home.html', data = car_data)


@app.route('/filer_function')
def filter_function():
    query = request.args.get("q")
    
    if not query:
        total = len(car_data)
        return render_template('carzone.html', data = car_data, totalcar = total)
    else:
        temp_data = []

        for cars in car_data:
            if query.lower() in cars['class'].lower():
                temp_data.append(cars)

        for cars in car_data:
            if query.lower() in cars['type'].lower():
                temp_data.append(cars)
        
        for cars in car_data:
            if query.lower() in cars['gtype'].lower():
                temp_data.append(cars)

        for cars in car_data:
            if query.lower() in cars['ftype'].lower():
                temp_data.append(cars)
        
        
        return jsonify(temp_data)

@app.route('/data')
def get_data():
    return jsonify(car_data)


@app.route('/carzone', methods=['post'])
def location():
    data = request.form
    return render_template('carzone.html', data = car_data)


@app.route('/checkout/<id>')
def checkout(id):
    for carid in car_data:
        if str(carid["id"]) == str(id):
            car_new_dict = carid
            total_price = car_new_dict['tprice'] + 40
            return render_template('index.html', car_newdata = car_new_dict, tnewprice = total_price)
        
    return "No Car here"



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 