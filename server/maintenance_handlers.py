import logging

from flask import Blueprint, jsonify

from server.db.managers.aircraft_manager import AircraftManager

maintenance_blueprint = Blueprint('aircraft_blueprint', __name__)
logger = logging.getLogger(__name__)


@maintenance_blueprint.route('/api/maintenance/aircraft/<aircraft_id>', methods=['GET'])
def get_all_zips(aircraft_id):
    aircraft = AircraftManager.all()
    return jsonify([a.to_json() for a in aircraft])

