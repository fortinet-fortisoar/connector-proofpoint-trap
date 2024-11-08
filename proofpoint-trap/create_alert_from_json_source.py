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


def create_alert_from_json_source(config, params):
    alertSourceID = params.get('alertSourceID')
    data = params.get('data')
    if not alertSourceID or not data:
        raise ConnectorError('Missing required parameters')
    endpoint = '/threat/json_event/events/{0}'.format(alertSourceID) 
    logger.debug('CREATE ALERT ENDPOINT = {}'.format(endpoint))
    logger.debug('CREATE ALERT DATA = {}'.format(str(data)))
    response = invoke_rest_endpoint(config, endpoint, 'POST', data=data)
    return response