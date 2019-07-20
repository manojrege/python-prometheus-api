import yaml
import requests
from requests.exceptions import HTTPError
import traceback

from promapi.__init__ import get_data

config = yaml.safe_load(open(get_data("config.yml")))


def set_endpoint(url, port):
    """
    Sets the prometheus endpoint base url
    :param hostname: Prometheus endpoint
    :param port: Prometheus port number
    :return:
    """
    config['prometheus']['url'] = url
    config['prometheus']['port'] = port


def query_instant(query, time=None, timeout=None):
    """
    Evaluates an instant query at a single point in time
    :param query: Prometheus expression query string
    :param time: Evaluation timestamp
    :param timeout: Evaluation timeout
    :return: Query result
    """
    try:
        response = requests.get(
            '{}:{}{}'.format(
                config['prometheus']['url'],
                config['prometheus']['port'],
                config['prometheus']['endpoints']['instant_query']),
            params={
                'query': query,
                'time': time,
                'timeout': timeout})
        response.raise_for_status()
    except HTTPError as http_err:
        print('HTTP Error {}'.format(http_err))
        return response.status_code, response.content
    except Exception as err:
        traceback.print_exc()
        print('Error {}'.format(err))
    else:
        results = response.json()['data']['result']
        return response.status_code, results


def query_range(query, start, end, step, timeout=None):
    """
    Evaluates an expression query over a range of time
    :param query: Prometheus expression query string
    :param start: Start timestamp
    :param end: End timestamp
    :param step: Query resolution step width in duration format or float number of seconds
    :param timeout: Evaluation timeout
    :return: Query result
    """
    try:
        response = requests.get(
            '{}:{}{}'.format(
                config['prometheus']['url'],
                config['prometheus']['port'],
                config['prometheus']['endpoints']['range_query']),
            params={
                'query': query,
                'start': start,
                'end': end,
                'step': step,
                'timeout': timeout})
        response.raise_for_status()
    except HTTPError as http_err:
        print('HTTP Error {}'.format(http_err))
        return response.status_code, response.content
    except Exception as err:
        traceback.print_exc()
        print('Error {}'.format(err))
    else:
        results = response.json()['data']['result']
        return response.status_code, results


def query_metadata_series(match, start=None, end=None):
    """
    Finds series by label matchers
    :param match: Repeated series selector argument that selects the series to return
    :param start: Start timestamp
    :param end: End timestamp
    :return: Finds series by label matchers
    """
    try:
        response = requests.get(
            '{}:{}{}'.format(
                config['prometheus']['url'],
                config['prometheus']['port'],
                config['prometheus']['endpoints']['label_matcher_series_query']),
            params={
                'match[]': match,
                'start': start,
                'end': end})
        response.raise_for_status()
    except HTTPError as http_err:
        print('HTTP Error {}'.format(http_err))
        return response.status_code, response.content
    except Exception as err:
        traceback.print_exc()
        print('Error {}'.format(err))
    else:
        results = response.json()['data']
        return response.status_code, results


def query_label_names():
    """
    Returns a list of label names
    :return: Prometheus Label names
    """
    try:
        response = requests.get(
            '{}:{}{}'.format(
                config['prometheus']['url'],
                config['prometheus']['port'],
                config['prometheus']['endpoints']['label_names_query']))
        response.raise_for_status()
    except HTTPError as http_err:
        print('HTTP Error {}'.format(http_err))
        return response.status_code, response.content
    except Exception as err:
        traceback.print_exc()
        print('Error {}'.format(err))
    else:
        results = response.json()['data']
        return response.status_code, results


def query_label_values(label_name):
    """
    Returns a list of string label values for a given label
    :param label_name: Label name
    :return: Prometheus label values for the label name
    """
    try:
        response = requests.get(
            '{}:{}{}'.format(
                config['prometheus']['url'],
                config['prometheus']['port'],
                config['prometheus']['endpoints']['label_values_query'].replace(
                    '<label_name>',
                    label_name)))
        response.raise_for_status()
    except HTTPError as http_err:
        print('HTTP Error {}'.format(http_err))
        return response.status_code, response.content
    except Exception as err:
        traceback.print_exc()
        print('Error {}'.format(err))
    else:
        results = response.json()['data']
        return response.status_code, results


def query_targets():
    """
    returns an overview of the current state of the Prometheus target discovery
    :return: State of Prometheus target discovery
    """
    try:
        response = requests.get(
            '{}:{}{}'.format(
                config['prometheus']['url'],
                config['prometheus']['port'],
                config['prometheus']['endpoints']['targets_query']))
        response.raise_for_status()
    except HTTPError as http_err:
        print('HTTP Error {}'.format(http_err))
        return response.status_code, response.content
    except Exception as err:
        traceback.print_exc()
        print('Error {}'.format(err))
    else:
        results = response.json()['data']
        return response.status_code, results


def query_rules():
    """
    returns a list of currently loaded alerting and recording rules
    :return: Alerting and recording rules
    """
    try:
        response = requests.get(
            '{}:{}{}'.format(
                config['prometheus']['url'],
                config['prometheus']['port'],
                config['prometheus']['endpoints']['rules_query']))
        response.raise_for_status()
    except HTTPError as http_err:
        print('HTTP Error {}'.format(http_err))
        return response.status_code, response.content
    except Exception as err:
        traceback.print_exc()
        print('Error {}'.format(err))
    else:
        results = response.json()['data']
        return response.status_code, results


def query_alerts():
    """
    returns a list of all active alerts
    :return: Active alerts
    """
    try:
        response = requests.get(
            '{}:{}{}'.format(
                config['prometheus']['url'],
                config['prometheus']['port'],
                config['prometheus']['endpoints']['alerts_query']))
        response.raise_for_status()
    except HTTPError as http_err:
        print('HTTP Error {}'.format(http_err))
        return response.status_code, response.content
    except Exception as err:
        traceback.print_exc()
        print('Error {}'.format(err))
    else:
        results = response.json()['data']
        return response.status_code, results


def query_target_metadata(match_target=None, metric=None, limit=None):
    """
    Returns metadata about metrics scraped by targets
    :param match_target:  Label selectors that match targets by their label sets.
    :param metric: A metric name to retrieve metadata
    :param limit: Maximum number of targets to match
    :return: Returns metadata about metrics scraped by targets
    """
    try:
        response = requests.get(
            '{}:{}{}'.format(
                config['prometheus']['url'],
                config['prometheus']['port'],
                config['prometheus']['endpoints']['targets_metatdata_query']),
            params={
                'match_target': match_target,
                'metric': metric,
                'limit': limit})
        response.raise_for_status()
    except HTTPError as http_err:
        print('HTTP Error {}'.format(http_err))
        return response.status_code, response.content
    except Exception as err:
        traceback.print_exc()
        print('Error {}'.format(err))
    else:
        results = response.json()['data']
        return response.status_code, results


def query_alertmanagers():
    """
    returns info on current state of the Prometheus alertmanager discovery
    :return: current state of the Prometheus alertmanager discovery
    """
    try:
        response = requests.get(
            '{}:{}{}'.format(
                config['prometheus']['url'],
                config['prometheus']['port'],
                config['prometheus']['endpoints']['alermanagers_query']))
        response.raise_for_status()
    except HTTPError as http_err:
        print('HTTP Error {}'.format(http_err))
        return response.status_code, response.content
    except Exception as err:
        traceback.print_exc()
        print('Error {}'.format(err))
    else:
        results = response.json()['data']
        return response.status_code, results


def query_status_config():
    """
    returns currently loaded configuration file content
    :return: Configurattion file content
    """
    try:
        response = requests.get(
            '{}:{}{}'.format(
                config['prometheus']['url'],
                config['prometheus']['port'],
                config['prometheus']['endpoints']['status_config_query']))
        response.raise_for_status()
    except HTTPError as http_err:
        print('HTTP Error {}'.format(http_err))
        return response.status_code, response.content
    except Exception as err:
        traceback.print_exc()
        print('Error {}'.format(err))
    else:
        results = response.json()['data']
        return response.status_code, results


def query_status_flags():
    """
    Returns flag values that Prometheus was configured with
    :return: Status flags
    """
    try:
        response = requests.get(
            '{}:{}{}'.format(
                config['prometheus']['url'],
                config['prometheus']['port'],
                config['prometheus']['endpoints']['status_flags_query']))
        response.raise_for_status()
    except HTTPError as http_err:
        print('HTTP Error {}'.format(http_err))
        return response.status_code, response.content
    except Exception as err:
        traceback.print_exc()
        print('Error {}'.format(err))
    else:
        results = response.json()['data']
        return response.status_code, results


def create_snapshot(skip_head=False):
    """
    Creates a snapshot of all current data into snapshots/<datetime>-<rand> under the TSDB's data directory and returns the directory as response
    :param skip_head: Boolean flag If True skips head
    :return: snapshot of all current data into snapshots/<datetime>-<rand> under the TSDB's data directory and returns the directory as response
    """
    try:
        response = requests.post(
            '{}:{}{}'.format(
                config['prometheus']['url'],
                config['prometheus']['port'],
                config['prometheus']['endpoints']['tsdb_snapshot_query']),
            params={
                'skip_head': skip_head})
        response.raise_for_status()
    except HTTPError as http_err:
        print('HTTP Error {}'.format(http_err))
        return response.status_code, response.content
    except Exception as err:
        traceback.print_exc()
        print('Error {}'.format(err))
    else:
        results = response.json()['data']
        return response.status_code, results


def delete_series(match, start, end):
    """
    Deletes data for a selection of series in a time range
    :return: 204 if deletion is successful
    """
    try:
        response = requests.get(
            '{}:{}{}'.format(
                config['prometheus']['url'],
                config['prometheus']['port'],
                config['prometheus']['endpoints']['tsdb_delete_series_query']),
            params={
                'match[]': match,
                'start': start,
                'end': end})
        response.raise_for_status()
    except HTTPError as http_err:
        print('HTTP Error {}'.format(http_err))
        return response.status_code, response.content
    except Exception as err:
        print('Error {}'.format(err))
        traceback.print_exc()
    else:
        return response.status_code


def clean_tombstones():
    """
    Removes the deleted data from disk and cleans up the existing tombstones
    :return: 204 if deletion is successful
    """
    try:
        response = requests.get(
            '{}:{}{}'.format(
                config['prometheus']['url'],
                config['prometheus']['port'],
                config['prometheus']['endpoints']['clean_tombstones_query']))
        response.raise_for_status()
    except HTTPError as http_err:
        print('HTTP Error {}'.format(http_err))
        return response.status_code, response.content
    except Exception as err:
        traceback.print_exc()
        print('Error {}'.format(err))
    else:
        return response.status_code
