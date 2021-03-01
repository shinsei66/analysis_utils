'''Utility functions for data analysis and machine learning\
    experiment piplines.

    
Example
---------
>>> from analysis_utils.utils import *
'''

import sys
import logging
import argparse
import yaml
import datetime
from typing import Optional


def is_prime(num: int) -> bool:
    '''
    Examples
    -----------
    >>> is_prime(1)
    False
    >>> is_prime(3)
    True
    Parameters
    -----------
    num : Any integers
    
    Returns
    -----------
    Judge result that whether the num is a prime number
    '''
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, num, 2):
        if num % i == 0:
            return False

    return True


def create_logger(
        log_version_name: str,
        logger_name: Optional[str] = 'Log',
        log_path: Optional[str] = '../logs') -> logging.Logger:
    '''Function to create a logger
    Examples
    -----------
    >>> logger = create_logger(log_version_name)
    >>> logger.info('Hello World')
    
    Parameters
    ------------
    log_version_name : the name of the log files
    logger_name : if you want to set up different\
        logger, please define its name here
    log_path : directory path of log files
    Returns
    ------------
    logger : logger object
    '''
    format_str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=format_str,
                        filename=f'{log_path}/{log_version_name}.log')
    logger = logging.getLogger(logger_name)
    return logger


def get_args(Description: str) -> argparse.Namespace:
    '''Function to get a argument parser
    Examples
    ------------
    >>> args = get_args(Description)
    >>> with open(args.config_path, 'r') as f:
    ...     config = yaml.safe_load(f)
    >>> PARAMETER = config['PARAMETER']

    Commandline Usage ::

        $ python xx.py ./config/xx.yaml

    yaml file example ::
    ------------
        >>> PARAMETER : 1

    Parameters
    ------------
    Description : description of the arguments

    Returns
    ------------
    args : argument name space
    '''
    parser = argparse.ArgumentParser(description=Description)
    parser.add_argument('config_path', type=str,
                        help='Setting parameter(.yaml)')
    args = parser.parse_args()
    return args


def exp_condition_backup(
        config: dict,
        version_name: str,
        log_path: Optional[str] = './logs') -> None:
    ''' Utility function to save the experiment config yaml\
        files and the exe python scripts
    
    Examples
    ------------
    >>> exp_condition_backup(config, version_name, log_path)

    Parameters
    ------------
    config : imported config dictionary
    version_name : the name of the log file
    log_path : directory path of log files


    Returns
    ------------
    save the imported yaml file and
    the executed python scripts
    '''
    log_version_name = version_name + '_' + \
        str(datetime.datetime.now()).replace(' ', '_').replace(':', '_')[:-7]
    with open(f'{log_path}/{log_version_name}_config.yaml', 'w') as f:
        yaml.dump(config, f)
    exe_script = str(sys.argv[0])
    with open(f'{exe_script}', 'r') as op:
        scripts = op.read()
    script_name = exe_script.split('/')[-1]
    with open(f'{log_path}/{log_version_name}_{script_name}', 'w') as p:
        p.write(scripts)


def main():
    log_version_name = str(datetime.datetime.now()).replace(
        ' ', '_').replace(':', '_')[:-7] + '_Test'
    args = get_args(log_version_name)
    with open(args.config_path, 'r') as f:
        config = yaml.safe_load(f)
    LOG_PATH = config['LOG_PATH']
    logger = create_logger('test', log_path=LOG_PATH)
    logger.info(sys.argv)
    logger.info(config)
    exp_condition_backup(config, 'exp', LOG_PATH)


if __name__ == '__main__':
    main()
