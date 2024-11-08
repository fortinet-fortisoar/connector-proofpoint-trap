"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""
from connectors.core.connector import get_logger, ConnectorError
from .utils import invoke_rest_endpoint
from .constants import LOGGER_NAME

logger = get_logger(LOGGER_NAME)


def get_incident_details(config, params):
    incidentid = params.get('incidentID')

    endpoint = '/api/incidents/{0}.json'.format(incidentid)
    logger.debug('ENDPOINT = {}'.format(endpoint))
    response = invoke_rest_endpoint(config, endpoint, 'GET')
    return response
