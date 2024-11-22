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


def get_incidents(config, params):
    state = params.get('state')
    state = state.lower()
    createdAfterDate = params.get('createdAfterDate')
    createdBeforeDate = params.get('createdBeforeDate')
    emailMessageID = params.get('emailMessageID')
    if createdAfterDate and createdBeforeDate and state and emailMessageID:
        endpoint = '/api/incidents?state={0}&created_after={1}&created_before={2}&message_id={3}'.format(state, createdAfterDate, createdBeforeDate, emailMessageID)
    elif createdAfterDate and createdBeforeDate and state:
        endpoint = '/api/incidents?state={0}&created_after={1}&created_before={2}'.format(state, createdAfterDate, createdBeforeDate)
    elif state and createdAfterDate:
        endpoint = '/api/incidents?state={0}&created_after={1}'.format(state, createdAfterDate)
    elif state and createdBeforeDate:
        endpoint = '/api/incidents?state={0}&created_before={1}'.format(state, createdBeforeDate)
    elif state and emailMessageID:
        endpoint = '/api/incidents?state={0}&message_id={1}'.format(state,emailMessageID)
    elif createdAfterDate and createdBeforeDate:
        endpoint = '/api/incidents?createdAfterDate={0}&created_before={1}'.format(createdAfterDate, createdBeforeDate)
    elif emailMessageID:
        endpoint = '/api/incidents?message_id={0}'.format(emailMessageID)
    elif createdAfterDate:
        endpoint = '/api/incidents?created_after={0}'.format(createdAfterDate)
    elif createdBeforeDate:
        endpoint = '/api/incidents?created_before={0}'.format(createdBeforeDate)
    else:
        endpoint = '/api/incidents?state={0}'.format(state)


    response = invoke_rest_endpoint(config, endpoint, 'GET')
    return response