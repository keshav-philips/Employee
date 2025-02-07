from fastapi import FastAPI

app = FastAPI()

# Sample data (dictionary to store deparments)
department = {1: {"department name": "IT"}}

# Get a department by ID
@app.get("/department/{department_id}")
def read_department(department_id: int):
    return department.get(department_id, {"error": "department not found"})

# Create a new department
@app.post("/department/{department_id}")
def create_department(department_id: int, department_name: str):
    if department_id in department:
        return {"error": "department already exists"}
    department[department_id] = {"department name": department_name}
    return {"message": "department created", "department": department[department_id]}

# Update a department
@app.put("/department/{department_id}")
def update_department(department_id: int, department_name: str):
    if department_id not in department:
        return {"error": "department not found"}
    department[department_id] = {"department name": department_name}
    return {"message": "department updated", "department": department[department_id]}

# Delete a department
@app.delete("/department/{department_id}")
def delete_department(department_id: int):
    if department_id not in department:
        return {"error": "department not found"}
    del department[department_id]
    return {"message": "department deleted"}