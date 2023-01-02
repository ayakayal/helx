from typing import Any

import bsuite.environments
import dm_env
import gym.core
import gymnasium.core

from .envs.bsuite import FromBsuiteEnv
from .envs.dm_env import FromDmEnv
from .envs.gym import FromGymEnv
from .envs.gymnasium import FromGymnasiumEnv


def make_from(env: Any) -> Any:
    if isinstance(env, gymnasium.core.Env):
        return FromGymnasiumEnv(env)
    elif isinstance(env, gym.core.Env):
        return FromGymEnv(env)
    elif isinstance(env, dm_env.Environment):
        return FromDmEnv(env)
    elif isinstance(env, bsuite.environments.Environment):
        return FromBsuiteEnv(env)
    else:
        raise TypeError(
            f"Environment type {type(env)} is not supported. "
            "Only gymnasium, gym, dm_env and bsuite environments are supported."
        )
