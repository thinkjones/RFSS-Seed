from flask import Flask, request
from flask import send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from server.db.managers.aircraft_manager import AircraftManager
from server.db.managers.maintenance_manager import MaintenanceManager
from server.db.managers.user_manager import UserManager

from db.database import db_session

app = Flask(__name__)
app.static_folder = '../client'
app.static_url_path = ''


@app.route('/')
def route_file():
    return app.send_static_file('index.html')


@app.route('/api/aircraft', methods=['GET'])
def get_all_zips():
    aircraft = AircraftManager.all()
    return jsonify([a.to_json() for a in aircraft])


@app.route('/api/maintenance/<aircraft_id>', methods=['GET'])
def get_maintenance_history(aircraft_id):
    history, to_dict = MaintenanceManager.history(aircraft_id)
    return jsonify([to_dict(h) for h in history])


@app.route('/api/maintenance/<aircraft_id>', methods=['POST'])
def add_maintenance_history(aircraft_id):
    user = get_current_real_user()
    data = request.json
    MaintenanceManager.add(user.id, aircraft_id, data['description'], data['blocked'])
    return jsonify({'success': True})


@app.route('/<path:filename>')
def send_app_files(filename):
    return send_from_directory(app.static_folder + '/', filename)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


def configure(binder):
    binder.bind(SQLAlchemy, to=db_session, scope=singleton)


def get_current_real_user():
    """ Fake Session - Session and Auth not implemented.  Just return first real user.
    """
    all_users = UserManager.all_real_users()
    return all_users[0]


if __name__ == "__main__":
    app.run()


