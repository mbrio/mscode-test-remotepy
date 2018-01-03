"""Test code for remote debugging."""
import time


def _transform(t):
    return t / 2


t = time.time()
d = _transform(t)

print(d)
