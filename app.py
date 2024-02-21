from flask import Flask, request

app = Flask(__name__)

@app.get("/stores")
def get_stores():
    return {"stores" : stores}

@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201

@app.post("/<string:store_name>/item")
def create_item(store_name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == store_name:
            new_item = {"name": request_data["name"], "price":request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return "{'error-message': 'store not found'}", 404

@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store, 200
    return "{'error_message': 'store not found'}", 404

@app.get("/store/<string:store_name>/items")
def get_store_items(store_name):
    for store in stores:
        if store["name"] == store_name:
            return store["items"]
    return "{'error_message': 'store not found'}", 404