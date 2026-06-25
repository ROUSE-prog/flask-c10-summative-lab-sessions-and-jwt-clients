from app import app
from models import db, User, Task

with app.app_context():
    print("Deleting old data...")
    Task.query.delete()
    User.query.delete()

    print("Creating users...")

    steven = User(
        username="steven",
        email="steven@example.com",
    )
    steven.password = "password123"

    demo = User(
        username="demo",
        email="demo@example.com",
    )
    demo.password = "password123"

    db.session.add_all([steven, demo])
    db.session.commit()

    print("Creating tasks...")

    tasks = [
        Task(
            title="Build Flask API",
            description="Create models, routes, sessions, and pagination.",
            priority="high",
            completed=False,
            user_id=steven.id,
        ),
        Task(
            title="Connect React client",
            description="Use fetch requests with credentials included.",
            priority="medium",
            completed=False,
            user_id=steven.id,
        ),
        Task(
            title="Test login flow",
            description="Confirm signup, login, me, and logout work.",
            priority="high",
            completed=False,
            user_id=demo.id,
        ),
    ]

    db.session.add_all(tasks)
    db.session.commit()

    print("Done seeding!")