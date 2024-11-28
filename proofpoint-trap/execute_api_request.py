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


def execute_api_request(config, params):
    params = _build_payload(params)
    endpoint = params.get('endpoint')
    logger.debug('ENDPOINT = {}'.format(endpoint))
    response = invoke_rest_endpoint(config, endpoint, method=params.get('method'), data=params.get('payload', None),
                                    params=params.get('query_params', None))
    return response


def _build_payload(params: dict, options_dict: dict = {}) -> dict:
    if params.get('other_fields'):
        params.update(params.pop('other_fields'))

    return {key: options_dict.get(val, val) if isinstance(val, str) else val for key, val in params.items() if
            isinstance(val, (bool, int)) or val}
