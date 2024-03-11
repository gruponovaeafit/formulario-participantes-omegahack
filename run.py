from app import app
# from flask_migrate import Migrate

# Assuming 'app' is your Flask application and 'db' is SQLAlchemy object
# migrate = Migrate(app, db)


if __name__ == "__main__":
    app.run(debug=True)
