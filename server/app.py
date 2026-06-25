from flask import request, session
from config import app, db
from models import User, Task


@app.route("/")
def home():
    return {"message": "Flask sessions API is running!"}, 200


@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    if data.get("password") != data.get("password_confirmation"):
        return {"errors": ["Passwords do not match."]}, 422

    if User.query.filter_by(username=data.get("username")).first():
        return {"errors": ["Username already exists."]}, 422

    try:
        user = User(
            username=data.get("username"),
            email=f'{data.get("username")}@example.com',
        )
        user.password = data.get("password")

        db.session.add(user)
        db.session.commit()

        session["user_id"] = user.id

        return user.to_dict(rules=("tasks",)), 201

    except Exception as e:
        db.session.rollback()
        return {"errors": [str(e)]}, 422


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    user = User.query.filter_by(username=data.get("username")).first()

    if user and user.authenticate(data.get("password")):
        session["user_id"] = user.id
        return user.to_dict(rules=("tasks",)), 200

    return {"errors": ["Invalid username or password"]}, 401


@app.route("/logout", methods=["DELETE"])
def logout():
    session.pop("user_id", None)
    return {}, 204


@app.route("/check_session", methods=["GET"])
def check_session():
    user = User.query.get(session.get("user_id"))

    if not user:
        return {"errors": ["Unauthorized"]}, 401

    return user.to_dict(rules=("tasks",)), 200


@app.route("/me", methods=["GET"])
def me():
    user = User.query.get(session.get("user_id"))

    if not user:
        return {"errors": ["Unauthorized"]}, 401

    return user.to_dict(rules=("tasks",)), 200


@app.route("/tasks", methods=["GET", "POST"])
def tasks():
    user = User.query.get(session.get("user_id"))

    if not user:
        return {"errors": ["Unauthorized"]}, 401

    if request.method == "GET":
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", 5, type=int)

        pagination = Task.query.filter_by(user_id=user.id).paginate(
            page=page,
            per_page=per_page,
            error_out=False,
        )

        return {
            "tasks": [task.to_dict() for task in pagination.items],
            "page": pagination.page,
            "per_page": pagination.per_page,
            "total": pagination.total,
            "pages": pagination.pages,
        }, 200

    data = request.get_json()

    try:
        task = Task(
            title=data.get("title"),
            description=data.get("description"),
            priority=data.get("priority", "medium"),
            completed=data.get("completed", False),
            user_id=user.id,
        )

        db.session.add(task)
        db.session.commit()

        return task.to_dict(), 201

    except Exception as e:
        db.session.rollback()
        return {"errors": [str(e)]}, 400


@app.route("/tasks/<int:id>", methods=["GET", "PATCH", "DELETE"])
def task_by_id(id):
    user = User.query.get(session.get("user_id"))

    if not user:
        return {"errors": ["Unauthorized"]}, 401

    task = Task.query.filter_by(id=id, user_id=user.id).first()

    if not task:
        return {"errors": ["Task not found."]}, 404

    if request.method == "GET":
        return task.to_dict(), 200

    if request.method == "PATCH":
        data = request.get_json()

        try:
            for attr in ["title", "description", "priority", "completed"]:
                if attr in data:
                    setattr(task, attr, data[attr])

            db.session.commit()
            return task.to_dict(), 200

        except Exception as e:
            db.session.rollback()
            return {"errors": [str(e)]}, 400

    db.session.delete(task)
    db.session.commit()

    return {}, 204


if __name__ == "__main__":
    app.run(port=5555, debug=True)