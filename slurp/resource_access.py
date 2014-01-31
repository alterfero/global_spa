__author__ = 'thor'

import random


def get_random_user_agent():
    """
    Returns a random user agent from the full list of user agents.
    Cycles through all agents before re-sampling from the full list again.
    """
    from slurp.resource_data import user_agent_list
    return random.choice(user_agent_list)