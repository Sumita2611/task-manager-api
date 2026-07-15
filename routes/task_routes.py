from flask import Blueprint, jsonify, request

task_bp = Blueprint("task", __name__)

tasks = []

next_id = 1


@task_bp.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


@task_bp.route("/tasks/<int:id>", methods=["GET"])
def get_task(id):
    for task in tasks:
        if task["id"] == id:
            return jsonify(task)

    return jsonify({"message": "Task not found"}), 404


@task_bp.route("/tasks", methods=["POST"])
def create_task():
    global next_id

    data = request.get_json()

    task = {
        "id": next_id,
        "title": data["title"],
        "completed": False
    }

    tasks.append(task)
    next_id += 1

    return jsonify(task), 201


@task_bp.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    data = request.get_json()

    for task in tasks:

        if task["id"] == id:
            task["title"] = data.get("title", task["title"])
            task["completed"] = data.get("completed", task["completed"])

            return jsonify(task)

    return jsonify({"message": "Task not found"}), 404


@task_bp.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):

    for task in tasks:

        if task["id"] == id:
            tasks.remove(task)

            return jsonify({
                "message": "Deleted successfully"
            })

    return jsonify({
        "message": "Task not found"
    }), 404