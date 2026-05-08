from flask import Flask, request, jsonify

app = Flask(__name__)

productos = [
    {"id": 1, "Nombre": "Smart TV", "Precio": 300000},
    {"id": 2, "Nombre": "Heladera", "Precio": 200000},
    {"id": 3, "Nombre": "Cocina", "Precio": 150000},
    {"id": 4, "Nombre": "Aire Acondicionado", "Precio": 500000},
    {"id": 5, "Nombre": "Ventilador", "Precio": 10000}, 
    {"id": 6, "Nombre": "Bicicleta", "Precio": 15000},
    {"id": 7, "Nombre": "Microondas", "Precio": 20000}
]

carrito = []

#Lista prodductos
@app.route('/productos', methods=['GET'])
def lista_productos():
    return jsonify(productos)

#agregar al carrito
@app.route('/carrito', methods=['POST'])
def agregar_carrtito():
    data = request.get_json()
    id_producto = data.get("id")

    producto = None
    for p in productos:
        if p['id'] == id_producto:
            producto = p
            break

    if not producto:
        return jsonify({"Mensaje": "Producto no encontrado"}), 404
        
    carrito.append(producto)
    return jsonify({"Mensaje": "Producto agregado", "carrito": carrito})

#eliminar del carrito
@app.route('/carrito/<int:id>', methods=['DELETE'])
def eliminar_carrito(id):
    global carrito

    nuevo_carrito = []
    for p in carrito:
        if p['id'] != id:
            nuevo_carrito.append(p)

    carrito = nuevo_carrito
    return jsonify({"Mensaje": "Producto eliminado", "carrito": carrito})

#ver carrito
@app.route('/carrito', methods=['GET'])
def ver_carrito():
    return jsonify(carrito)

#ver total
@app.route('/carrito/total', methods=['GET'])
def total():
    total = 0

    for p in carrito:
        total += p['Precio']

    return jsonify({"total": total})