import logging

from flask import Blueprint, jsonify

from server.db.managers.aircraft_manager import AircraftManager

aircraft_blueprint = Blueprint('aircraft_blueprint', __name__)
logger = logging.getLogger(__name__)


@aircraft_blueprint.route('/api/aircraft', methods=['GET'])
def get_all_zips():
    aircraft = AircraftManager.all()
    return jsonify([a.to_json() for a in aircraft])

