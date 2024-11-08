"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""
import requests
from connectors.core.connector import get_logger, ConnectorError
from .utils import invoke_rest_endpoint
from .constants import LOGGER_NAME
logger = get_logger(LOGGER_NAME)


def get_incidents(config, params):
    state : str= params.get('state')
    if not state:
        raise ConnectorError('Missing required parameters state')
    state = state.lower()
    createdAfterDate = params.get('createdAfterDate')
    createdBeforeDate = params.get('createdBeforeDate')
    closedAfterDate = params.get('closedAfterDate')
    closedBeforeDate = params.get('closedBeforeDate')
    if createdAfterDate and createdBeforeDate and closedAfterDate and closedBeforeDate and state:
      endpoint = '/api/incidents?state={0}&created_after={1}&created_before={2}&closed_after={3}&closed_before={4}&expand_events=true'.format(state, createdAfterDate, createdBeforeDate, closedAfterDate, closedBeforeDate)
    elif createdAfterDate and createdBeforeDate and closedAfterDate and state:
      endpoint = '/api/incidents?state={0}&created_after={1}&created_before={2}&closed_after={3}&expand_events=true'.format(state, createdAfterDate, createdBeforeDate, closedAfterDate)
    elif createdAfterDate and createdBeforeDate and closedBeforeDate and state:
      endpoint = '/api/incidents?state={0}&created_after={1}&created_before={2}&closed_before={3}&expand_events=true'.format(state, createdAfterDate, createdBeforeDate, closedBeforeDate)
    elif createdAfterDate and closedAfterDate and closedBeforeDate and state:
      endpoint = '/api/incidents?state={0}&created_after={1}&closed_after={2}&closed_before={3}&expand_events=true'.format(state, createdAfterDate, closedAfterDate, closedBeforeDate)
    elif createdBeforeDate and closedAfterDate and closedBeforeDate and state:
      endpoint = '/api/incidents?state={0}&created_before={1}&closed_after={2}&closed_before={3}&expand_events=true'.format(state, createdBeforeDate, closedAfterDate, closedBeforeDate)
    elif createdAfterDate and createdBeforeDate and state:
      endpoint = '/api/incidents?state={0}&created_after={1}&created_before={2}&expand_events=true'.format(state, createdAfterDate, createdBeforeDate)
    elif closedAfterDate and closedBeforeDate and state:
      endpoint = '/api/incidents?state={0}&closed_after={1}&closed_before={2}&expand_events=true'.format(state, closedAfterDate, closedBeforeDate)
    elif createdAfterDate and state:
      endpoint = '/api/incidents?state={0}&created_after={1}&expand_events=true'.format(state, createdAfterDate)
    elif createdBeforeDate and state:
      endpoint = '/api/incidents?state={0}&created_before={1}&expand_events=true'.format(state, createdBeforeDate)
    elif closedAfterDate and state:
      endpoint = '/api/incidents?state={0}&closed_after={1}&expand_events=true'.format(state, closedAfterDate)
    elif closedBeforeDate and state:
      endpoint = '/api/incidents?state={0}&closed_before={1}&expand_events=true'.format(state, closedBeforeDate)
    elif state:
      endpoint = '/api/incidents?state={0}&expand_events=true'.format(state)
    else:
      raise ConnectorError('Missing required parameters state')
      
    logger.debug('GET INCIDENT FILTER ENDPOINT = {}'.format(endpoint))
    response = invoke_rest_endpoint(config, endpoint, 'GET')
    return response