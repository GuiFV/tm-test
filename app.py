from flask import Flask, jsonify
from models import db, Policy
from dotenv import load_dotenv
import os


# Load environmental variables
load_dotenv()

def create_app(config_name=None):
    # Instantiate application
    app = Flask(__name__)

    # Configure the database based on instance configuration
    if config_name == 'testing':
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    else:
        # Default to production or use configurations from .env
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database
    db.init_app(app)

    # Create tables when app loads
    with app.app_context():
        db.create_all()

    @app.route('/policy/<int:policy_id>', methods=['GET'])
    def get_item(policy_id):
        """Endpoint to retrieve policies"""
        item = db.session.get(Policy, policy_id)
        if item:
            return jsonify({'id': item.id, 'name': item.name})
        else:
            return jsonify({'error': 'Item not found'}), 404

    @app.route('/', methods=['GET'])
    def home():
        """Main application endpoint"""
        return {
            'how to retrieve policy': 'access /policy/policy_id_number',
            'policy main endpoint': 'api is working!'
        }

    return app

app = create_app()

if __name__ == '__main__':

    app.run()

