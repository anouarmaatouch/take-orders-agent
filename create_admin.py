from app import create_app
from extensions import db
from models import User

app = create_app()

def create_admin():
    with app.app_context():
        # Check if any user exists
        user = User.query.first()
        if not user:
            print("No users found. Creating default admin user...")
            username = input("Enter admin username (default: admin): ") or "admin"
            password = input("Enter admin password (default: admin): ") or "admin"
            company = input("Enter company name (default: My Restaurant): ") or "My Restaurant"
            phone = input("Enter Vonage phone number (default: 123456789): ") or "123456789"
            
            admin = User(
                username=username,
                company=company,
                phone_number=phone,
                agent_on=True,
                voice='sage',
                is_admin=True,
                system_prompt="You are a helpful assistant.",
                menu="Burger: $10"
            )
            admin.set_password(password)
            db.session.add(admin)
            db.session.commit()
            print(f"Admin user '{username}' created successfully!")
        else:
            print(f"Users exist. Promoting '{user.username}' to admin...")
            user.is_admin = True
            db.session.commit()
            print(f"User '{user.username}' is now an admin.")

if __name__ == "__main__":
    create_admin()
