import json
import logging
import time
from argparse import ArgumentParser, ArgumentTypeError

# local imports
import tmrl.config.config_constants as cfg
import tmrl.config.config_objects as cfg_obj
from tmrl.envs import GenericGymEnv
from tmrl.networking import Server, Trainer, RolloutWorker
from tmrl.tools.check_environment import check_env_tm20lidar, check_env_tm20full
from tmrl.tools.record import record_reward_dist
from tmrl.util import partial

check_env_tm20full()