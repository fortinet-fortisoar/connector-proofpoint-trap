"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""
from .utils import invoke_rest_endpoint
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME

logger = get_logger(LOGGER_NAME)


def health_check(config=None, *args, **kwargs):
    endpoint = '/api/incidents?state=ignored'
    invoke_rest_endpoint(config, endpoint, 'GET')
    return 'Connector is Available'
