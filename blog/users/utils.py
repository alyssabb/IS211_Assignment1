from werkzeug.security import generate_password_hash
from users.models import User

# Creates a demo user
def create_demo_user(db):
    new_user = User(username="admin", password="admin")
    db.session.add(new_user)
    db.session.commit()
    print("Demo user created")