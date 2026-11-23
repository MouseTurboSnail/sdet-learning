from flask import Flask, request

app = Flask(__name__)

@app.get("/hello")
def hello():
    return "hello"

@app.get("/health")
def health():
    return "broken"

# СЛОВАРЬ
service_states = {"ssh": "running", "NetworkManager": "stopped"}

@app.get("/services")
def get_service():
    response = (service_states)
    return response

@app.get("/services/<service_name>")
def services(service_name):
    if service_name not in service_states:
        return "Service not found", 404
    response = service_states[service_name]
    return response

@app.post("/services")
def create_service():
    data = request.get_json()

    if "status" not in data:
        return "Missing status", 400
    if "name" not in data:
        return "Missing name", 400
    service_name = data['name']
    service_status = data["status"]
    if service_name in service_states:
        return "Conflict", 409
    service_states[service_name] = service_status
    # ИЛИ, короче:
    # service_states[data["name"]] = data["status"]
    return "Service created", 201

@app.patch("/services/<service_name>")
def update_service_status(service_name):
    data = request.get_json()
    if service_name not in service_states:
        return "Service not found", 404
    if "status" not in data:
        return "Missing status", 400
    service_status = data["status"]
    service_states[service_name] = service_status
    return "Service updated", 200

@app.delete("/services/<service_name>")
def delete_service(service_name):
    if service_name not in service_states:
        return "Service not found", 404
    else:
        del service_states[service_name]
        return "", 204
# ИЛИ без else (НА УРОВНЕ С if !):
#   del service_states[service_name]
#   return "", 204

