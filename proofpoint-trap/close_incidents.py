"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""
from connectors.core.connector import get_logger
from .utils import invoke_rest_endpoint
from .constants import LOGGER_NAME

logger = get_logger(LOGGER_NAME)


def close_incidents(config, params):
    incidentIDs = params.get('incidentIDs')
    closeSummary = params.get('closeSummary')
    closeDetail = params.get('closeDetail')
    if isinstance(incidentIDs, list):
        endpoint = '/api/incidents/close.json'
        data = {'incidentIds': incidentIDs, 'summary': closeSummary, 'detail': closeDetail}
    if isinstance(incidentIDs, int):
        endpoint = '/api/incidents/{0}/close.json'.format(incidentIDs)
        data = {'summary': closeSummary, 'detail': closeDetail}

    response = invoke_rest_endpoint(config, endpoint, 'POST', data=data)
    return response
