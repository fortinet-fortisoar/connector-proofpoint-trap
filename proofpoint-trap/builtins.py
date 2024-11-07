"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""
from .get_incident_details import get_incident_details
from .get_incidents import get_incidents
from .create_alert_from_json_source import create_alert_from_json_source

supported_operations = {
    'get_incident_details': get_incident_details,
    'get_incidents': get_incidents,
    'create_alert_from_json_source': create_alert_from_json_source
}
