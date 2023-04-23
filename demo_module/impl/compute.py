from demo_module.impl.arg_parse import parse_args
import numpy as np

VARIANT = parse_args().variant

if VARIANT == "numba".casefold():
    import numba as nb

M, N = parse_args().task_size


def compute_init(m, n):
    values = np.random.random(m * n).reshape(m, n)
    return values


def compute_update(frame, values):
    values += np.random.uniform(-1.0, 1.0, values.shape[0] * values.shape[1]).reshape(values.shape)
    return values
