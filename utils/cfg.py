import os
import json
import logging
import configparser

G_CONFIG_DICT = dict()


def load_cfg(f_path, args='', mode='cmd'):
    """Load config with config.ini"""
    global G_CONFIG_DICT

    # load from ini file
    cfg_dict = dict()
    if not os.path.exists(f_path):
        logging.error(f'{f_path} does not exist!')
        return cfg_dict

    cfp = configparser.ConfigParser()
    cfp.read(f_path,encoding='UTF-8')
    sections = cfp.sections()
    for section in sections:
        options = cfp.options(section)
        for option in options:
            key = section + '.' + option
            value = cfp.get(section, option)
            cfg_dict[key.lower()] = value

    # if mode is 'cmd', load from cmd args
    if mode == 'cmd' and args:
        options_dict = json.loads(args)
        for key, value in options_dict.items():
            cfg_dict[key] = value
    G_CONFIG_DICT = cfg_dict
