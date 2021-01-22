from typing import Any, Callable, Dict, NamedTuple, Tuple
import jax.numpy as jnp
from jax.experimental.optimizers import OptimizerState


RNGKey = jnp.ndarray
Shape = Tuple[int, ...]
Params = Any
Init = Callable[[RNGKey, Shape], Tuple[Shape, Params]]
Apply = Callable[[Params, jnp.ndarray, Dict], jnp.ndarray]
InitState = Callable[[], jnp.ndarray]


class Module(NamedTuple):
    init: Init
    apply: Apply
    initial_state: InitState = None


class Optimiser(NamedTuple):
    init: Callable[[Params], OptimizerState]
    update: Callable[[OptimizerState], OptimizerState]
    params: Callable[[OptimizerState], Params]
