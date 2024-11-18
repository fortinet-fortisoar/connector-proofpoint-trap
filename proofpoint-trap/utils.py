"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""
import requests
import json
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME

logger = get_logger(LOGGER_NAME)


def invoke_rest_endpoint(config, endpoint, method='GET', data=None, headers=None):
    server_address = config.get('server_address')
    port = config.get('port', '443')
    apiToken = config.get('aPIToken')
    verify_ssl = config.get('verify_ssl', True)
    if not server_address or not apiToken:
        raise ConnectorError('Missing required parameters')
    headers = {'Content-type': 'application/json', 'accept': 'application/json', 'Authorization': apiToken}
    url = '{server_address}{endpoint}'.format(server_address=server_address, endpoint=endpoint)
    try:
        response = requests.request(method, url, verify=verify_ssl,
                                    data=json.dumps(data), headers=headers)
        logger.error('RESPONSE STATUS CODE = {}'.format(str(response.status_code)))
        logger.error('RESPONSE STATUS TEXT = {}'.format(str(response.text)))
    except Exception as e:
        logger.exception('Error invoking endpoint: {0}'.format(endpoint))
        raise ConnectorError('Error: {0}'.format(str(e)))

    if response.status_code == 200 or response.status_code == 201 or response.status_code == 202:
        if response.ok and response.text:
            return response.json()
        elif response.text:
            return {"status": response.text}
        else:
            return {"status": "success"}
    else:
        logger.error(response.content)
        raise ConnectorError(response.content)

        logger.exception('Error invoking endpoint: {0}'.format(endpoint))
        raise ConnectorError('Error: {0}'.format(str(e)))

    if response.status_code == 202:
        return {"status": "success"}
    elif response.ok:
        return response.json()
    else:
        logger.error(response.content)
        raise ConnectorError(response.content)
